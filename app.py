import streamlit as st
from package.imdbrequest import ImdbRequest

movies = ImdbRequest.get_movies(search="Star Wars")

movies.sort(key=lambda x: x.ratingRottenTomatoes, reverse=True)

for movie in movies:
    print(f"{movie.ratingRottenTomatoes} : {movie.title}")

for movie in movies:
    st.caption(movie.title)
    st.code(movie.ratingRottenTomatoes)