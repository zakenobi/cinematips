from pytrends.request import TrendReq
import streamlit as st
import pandas as pd

# Impletment a decorator that logs the execution time of a function
def log_time(func):
    import time
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print(f"Function {func.__name__} took {t2-t1} seconds")
        st.markdown(f"Function {func.__name__} took {t2-t1} seconds")
        return result
    return wrapper

# function that loads a text file and counts the number of appearances of a word in the text
@log_time
def load_text():
    # Load the text file
    with open("./Shakespear", "r") as f:
        text = f.read()

    # Count the number of appearances of each word in the text and store it in a dictionary
    word_count = {}
    for word in text.split():
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Convert the dictionary to a pandas dataframe
    df = pd.DataFrame.from_dict(word_count, orient='index', columns=['count'])
    df = df.sort_values(by='count', ascending=False)

    st.title("Word count of Shakespear's Hamlet")
    # Plot the top 10 words in a bar chart using streamlit
    st.bar_chart(df.head(10))




# Decorate the main function with the log_time decorator
@log_time
def main():
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



main()
load_text()