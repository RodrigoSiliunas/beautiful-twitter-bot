import os
import requests
from time import sleep
from src.modules.PostMessage import PostService

if __name__ == '__main__':
    print('Twitter BOT Online! A primeira postagem será feita em um minuto.')
    sleep(60)

    url = os.environ.get('THING_URL')
    key = os.environ.get('THING_KEY')
    twitter = PostService(url, key)

    while True:
        poem = requests.get('http://beautiful-pyems.herokuapp.com/randoms').json()

        while len(poem['content']) > 220:
            poem = requests.get('http://beautiful-pyems.herokuapp.com/randoms').json()

        twitter.post_message(
            f'Título: { poem["title"] };\nAutor: { poem["author"] };\n\n{ poem["content"] }'
        )
        print("Mensagem postada!")

        sleep(60 * 60 * 3)
