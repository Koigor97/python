import random


class RandomPassword:
    def __init__(self):
        self.__letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
        't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
        'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.__numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.__symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    def get_passwd(self):
        password = [random.choice(self.__letters) for _ in range(4)]
        password += [random.choice(self.__numbers) for _ in range(3)]
        password += [random.choice(self.__symbols) for _ in range(4)]

        random.shuffle(password)
        finish_passwd =  "".join(password)
        return finish_passwd