import requests
from bs4 import BeautifulSoup


class ScrapData:
    def __init__(self):
        self.__year_of_search = ""
        self.__url_endpoint = "https://www.billboard.com/charts/hot-100/"


    def set_year_of_search(self, query):
        self.__year_of_search = query


    def __get_year_of_search(self):
        return self.__year_of_search

    def __get_raw_data(self):
        response = requests.get(f"{self.__url_endpoint}{self.__get_year_of_search()}")
        response.raise_for_status()
        billboard_top_100 = response.text
        soup = BeautifulSoup(billboard_top_100, "html.parser")
        return soup


    def __clean_data_to_list(self):
        refine_soup = self.__get_raw_data().findAll(name="h3", id="title-of-a-story")
        rough_song_list = [song.getText().strip() for song in refine_soup]
        list_of_songs = [song for song in rough_song_list if all(char not in song for char in ['/', '\\', '(s)', ':'])]
        return list_of_songs

    def the_data_recieve(self):
        return self.__clean_data_to_list()
