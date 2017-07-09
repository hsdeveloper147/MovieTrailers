# -*- coding: utf-8 -*-
"""
Created on Sat Jul 08 23:21:45 2017

@author: sundr
"""
import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                            "A story of a boy and his toys that come to life",
                            "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                            "https://www.youtube.com/watch?v=tN1A2mVnrOM")
#print(toy_story.storyline)
#webbrowser.open(toy_story.trailer_youtube_url)

avatar = media.Movie("Avatar",
                    "A marine on an alien planet",
                    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=cRdxXPV9GNQ"
                    )

#print(avatar.trailer_youtube_url)
#avatar.show_trailer()

avatar1 = media.Movie("Avatar",
                    "A marine on an alien planet",
                    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=cRdxXPV9GNQ"
                    )

avatar2 = media.Movie("Avatar",
                    "A marine on an alien planet",
                    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=cRdxXPV9GNQ"
                    )

avatar3 = media.Movie("Avatar",
                    "A marine on an alien planet",
                    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=cRdxXPV9GNQ"
                    )

avatar4 = media.Movie("Avatar",
                    "A marine on an alien planet",
                    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=cRdxXPV9GNQ"
                    )

movies = [toy_story, avatar, avatar1, avatar2, avatar3, avatar4]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)