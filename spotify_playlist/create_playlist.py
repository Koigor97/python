
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
        self.__get_test()


    def __get_test(self):
        sp = spotipy.Spotify(
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
        self.__user_id = sp.current_user()["id"]


    def __get_user_id(self):
        return self.__user_id


    def set_user_list(self, the_input, the_list):
        self.__user_input = the_input
        self.__list_of_song.append(all(the_list))
        print(self.__list_of_song)


    def __get_user_input(self):
        return self.__user_input


    def __get_user_song_list(self):
        return self.__list_of_song

    def search_for_songs(self):
        song_uris = []

        year = self.__get_user_input().split("-")[0]
        for song in self.__get_user_song_list():
            result = self.__sp.search(q=f"track:{song} year:{year}", type="track")
            print(result)
            try:
                uri = result["tracks"]["items"][0]["uri"]
                song_uris.append(uri)
            except IndexError:
                print(f"{song} doesn't exist in Spotify. Skipped.")
