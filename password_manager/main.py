from tkinter import *
from save_data import SaveData
from generate_passwd import  RandomPassword
from search import SearchInfo
import pyperclip

#############################INSTANCES/OBJECTS##########################
save_info = SaveData()
random_passwd = RandomPassword()
search_info = SearchInfo()

#############################CONFIGURATION################################
ADD_PASSWD_BTN_COLOR = "#7A9D54"
GENERATE_PASSWD_BTN_COLOR = "#557A46"
GUI_BG_COLOR = "#EEEDED"
TEXT_COLOR = "#181823"
FONT = ("Ariel", 18, "normal")
BTN_FONT = ("Ariel", 17, "bold")
DEFAULT_EMAIL = "exampleDummy@yahoo.com"

##################################THE_GUI_SETUP#############################
screen = Tk()
screen.title("Password Manager 🔐")
screen.config(padx=200, pady=100, background=GUI_BG_COLOR)
canvas = Canvas(width=200, height=200, background=GUI_BG_COLOR, highlightthickness=0)
image_path = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image_path)
canvas.grid(row=0, column=1, columnspan=2)

###################################HELPER _FUNCTIONS#############################
def _add_btn_helper():
    if save_info.save_passwd():
        website_entry.delete(0, END)
        password_entry.delete(0, END)

def _generate_btn_helper():
    password_entry.delete(0, END)
    password_entry.insert(0, random_passwd.get_passwd())
    pyperclip.copy(random_passwd.get_passwd())

def _search_btn_helper():
    data = website_entry.get()
    search_info.set_website(data)

    if search_info.look_up_search():
        website_entry.delete(0, END)

#################################THE_UI_INTERFACE############################
website = Label(text="Website:", font=FONT, foreground=TEXT_COLOR, background=GUI_BG_COLOR, padx=15, pady=8)
website.grid(row=1, column=0)
website_entry = Entry(width=17, font=FONT, bg=GUI_BG_COLOR, fg=TEXT_COLOR, highlightcolor=ADD_PASSWD_BTN_COLOR)
website_entry.focus()
website_entry.grid(row=1, column=1)

email = Label(text="Email/Username:", font=FONT, foreground=TEXT_COLOR, background=GUI_BG_COLOR, padx=15, pady=8)
email.grid(row=2, column=0)
email_user_entry = Entry(width=35, font=FONT, bg=GUI_BG_COLOR, fg=TEXT_COLOR, highlightcolor=ADD_PASSWD_BTN_COLOR)
email_user_entry.insert(0, DEFAULT_EMAIL)
email_user_entry.grid(row=2, column=1, columnspan=2)

password = Label(text="Password:", font=FONT, foreground=TEXT_COLOR, background=GUI_BG_COLOR, padx=15, pady=15)
password.grid(row=3, column=0)
password_entry = Entry(width=17, font=FONT, bg=GUI_BG_COLOR, fg=TEXT_COLOR, highlightcolor=ADD_PASSWD_BTN_COLOR)
password_entry.grid(row=3, column=1)

generate_passwd_btn = Button(text="Generate Password", font=BTN_FONT, bg=GENERATE_PASSWD_BTN_COLOR,
                         command=_generate_btn_helper)
generate_passwd_btn.grid(row=3, column=2)

save_info.set_info(website_entry, email_user_entry, password_entry)

add_passwd_btn = Button(text="Add Password", font=BTN_FONT, width=32, bg=ADD_PASSWD_BTN_COLOR, command=_add_btn_helper)
add_passwd_btn.grid(row=4, column=1, columnspan=2)

search_btn = Button(text="Search Saved Info", font=BTN_FONT, bg=ADD_PASSWD_BTN_COLOR, command=_search_btn_helper)
search_btn.grid(row=1, column=2)


screen.mainloop()


