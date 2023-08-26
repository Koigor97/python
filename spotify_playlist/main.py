from get_songs_data import ScrapData


scrap_data = ScrapData()

year_query = input("Which year would like to search for (YY-MM-DD): ")
scrap_data.set_year_of_search(year_query)
data = scrap_data.the_data_recieve()[3:-11]
# print(len(data))
# for song in data:
#     print(song)

# while not year_query.isalpha():
#     print(year_query.isalpha())
#     year_query = input("Which year would like to search for (YY-MM-DD): ")