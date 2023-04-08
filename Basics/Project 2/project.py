"""The project is a music data analysis tool that loads a set of music data and provides functionality to filter and
analyze the data. The data is stored in a list of dictionaries, with each dictionary representing a single song and
containing fields such as the artist, title, genre, year, and duration."""


def start():
    """
    :return: operation list that represent the functionality of this project and manipulate them
    """
    operations = {
        1: "View Playlist",
        2: "Search Playlist",
        3: "Analyze Playlist",
        4: "Exit"
    }
    print("__________________operation list______________________")
    for operation in operations.items():
        print(f"{operation[0]}) {operation[1]}")
    #         validation for operation inputs
    try:
        operation_number = int(input("Select operation number from the list: "))
        if operation_number < 1 or operation_number > 5:
            print("Invalid input: please select a number from the list")
            start()
        if operation_number == 1:
            print("Playlist is: ")
            view_playlist()
            start()
        if operation_number == 2:
            search_list()
    #     if operation_number == 3:
    #         song_gener = input("Enter song's gener: ")
    #         song_year = input("Enter song's year: ")
    #         # validation for inputs
    #         inputs_errors = []
    #         if not song_gener.isalpha():
    #             inputs_errors.append("Gener must letters only")
    #         if not song_year.isdigit():
    #             inputs_errors.append("Year must be only number")
    #         while len(inputs_errors) > 0:
    #             for error in inputs_errors:
    #                 print(error)
    #         else:
    #             for song in search_song(song_gener, song_year):
    #                 print(
    #                     f"{search_song(song_gener, song_year).index(song) + 1}) {song['title']} - {song['artist']} - {song['genre']} - {song['year']} - {song['duration']} sec")
    #                 start()
    #
    except ValueError:
        print("please enter a number from the list ex: 1")
        start()


def convert_duration(song):
    duration_in_min = int(song["duration"] / 60)
    reminder_duration_in_sec = song["duration"] % 60
    return duration_in_min, reminder_duration_in_sec


def view_playlist():
    """
    :return: all songs in song_data
    """
    for song in song_data:
        print(
            f"{song_data.index(song) + 1}) {song['title']} - {song['artist']} - {song['genre']} - {song['year']} - {song['duration']}")


def search_list():
    search_about_list = {
        1: "According to specific artist",
        2: "According to genre",
        3: "According to specific year",
        4: "Go back"
    }
    for option in search_about_list.items():
        print(f"{option[0]}) {option[1]}")
    try:
        option_selected = int(input("Please Select favorite search: "))
        if option_selected < 1 or option_selected > 4:
            print("Please select number from options list")
            print("___________________________")
            search_list()
        if option_selected == 1:
            name = input("Please enter artist name: ")
            search_song_according_artist(name)
        if option_selected == 2:
            genre = input("Please enter genre: ")
            search_song_according_genre(genre)
        if option_selected == 3:
            year = input("Enter the year: ")
            search_song_according_year(year)
        if option_selected == 4:
            start()


    except ValueError:
        print("Please select number from options list")
        print("______________________________")
        search_list()


def search_song_according_artist(artist_name):
    artist_songs = []
    for artist_song in song_data:
        if artist_song["artist"] == artist_name:
            artist_songs.append(artist_song)
    for song in artist_songs:
        print(
            f"{artist_songs.index(song) + 1}) {song['title']} - {song['artist']} - {song['genre']} - {song['year']} - {convert_duration(song)[0]} min, {convert_duration(song)[1]} Sec"
        )


def search_song_according_genre(genre):
    genre_songs = []
    for genre_song in song_data:
        if genre_song["genre"] == genre:
            genre_songs.append(genre)
    for song in genre_songs:
        print(
            f"{genre_songs.index(song) + 1}) {song['title']} - {song['artist']} - {song['genre']} - {song['year']} - {convert_duration(song)[0]} min, {convert_duration(song)[1]} Sec"
        )


def search_song_according_year(year):
    year_songs = []
    for year_song in song_data:
        if str(year_song["year"]) == year:
            year_songs.append(year_song)
    for song in year_songs:
        print(
            f"{year_songs.index(song) + 1}) {song['title']} - {song['artist']} - {song['genre']} - {song['year']} - {convert_duration(song)[0]} min, {convert_duration(song)[1]} Sec"
        )


def average_duration(artist_name):
    """
    :param artist_name: artist name that we want to compute his song duration
    :return: average of artist's song
    """
    artist_songs = []
    for song in song_data:
        if song["artist"] == song_data:
            artist_songs.append(song)
        else:
            print("Artist is not in the playlist")
    summation_of_duration = 0
    for song in artist_songs:
        summation_of_duration += song["duration"]
        average = summation_of_duration / len(artist_songs)
    return average


if __name__ == '__main__':
    song_data = [
        {"title": "Bohemian Rhapsody", "artist": "Queen", "genre": "Rock", "year": 1975, "duration": 355},
        {"title": "Stairway to Heaven", "artist": "Led Zeppelin", "genre": "Rock", "year": 1971, "duration": 482},
        {"title": "Hotel California", "artist": "The Eagles", "genre": "Rock", "year": 1977, "duration": 390},
        {"title": "Back in Black", "artist": "AC/DC", "genre": "Rock", "year": 1980, "duration": 255},
        {"title": "The Chain", "artist": "Fleetwood Mac", "genre": "Rock", "year": 1977, "duration": 288},
        {"title": "Highway to Hell", "artist": "AC/DC", "genre": "Rock", "year": 1979, "duration": 208},
        {"title": "Don't Stop Believin'", "artist": "Journey", "genre": "Rock", "year": 1981, "duration": 249},
        {"title": "Smells Like Teen Spirit", "artist": "Nirvana", "genre": "Grunge", "year": 1991, "duration": 301},
        {"title": "Enter Sandman", "artist": "Metallica", "genre": "Metal", "year": 1991, "duration": 332},
        {"title": "November Rain", "artist": "Guns N' Roses", "genre": "Rock", "year": 1991, "duration": 537},

    ]
    start()
