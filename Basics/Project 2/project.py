"""The project is a music data analysis tool that loads a set of music data and provides functionality to filter and
analyze the data. The data is stored in a list of dictionaries, with each dictionary representing a single song and
containing fields such as the artist, title, genre, year, and duration."""


def start():
    """
    :return: operation list that represent the functionality of this project and manipulate them
    """
    operations = {
        1: "Load Playlist",
        2: "View Playlist",
        3: "Search Playlist",
        4: "Analyze Playlist",
        5: "Exit"
    }
    print("__________________operation list______________________")
    for operation in operations.items():
        print(f"{operation[0]}) {operation[1]}")
    #         validation for operation inputs
    try:
        operation_number = int(input("Select operation number from the list: "))
        if operation_number < 1 or operation_number > 5:
            print("Invalid input: please select a number from the list")
        if operation_number == 2:
            view_playlist()
        # if operation_number == 3:
        #     convert_duration()
        if operation_number == 3:
            song_gener = input("Enter song's gener: ")
            song_year = input("Enter song's year: ")
            # validation for inputs
            inputs_errors = []
            if not song_gener.isalpha():
                inputs_errors.append("Gener must letters only")
            if not song_year.isdigit():
                inputs_errors.append("Year must be only number")
            while len(inputs_errors) > 0:
                for error in inputs_errors:
                    print(error)
            else:
                for song in search_song(song_gener, song_year):
                    print(
                        f"{search_song(song_gener, song_year).index(song) + 1}) {song['title']} - {song['artist']} - {song['genre']} - {song['year']} - {song['duration']} sec")

    except ValueError:
        print("please enter a number from the list ex: 1")
        start()


def convert_duration():
    for song in song_data:
        duration_in_min = int(song["duration"] / 60)
        reminder_duration_in_sec = song["duration"] % 60
        print(f'song duration for {song["title"]} is: {duration_in_min} min, {reminder_duration_in_sec} sec')


def view_playlist():
    """
    :return: all songs in song_data
    """
    for song in song_data:
        print(
            f"{song_data.index(song) + 1}) {song['title']} - {song['artist']} - {song['genre']} - {song['year']} - {song['duration']}")


def search_song(gener, year):
    """

    :param gener: (string) the gener of song the user search about
    :param year: (int) the year of song the user search about
    :return: (list) list of songs that gener and year matches the inputs gener and years
    """
    song_list = []
    for song in song_data:
        if song["genre"] == gener and str(song["year"]) == year:
            song_list.append(song)
    return song_list


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
