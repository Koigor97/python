from get_songs_data import ScrapData
from create_playlist import CreatePlaylist


scrap_data = ScrapData()
create_playlist = CreatePlaylist()


year_query = input("Which year would like to search for (YY-MM-DD): ")
scrap_data.set_year_of_search(year_query)
data = scrap_data.the_data_recieve()[3:-11]
create_playlist.set_user_list(the_input=year_query, the_list=data)
create_playlist.search_for_songs()
# print(len(data))
# for song in data:
#     print(song)

# while not year_query.isalpha():
#     print(year_query.isalpha())
#     year_query = input("Which year would like to search for (YY-MM-DD): ")

