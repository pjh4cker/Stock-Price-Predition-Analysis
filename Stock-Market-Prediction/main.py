import streamlit as st 
from multiapp import Multiapp
from apps import compinfo, analysis, pred

main=Multiapp()

main.add_app("Stock Price Prediction", pred.app)
main.add_app("Technical Analysis", analysis.app)
main.add_app("Company Information", compinfo.app)

main.run()