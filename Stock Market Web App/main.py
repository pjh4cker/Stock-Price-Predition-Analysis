import streamlit as st
import pandas as pd
from PIL import Image

def init():
    # Add a title and an image
    st.write("""
             **Stock Market Web Application**
             """)

    image = Image.open("D:/VS Code/Python Projects/Stock Market Web App/Images/stock_market_image.jpg")

    st.image(image, use_column_width=True)

    # Create a sidebar header
    st.sidebar.header("User Input")

df = pd.read_csv("Stocks\list.csv")
company=list(df['Name'])

def get_input():
    start_date = st.sidebar.text_input("Start Date", "2016-02-06")
    end_date = st.sidebar.text_input("End Date", "2021-02-03")
    stock_symbol = st.sidebar.selectbox("Stock Symbol", options=company)
    return start_date, end_date, stock_symbol


def get_company_name(symbol):
    if symbol == "AMZN":
        return "Amazon"
    elif symbol == "TSLA":
        return "Tesla"
    elif symbol == "GOOG":
        return "Google"
    else:
        return None
    


def get_data(symbol, start, end):
    # Load the file
    if symbol.upper() == "AMZN":
        data_frame = pd.read_csv(
            r"D:\VS Code\Python Projects\Stock Market Web App\Stocks\AMZN.csv")
    elif symbol.upper() == "TSLA":
        data_frame = pd.read_csv(
            r"D:\VS Code\Python Projects\Stock Market Web App\Stocks\AMZN.csv")
    elif symbol.upper() == "GOOG":
        data_frame = pd.read_csv(
            r"D:\VS Code\Python Projects\Stock Market Web App\Stocks\AMZN.csv")
    else:
        data_frame = pd.DataFrame(
            columns=["Data", "Close", "Open", "Volume", "Adj Close", "High", "Low"])

    # Get the Data range
    start = pd.to_datetime(start)
    end = pd.to_datetime(end)

    # Set the start and end index rows both to 0
    start_row = 0
    end_row = 0

    for i in range(0, len(data_frame)):
        if start <= pd.to_datetime(data_frame["Date"][i]):
            start_row = i
            break

    for j in range(0, len(data_frame)):
        if end >= pd.to_datetime(data_frame["Date"][len(data_frame) - 1 - j]):
            end_row = len(data_frame) - 1 - j
            break

    # Set the index to be the date
    data_frame = data_frame.set_index(pd.DatetimeIndex(data_frame["Date"].values))

    return data_frame.iloc[start_row:end_row + 1, :]


def main():

    init()

    # Get the user input
    start, end, symbol = get_input()


    # Get the company name
    company_name = get_company_name(symbol.upper())

    try:
        # Get the data
        data_frame = get_data(symbol, start, end)

        # Display the close price
        st.header(company_name + " Close Price\n")
        st.line_chart(data_frame["Close"])

        # Display the Volume
        st.header(company_name + " Volume\n")
        st.line_chart(data_frame["Volume"])

        # Get statistics on the data
        st.header("Data Statistics")
        st.write(data_frame.describe())

    except:
        st.write("""
        # Stock Ticker couldn't be found! TRY AGAIN!!
        """)

        image = Image.open(
            "C:/Users/jaypr/OneDrive/Desktop/VS Code/Python Projects/Stock Market Web App/Images/error_page.jpg")

        st.image(image, use_column_width=True)


main()
