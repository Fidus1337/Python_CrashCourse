"""
User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop.
"""


def make_album(artist_name: str, title_name: str, number_of_songs: int = None):
    """Function for creating dictionary about album"""
    return {'artist': artist_name, 'title': title_name, 'songs': number_of_songs}


albums_list = []
poll_active = None
while (poll_active != 'Quit'):
    artist_input = input(
        'We want to create album, so input any artist: ').title()
    title_input = input('Input title of album: ').title()
    songs_input = input('Input number of songs: ')

    albums_list.append(make_album(artist_input, title_input, songs_input))
    poll_active = input(
        '\nDo you want to quit poll?(then input Quit)\n'.title())

    if poll_active.title() == 'Quit':
        poll_active = 'Quit'

    for album in albums_list:
        print(album)
