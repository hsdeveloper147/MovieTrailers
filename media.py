import webbrowser


class Movie():
    '''This Class is used to store each movie's data in a structured
       way i.e, this class is the representation or blueprint of the
       instances that can be instantiated out of it. To instantiate
       an object of this class in a sepearte file write following code:
           new_object = media.Movie(movie_title, movie_storyline,
                                    poster_image,trailer_youtube, ratings)
       where parameters are the supplied arguments related the
       particular movie
    '''
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, ratings):
        '''init function is used to instantiate an object with the seperate
        memory space
        '''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.ratings = ratings

    def show_trailer(self):
        '''show_tralier(self) is an instance method that is used to play
        the trailer of a movie in a web browser
        '''
        webbrowser.open(self.trailer_youtube_url)
