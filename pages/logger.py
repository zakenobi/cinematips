import streamlit as st
from streamlit.components.v1 import html
from html import unescape
import requests


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
    # Make a request to the server
    response = requests.get("https://www.google.com")
    # Get the cookies from the response
    cookie = response.cookies._cookies
    # Print the response to the console
    print(cookie)
    # Print the response to the browser console as markdown
    st.markdown(cookie)

# Button to make a request to google analytics
if st.button("Ganalytics"):
    # Make a request to the server
    response = requests.get("https://analytics.google.com/analytics/web/#/p344238377/reports/intelligenthome?params=_u..nav%3Dmaui")

    # Print the response to the console
    st.text(response.status_code)
    # Print the response to the browser console as markdown
    st.markdown(response.text)

# Button to make a request to google analytics with credentials
if st.button("Ganalytics with credentials"):
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    
    # Set up the OAuth flow
    scopes = ['https://www.googleapis.com/auth/analytics.readonly']
    
    flow = InstalledAppFlow.from_client_secrets_file(
        'client_secrets.json', scopes=scopes)

    
    # Prompt the user to grant access
    creds = flow.run_console()
    
    # Save the credentials to a file
    with open('credentials.json', 'w') as f:
        f.write(creds.to_json())
    
    # Create a requests session with the credentials
    session = requests.Session()
    session.auth = Credentials.from_authorized_user_info(info=creds.to_json())
    
    # Make a request to the Google Analytics API
    response = session.get(
        'https://www.googleapis.com/analytics/v3/data/ga',
        params={
            'ids': 'ga:12345',  # Replace with your Google Analytics view ID
            'start-date': '7daysAgo',
            'end-date': 'today',
            'metrics': 'ga:sessions',
        }
    )
    
    # Print the response
    print(response.json())


    