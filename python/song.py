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

        if type(artist) != type("hello"):
            print ("This is song clzss"+ "*"*80)
            
            print(artist)
            print(title)
            print ("*"*80)

        self.title = title
        self.artist = artist
        self.duration = duration
    
    def get_title(self):
        return self.title

    name = property(get_title)

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
            self.artist = "Various Artists"
        else: 
            self.artist = artist
        if type(self.artist) != type("hello"):
            print ("*"*80)
            print(type(self.artist))
            print(self.artist.name)
            print(name)
            print(year)
            print ("*"*80)
        
    
        self.tracks = []

    def add_song(self, song, position=None):
        song_found = find_object(song, self.tracks)
        if song_found is None:
            song_found = Song(song, self.artist)
        if position is None:
           self.tracks.append(song_found)
        else: 
            self.tracks.insert(position, song_found)

class Artist:
    """Basic class to store artist details.
    Attributes:
        name(str): name of artist
        albums (List[Album]): whatever
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        self.albums.append(album)
    
    def add_song(self, name, year, title):
        """add a new song to the collection of albums
        This method will add the song to an album in the collection.
        A new album will be created in the collection if it doesn't already exist.
        
        Args:
            name (str): The name of the album
            year (int): The year the album was produced
            title (str): The title of the song
            """
        album_found  = find_object(name, self.albums)
        if album_found is None:
            print(name + " not found :/")
            album_found = Album(name, year, self.name)
            self.add_album(album_found)

        else: 
            print("Found album " + name)

        album_found.add_song(title)


        

def find_object(field, object_list):
    """Check 'object list' to see if an object with a 'name' attribute equal to 'field' exists, return it if so."""
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():
    
    artist_list = []
    
    with open("albums.txt", "r") as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip("\n").split("\t"))
            year_field = int(year_field)
            print("{}: {}: {}: {}".format(artist_field, album_field, year_field, song_field))

            new_artist = find_object(artist_field, artist_list)
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)

            new_artist.add_song(album_field, year_field, song_field)

    return artist_list

def create_checkfile(artist_list):
    """create a check file from the object data for comparison with the original file"""
    with open("checkfile.txt", "w") as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song),
                    file=checkfile)

if __name__ == "__main__":
    artists = load_data()
    print("There are {} artists".format(len(artists)))

    create_checkfile(artists)