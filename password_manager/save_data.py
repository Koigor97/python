from tkinter import messagebox
# This class saves the data received from the user

def question_warning_message():
    messagebox.showwarning(title="Empty Input-field", message="You have an empty entry-field.")




class SaveData:

    def __init__(self):
        self.__website = ""
        self.__user_login = ""
        self.__password = ""


    def set_info(self, website, login, passwd):
        self.__website = website
        self.__user_login = login
        self.__password = passwd


    def __get_website(self):
        return self.__website.get()


    def __get_user_login(self):
        return self.__user_login.get()


    def __get_passwd(self):
        return self.__password.get()


    def __is_entry_field_empty(self):
        status = False
        if (self.__get_website() == "") or (self.__get_user_login() == "") or (self.__get_passwd() == ""):
            question_warning_message()
        else:
            status = True

        return status


    def __confirm_to_save(self):
        return messagebox.askokcancel(
            title="Confirm Info", message=f"You entered the following:\n"
            f"Website: {self.__get_website()}\nUser-address: {self.__get_user_login()}\n"
            f"Password: {self.__get_passwd()}\nProceed to SAVE? ")


    def save_passwd(self):
        if self.__is_entry_field_empty():
            if self.__confirm_to_save():
                with open("data.txt", "a") as file:
                    file.write(f"{self.__get_website()} | {self.__get_user_login()} | {self.__get_passwd()}\n")
                return True
            else:
                return False