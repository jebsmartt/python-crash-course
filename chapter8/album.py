def make_album(artist_name,album_title,number_songs=None):
    if number_songs:
        
        album = {
            'artist_name' : artist_name,
            'album_title' : album_title,
            'number_of_songs': number_songs, 
        } 
    else:
       album = {
            'artist_name' : artist_name,
            'album_title' : album_title, 
        }
    return album

print(make_album('Queen', 'Greatest Hits', 24))
print(make_album('Earth Wind and Fire', 'September'))
print(make_album('My Chemical Romance','Welcome to the Black Parade'))
