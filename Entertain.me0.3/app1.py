
import streamlit as st
# Set page configuration
st.set_page_config(
    page_title="Entertain.me",
    page_icon="🎞️",
    layout="wide",
    initial_sidebar_state="expanded"
)
hide_st_style = """
    <style>
    footer  {visibility: hidden;} 
    header  {visibility: hidden;} 
    .MainMenu {visibility: hidden;} 
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

from turtle import home
import streamlit as st
from urllib.request import urlopen
from streamlit_option_menu import option_menu
import home1 as home1
import support as support 
import contact as contact 
import about as about 
import home1 
import meta.discussion as discussions

def init():
    st.sidebar.image("https://github.com/DanielVenH1337/DanielVenH1337/blob/main/Untitled-1.png?raw=true", use_column_width=True)

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        
        # Create sidebar option menu
        with st.sidebar:   
            app = option_menu(
                menu_title='',
                options=['🏠 Home','💬 Contact','💸 Support','💡 About'],
                icons=['🏠','💡','💬','💸'],
                default_index=0,
                styles={
                    "container": {"padding": "5!important","background-color":'#91A774'},
                    "icon": {"color": "white", "font-size": "23px"}, 
                    "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#B4CD96"},
                    "nav-link-selected": {"color":"black","background-color": "white"}
                }  
            )
            init()  

        # Determine which app to run based on the selected option
        if app == '🏠 Home':
            home1.app()
        elif app == '💬 Contact':
            contact.app()          
        elif app == '💡 About':
            about.app()
        elif app == '💸 Support':
            support.app()

# Instantiate the MultiApp class and run the app
multi_app = MultiApp()
multi_app.run()
