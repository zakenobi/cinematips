from pytrends.request import TrendReq
import streamlit as st
import pandas as pd

# make a request to google trends comparing the search terms "Boeing" and "SpaceX" in the US
pytrends = TrendReq(hl='en-US', tz=360)
kw_list = ["Boeing", "SpaceX", "NASA"]
pytrends.build_payload(kw_list, cat=0, timeframe='today 3-m', geo='US', gprop='')
df = pytrends.interest_over_time()
df = df.drop(labels=['isPartial'],axis='columns')

# Add a title to the page
st.title("Google Trends of Boeing vs SpaceX vs NASA in the US")

# Plot the data in a line chart using streamlit
st.line_chart(df)
