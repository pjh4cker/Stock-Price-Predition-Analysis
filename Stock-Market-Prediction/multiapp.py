import streamlit as st

class Multiapp:
    
    def __init__(self):
        self.apps = []
        
    def add_app(self, title, func):
        
        self.apps.append({
            "title": title,
            "function": func
        })
        
    def run(self):
        st.markdown("<h1 style='text-align: center'>Stock Market Predicton And Analysis</h1>", unsafe_allow_html=True)
        app = st.selectbox(
            'Navigation',
            self.apps,
            format_func=lambda app: app['title']
        )
        app['function']()
    