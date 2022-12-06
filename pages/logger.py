import streamlit as st
from streamlit.components.v1 import html


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
