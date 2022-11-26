import streamlit as st
from package.imdbrequest import ImdbRequest
from PIL import Image
import requests
from io import BytesIO

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

movies = ImdbRequest.get_movies(search=title)

movies.sort(key=lambda x: x.ratingRottenTomatoes, reverse=True)

for movie in movies:
    print(f"{movie.ratingRottenTomatoes} : {movie.title}")

for movie in movies:
    st.caption(movie.title)
    st.code(movie.ratingRottenTomatoes)

    response = requests.get(movie.image)
    img = Image.open(BytesIO(response.content))
    st.image(img, caption='Sunrise by the mountains')