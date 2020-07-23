class Song:
    """Class to represent a song
    Attributes:
        title (str): the title of the song
        artist (Artist): an artist object representing the song's creator
        duration (int): duration of song in seconds, can be 0
        """

    def __init__(self, title, artist, duration=0):
        """ Song init method

        Args:
        title (str): initializes title attribute
        artist (Artist): song's creator
        duration (optional[int]): initial value for duration attribute
            will default to zero if unspecified
        """
        self.title = title
        self.artist = artist
        self.duration = duration

class Album:
    """ class to represent an album using its track list

    Attributes:
    album_name (str): cheese
    year (int): dad
    artist: (artist): mom
    """

    def __init__(self, name, year, artist = None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else: 
            self.artist = artist
        
        self.tracks = []

    def add_song(self, song, position=None):
        
        if position is None:
           self.tracks.append(song)
        else: 
            self.tracks.insert(position, song)

help(Album)
    
