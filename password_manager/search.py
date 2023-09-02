import json
from tkinter import messagebox

def if_file_not_found():
    return messagebox.showinfo(title="File Not Found❗️",
                               message="Oops.. There's no such Storage file ")

def if_entry_not_found(website):
    return messagebox.showinfo(title=f"{website} Not Found❗️",
                               message="Oops.. The entry you search for is not in the Saved Passwords ")


class SearchInfo:
    def __init__(self):
        self.website = ''

    def set_website(self, search_entry):
        print(search_entry)
        self.website = search_entry


    def __get_search_entry(self):
        return  self.website


    def look_up_search(self):
        clear_entry_field = False
        try:
            with open("storage.json", "r") as file:
                content = json.load(file)
        except FileNotFoundError:
            if_file_not_found()
        else:
            if self.__get_search_entry() in content:
                messagebox.showinfo(title=self.__get_search_entry().title(),
                          message=f"Username/Email: {content[self.__get_search_entry()].user_login}\n"
                                  f"Password: {content[self.__get_search_entry()].user_passwd}")
                clear_entry_field = True
            else:
                if_entry_not_found(website=self.__get_search_entry().title())
        finally:
            return clear_entry_field