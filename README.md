[![Website cinematips.streamlit.app](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](http://cinematips.streamlit.app) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![GitHub license](https://img.shields.io/github/license/zakenobi/cinematips)](https://github.com/zakenobi/cinematips/blob/main/LICENSE) [![Flake8 Status](./reports/flake8/flake8-badge.svg)](./reports/flake8/index.html)


# ✨ Cinematips ✨
Alexandra Mille-Egea
Zachary Gagnou
## Intro
This project is a website that uses IMDB API for getting a movies rating. The project establish's it-self in two classes, **API and web scapping**, and **Digital Traces**. It has bein authored by Alexandra Mille-Egea and Zachary Gagnou.
## How it works
Using the web app is very simple, as you get on the home pages you are derectly greated by a search bar where you enter the name of the movie you wish to know the score and it will show you all the best results.

## Where to find it
The web app is hosted by streamlit app at: https://cinematips.streamlit.app/

But if you are fealing adventurous you can run the docker version. First get the docker file from docker hub:

```console
foo@bar:~$ sudo docker pull zakenobi/cinematips
```

Now you can run the image:

```console
foo@bar:~$ sudo docker run -p 8501:8501 zakenobi/cinematips
```
You can now access the app at http://localhost:8501. (You can also run the image with the -d flag to keep it running) Sorry Mac and Windows users you're on your own for this one.
## CI

GitHub Actions for python syntax error and proper habits with flake8. There is also code run test but their are no other unit testing.

## CD

Automatic with streamlit hub that checks the github repo for changes. The way they manage to do that is thanks to [Watchtower](https://containrrr.dev/watchtower/), We recomend that you check it out it's very cool!

In addition their is an automatic build and publishing of the docker image for the app to [Docker hub](https://hub.docker.com/repository/docker/zakenobi/cinematips).

## Google Analytics
This web site is using google analytics for educational purpose only monitoring the traffic.

## Improvments
Usage of streamlit is nice and easy to get a fast modern result but it is very heavy and slow. A nice improvment would be to use a more optimized frontend framwork such as React and having the python code served by a lightweight server like Django.
