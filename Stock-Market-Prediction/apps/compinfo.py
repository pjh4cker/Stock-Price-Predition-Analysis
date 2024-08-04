import streamlit as st 
import yfinance as yf 
import datetime
import pandas as pd 

def app():
    t_list=pd.read_csv("ticker_list.txt")
    st.sidebar.header("Select Parameter")
    tickerSymbol=st.sidebar.selectbox("Company Symbol", t_list)
    ticker=yf.Ticker(tickerSymbol)
    start_date=st.sidebar.date_input("Start Date", datetime.date(2010,1,1))
    end_date=st.sidebar.date_input("End Date", datetime.date(2021,1,31))
    options=st.multiselect("Choose Information to Display", ticker.info.keys())
    
    if st.button("Display"):
        st.text("")
        st.text("")
        ticker=yf.Ticker(tickerSymbol)
        df=ticker.history(start=start_date, end=end_date)
        s_name=ticker.info('longName')
        st.header('**%s**' % s_name)
        s_logo='<img src=%s>' % ticker.info['logo_url']
        st.markdown(s_logo, unsafe_allow_html=True)
        st.text("")
        s_summary=ticker.info['longBusinessSummary']
        st.info(s_summary)
        st.header("Stock Price Data - "+ticker.info('longName'))
        st.dataframe(df)
        st.header("Line Chart of Closing Stock Price")
        st.line_chart(df['Close'])
        for opt in options:
          st.header(opt)
          st.info(ticker.info(opt))