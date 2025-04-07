
#This Exercise is from chapter 8 which is functions

def make_albums(artist_name, artist_title, number_of_songs=None):

    """" Return a dictionary of Information about the album """

    name_of_artist = {'Artist Name':artist_name, 'Song Title':artist_title}

    if number_of_songs :
        name_of_artist['Number of Songs Released'] = number_of_songs

    return name_of_artist

first_album = make_albums('Dunsin Oyekan','Who is like you', 100)
print(first_album)

second_album = make_albums('Dunsin Oyekan', 'Yah', 50)
print(second_album)

third_album = make_albums('Dunsin Oyekan', 'Judah', 150)
print(third_album)