from tkinter import messagebox
import json
# This class saves the data received from the user

def question_warning_message():
    messagebox.showwarning(title="Empty Input-field", message="You have an empty entry-field.")


def verify_and_save(website, user_info, passwd):
    info_to_save = {website.lower(): {"user_login":user_info, "user_passwd":passwd}}

    try:
        with open("storage.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        with open("storage.json", "w") as file:
            json.dump(info_to_save, file, indent=4)

    else:
        data.update(info_to_save)
        with open("storage.json", "w") as file:
            json.dump(data, file, indent=4)


class SaveData:

    def __init__(self):
        self.website = ""
        self.user_login = ""
        self.password = ""


    def set_info(self, website, login, passwd):
        self.website = website
        self.user_login = login
        self.password = passwd


    def __get_website(self):
        return self.website.get()


    def __get_user_login(self):
        return self.user_login.get()


    def __get_passwd(self):
        return self.password.get()


    def __is_entry_field_empty(self):
        status = False
        if (self.__get_website() == "") or (self.__get_user_login() == "") or (self.__get_passwd() == ""):
            question_warning_message()
        else:
            status = True

        return status


    def save_passwd(self):
        if self.__is_entry_field_empty():
            verify_and_save(website=self.__get_website(), user_info=self.__get_user_login(), passwd=self.__get_passwd())
            return True
        else:
            return False