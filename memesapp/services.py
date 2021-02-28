import os
import requests


def get_memes():
    url = "https://api.imgflip.com/get_memes"

    response = requests.get(url)

    memes_data = response.json()

    allmemes = []

    for i in range(0, 5):
        allmemes.append(memes_data['data']['memes'][i])

    return allmemes