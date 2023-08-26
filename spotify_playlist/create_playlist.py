
import spotipy
from spotipy.oauth2 import SpotifyOAuth


class CreatePlaylist:
    def __init__(self):
        self.__client_id = "xxxxxxxx"
        self.__client_secret = "xxxxxxxx"
        self.__redirect_uri = "https://example.com"
        self.__username = "Koigor"
        self.__user_id = ""
        self.__sp = ""
        self.__list_of_song = []
        self.__user_input = ""
        self.__song_uris = []
        self.__get_test()


    def __get_test(self):
        self.__sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                scope="playlist-modify-private",
                redirect_uri=self.__redirect_uri,
                client_id=self.__client_id,
                client_secret=self.__client_secret,
                show_dialog=True,
                cache_path="token.txt",
                username=self.__username
            )
        )
        self.__user_id = self.__sp.current_user()["id"]


    def __get_user_id(self):
        return self.__user_id


    def set_user_list(self, the_input, the_list):
        self.__user_input = the_input
        self.__list_of_song += the_list



    def __get_user_input(self):
        return self.__user_input


    def __get_user_song_list(self):
        return self.__list_of_song


    def __get_song_uris(self):
        return self.__song_uris


    def search_for_songs(self):

        year = self.__get_user_input().split("-")[0]
        for song in self.__get_user_song_list():
            result = self.__sp.search(q=f"track:{song} year:{year}", type="track")
            try:
                uri = result["tracks"]["items"][0]["uri"]
                self.__song_uris.append(uri)
            except IndexError:
                print(f"{song} doesn't exist in Spotify. Skipped.")


    def create_playlist(self):
        playlist = self.__sp.user_playlist_create(user=self.__get_user_id(),
                                                  name=f"{self.__get_user_input().split('-')[0]} Billboard 100",
                                                  public=False)
        self.__sp.playlist_add_items(playlist_id=playlist["id"], items=self.__get_song_uris())