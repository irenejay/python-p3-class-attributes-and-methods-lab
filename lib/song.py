class Song:
    count = 0  # Class attribute to keep track of the number of new songs
    genres = []  # Class attribute to store unique genres
    artists = []  # Class attribute to store unique artists
    genre_count = {}  # Class attribute to store genre count
    artist_count = {}  # Class attribute to store artist count

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artist_count(cls, artist):
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1

    def __init__(self, title, artist, genre):
        self.title = title
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

# Example usage:
song1 = Song("Shape of You", "Ed Sheeran", "Pop")
song2 = Song("Bohemian Rhapsody", "Queen", "Rock")
song3 = Song("Old Town Road", "Lil Nas X", "Country")
song4 = Song("Lose Yourself", "Eminem", "Rap")
song5 = Song("Rolling in the Deep", "Adele", "Pop")

print("Total number of songs:", Song.count)
print("Genres:", Song.genres)
print("Artists:", Song.artists)
print("Genre count:", Song.genre_count)
print("Artist count:", Song.artist_count)
