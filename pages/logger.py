import streamlit as st
from streamlit.components.v1 import html
from html import unescape
import requests
import pandas as pd


# Define your javascript
my_js = """
console.log("Hello World");
"""
# Wrapt the javascript as html code
my_html = f"<script>{my_js}</script>"


# Button to print "Hello World" to the console
if st.button("Say hello world in all the consoles"):
    print("Hello World")
    # Print the log to the browser console
    st.error("Hello World")

    # Execute the javascript code
    st.components.v1.html(my_html)

# Button to make a request
if st.button("Make a request"):
    # Set a custom cookie
    cookie = {"Test": "Hello World"}

    # Make a request to the server
    response = requests.get("https://www.google.com", cookies=cookie)
    # Get the cookies from the response
    cookie = response.cookies._cookies

    # Print the response to the console
    print(cookie)
    # Print the response to the browser console as markdown
    st.markdown(cookie)

# Button to make a request to google analytics
if st.button("Ganalytics"):
    # Make a request to the server
    response = requests.get("https://analytics.google.com/analytics/web/#/p344238377/reports/reportinghub?params=_u..nav%3Dmaui")

    # Print the response to the console
    st.text(response.status_code)
    # Print the response to the browser console as markdown
    html(response.text, height=500)

# Button to make a request to google analytics with credentials
if st.button("Ganalytics with credentials"):
    # Import the necessary functions from "GA/connect.py"
    from GA.connect import initialize_analyticsreporting, get_report, handle_report

    analytics = initialize_analyticsreporting()

    global dfanalytics
    dfanalytics = []

    rows = []
    response = handle_report(analytics,'0',rows)

    dfanalytics = pd.DataFrame(list(rows))

    # Print the response to the console
    st.markdown(dfanalytics)