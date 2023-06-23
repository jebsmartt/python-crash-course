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

# print(make_album('Queen', 'Greatest Hits', 24))
# print(make_album('Earth Wind and Fire', 'September'))
# print(make_album('My Chemical Romance','Welcome to the Black Parade'))

input_flag = True

while input_flag == True:
    f_artist = f"Who is your favorite artist? "
    f_album = f"Which album of theirs is your favorite? "
    
    f_artist = input(f_artist)
    f_album = input(f_album)

    print(make_album(artist_name=f_artist,album_title=f_album))
    ask_again = input(f"Do you have another favorite artist? (Y / N) ")

    if ask_again != 'Y':
        input_flag = False

