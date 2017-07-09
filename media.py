# -*- coding: utf-8 -*-
"""
Created on Sat Jul 08 23:14:02 2017

@author: sundr
"""
import webbrowser
class Movie():
    '''Movie Class to store each movie's data 
    '''
    def __init__(self,movie_title, movie_storyline, poster_image, 
                 trailer_youtube,ratings):
        self.title = movie_title
        self.storyline= movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.ratings = ratings
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        