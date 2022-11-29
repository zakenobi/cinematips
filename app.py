import streamlit as st
from package.imdbrequest import ImdbRequest
from PIL import Image
import requests
from io import BytesIO
import streamlit.components.v1 as components

components.html("""
 <!-- Google tag (gtag.js) -->
<script async
src="https://www.googletagmanager.com/gtag/js?id=G-MHZRLJ3W6W"></script>
<script>
 window.dataLayer = window.dataLayer || [];
 function gtag(){dataLayer.push(arguments);}
 gtag('js', new Date());
 gtag('config', 'G-MHZRLJ3W6W');
</script>""", width=0, height=0)

title = st.text_input('Movie title')
st.write('The current movie title is', title)

movies = ImdbRequest.get_movies(search=title)

movies.sort(key=lambda x: x.ratingRottenTomatoes, reverse=True)

for movie in movies:
    st.header(movie.title)
    st.code(movie.ratingRottenTomatoes)

    response = requests.get(movie.image)
    img = Image.open(BytesIO(response.content))
    st.image(img)