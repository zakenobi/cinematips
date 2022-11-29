import streamlit as st
from package.imdbrequest import ImdbRequest
from PIL import Image
import requests
from io import BytesIO
import streamlit.components.v1 as components
import os
import re

code = """<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-37VMDHT2D6"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-37VMDHT2D6');
</script>"""

a=os.path.dirname(st.__file__)+'/static/index.html'
with open(a, 'r') as f:
    data=f.read()
    if len(re.findall('UA-', data))==0:
        with open(a, 'w') as ff:
            newdata=re.sub('<head>','<head>'+code,data)
            ff.write(newdata)

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