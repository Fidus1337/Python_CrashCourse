"""
Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
Use None to add an optional parameter to make_album() that allows you to
store the number of songs on an album. If the calling line includes a value for
the number of songs, add that value to the album’s dictionary. Make at least
one new function call that includes the number of songs on an album.
"""


def make_album(artist_name: str, title_name: str, number_of_songs: int = None):
    """Function for creating dictionary about album"""
    return {'artist': artist_name, 'title': title_name, 'songs': number_of_songs}


print(make_album('Queen', 'Bohemian Rhapsody', 14))
print(make_album('Kino', 'Unkown album', 6))
print(make_album('Kiss', 'I cannot to explain', 23))
