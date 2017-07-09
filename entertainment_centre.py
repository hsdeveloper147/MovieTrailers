# -*- coding: utf-8 -*-
"""
Created on Sat Jul 08 23:21:45 2017

@author: sundr
"""
import fresh_tomatoes
import media
import urllib
import json

api_key = '2b75293ff31f7a9106524c6645e8fb58'
link = 'https://api.themoviedb.org/3/movie/now_playing?api_key=' + api_key + '&page=1&genre=Animation'
default_img_url = 'http://image.tmdb.org/t/p/w300/'
default_video_url = 'http://api.themoviedb.org/3/movie/'
last_part = '/videos?api_key='
default_youtube_url = 'https://www.youtube.com/watch?v='

webfile = urllib.urlopen(link)
content = webfile.read()
data = json.loads(content)

movies = []

#putting json data into movies List
for jsonData in data["results"]:
    movieData = []
    movie_id = jsonData['id']
    title = jsonData['title']
    ratings = str(jsonData['vote_average'])
    overview = jsonData['overview']
    
    #fetching youtube url
    video_url = default_video_url + str(movie_id) + last_part + api_key
    dataResponse = urllib.urlopen(video_url).read()
    jsonResponse = json.loads(dataResponse)
    key = jsonResponse['results'][0]['key']
    if(len(key) <=2):
        continue
    trailer_url = default_youtube_url + key
    
    #fetching image url
    img_url = default_img_url + jsonData['poster_path']
    
    #intantiating Moive class Object
    movie = media.Movie(title,overview,img_url,trailer_url,ratings)
    movies.append(movie)
    

fresh_tomatoes.open_movies_page(movies)
