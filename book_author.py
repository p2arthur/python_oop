class User:
    def __init__(self, name, address):
        self._name = name
        self._address = address

    def get_info(self):
        return f'{self._address},{self._name}'


class Post:
    def __init__(self, text, user:User):
        self._text = text
        self._user = user


    def get_post(self):
        print(f'"{self._user.get_info()}" wrote - {self._text}')
        return



user = User('Samuel etoo', 'ding dong')

post = Post('Quis i foda', user);


post.get_post()