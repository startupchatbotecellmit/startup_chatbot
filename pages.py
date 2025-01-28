import streamlit as st
from config import INNOVATION_CENTRE_STARTUPS, MUTBI_STARTUPS, MBI_STARTUPS
from utils import handle_click

def render_unified_page(chat_engine):
    # Initialize session state for messages if it doesn't exist
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    st.markdown("""
        <style>
        .stButton button {
            height: 50px;
            white-space: normal;
            text-align: center;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .custom-input-container {
            position: relative;
            height: 50px;
            width: 100%;
            max-width: 300px;
            margin: 0 auto;
            padding-top: 1rem;
        }
        .startup-messages {
            max-width: 100%;
            overflow-x: hidden;
            word-wrap: break-word;
            margin-top: 20px;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.title("Startup Incubators")
    
    # Store clicked startup in session state
    if 'clicked_startup' not in st.session_state:
        st.session_state.clicked_startup = None
    
    # First display all tabs and buttons
    tabs = st.tabs(["Innovation Centre", "MUTBI", "Manipal Bio-Incubator"])
    incubator_data = [
        (INNOVATION_CENTRE_STARTUPS, "ic", "Innovation Centre Startups"),
        (MUTBI_STARTUPS, "mutbi", "MUTBI Startups"),
        (MBI_STARTUPS, "mbi", "Manipal Bio-Incubator Startups")
    ]
    
    for tab, (startups, key, title) in zip(tabs, incubator_data):
        with tab:
            st.subheader(title)
            search_query = st.text_input(f"Search {title}", key=f"{key}_search")
            filtered_startups = [s for s in startups if search_query.lower() in s.lower()] if search_query else startups
            
            if not filtered_startups:
                st.warning("No startups found matching your search.")
                continue
                
            st.markdown(f"Showing {len(filtered_startups)} startups")
            cols = st.columns(3)
            
            for idx, startup in enumerate(filtered_startups):
                with cols[idx % 3]:
                    if st.button(
                        startup,
                        key=f"{key}_startup_{idx}",
                        use_container_width=True
                    ):
                        st.session_state.clicked_startup = startup
                        # Clear messages when new startup is selected
                        st.session_state.messages = []
    
    # Display chat interface if a startup is selected
    if st.session_state.clicked_startup:
        try:
            st.markdown('<div class="startup-messages">', unsafe_allow_html=True)
            
            # Display initial query if messages are empty
            if not st.session_state.messages:
                with st.spinner("Generating response..."):
                    response = chat_engine.chat(f"Tell me about {st.session_state.clicked_startup}")
                    st.session_state.messages.extend([
                        ("user", f"Tell me about {st.session_state.clicked_startup}"),
                        ("assistant", response.response)
                    ])
            
            # Display all messages
            for role, content in st.session_state.messages:
                with st.chat_message(role):
                    st.markdown(content)
            
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Chat input
            user_message = st.chat_input("Type your message here...")
            if user_message:
                with st.spinner("Generating response..."):
                    followup_response = chat_engine.chat(user_message)
                    st.session_state.messages.extend([
                        ("user", user_message),
                        ("assistant", followup_response.response)
                    ])
                    st.experimental_rerun()
                    
        except Exception as e:
            st.error(f"Error generating response: {str(e)}")
