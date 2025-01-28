import os

# File paths
STARTUP_FILE = 'startup.txt'
DB_DIR = "C:/Users/gupta/OneDrive/Desktop/Ecell/startup software/chroma_db"

# Startup lists
INNOVATION_CENTRE_STARTUPS = ["Aion Health Solutions", "Differr", "Navmarg", "Openzo", "Kraftr", "Project Mind Matters", "Instrumus", "Ripple Technologies", "Socio Ichor","Vennbrd", "UpEase", "Bixel Studios", "Rial", "Brainso", "Thapy", "Go Perch"]
MBI_STARTUPS = ["Blackfrog Technologies", "Concipio Enterprise", "Alantis Sciences India", "Aaray Health Solutions", "Aironc Healthcare Technologies", "LEAD Molecules", "URWI Medical Innovations", "CURIOUZ Techlabs", "EikonaX Innovative Solutions", "Microbolite Research Development", "Uniarc Services", "Vyabja Ocular Innovations", "Biomed Implants and Research Technologies", "Regenco Innovations", "Drava Life Sciences", "Sciogen Biosciences", "Scires Technologies", "Biobreath Health Solutions", "Seragen Biotherapeutics", "Konkan Watercrafts", "Businexbridge Possibility Solutions", "Tad Aircon", "Blackfrog Technologies", "Iuva Foods", "Iuva Labs", "Tiny Prism Labs", "Senztech Technologies", "Ganglia Technologies", "SVN Novatech", "SENSOR", "Autorobox Artificial Intelligence & Robotics Solutions", "Auto Bhan Enterprises", "Neer Shakti Systems", "Teach Spoon Edtech"]
MUTBI_STARTUPS = ["BESTRIPTech Solutions", "Kumudha HealthTech", "OSIND Meditech", "Udupi eSamudaay Digital Services", "Co Works Solutions", "Avista E Learning", "PharmIT Solutions", "Replastiko", "Eclipse India", "Maiyas Healthcare", "IOTRACX", "Drone View Solutions", "Zupaloop", "Lakir Teachnologies", "Biosutra", "TAD Aircon", "Nimble Vision", "Panjurli Labs", "ZigMe Careers", "Malpe Meen", "Health is Wealth"]


# System prompts
CHAT_SYSTEM_PROMPT = """You are a chatbot, able to have normal interactions, as well as give
detailed explainations of different startups. In a very organised manner in pointers. New pointers have to be in new line. Email ID, Phone No, and the websites must be a hyperlink which on clicking can be redirected to that website."""
