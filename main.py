from pprint import pprint
import requests
import json

TOKEN = 2619421814940190
hero_list = ['Hulk', 'Captain America', 'Thanos']
def get_id(heros):
    # params =
    # headers =
    # response = requests.get(url)
    # pprint(response.status_code)
    id_list = []
    for hero in hero_list:
        url = f'https://superheroapi.com/api/{TOKEN}/search/{hero}'
        response = requests.get(url)
        id_list.append(response.json()['results'][0]['id'])
    return  id_list

def _get_hero_dict_():
    i = []
    for id in get_id(hero_list):
        url = f'https://superheroapi.com/api/{TOKEN}/{id}/powerstats'
        response = requests.get(url)
        i.append(response.json()['intelligence'])
    hero_dict = dict(zip(hero_list, i))
    return hero_dict

def get_top_1_intelligence():
    hero_dict = _get_hero_dict_()
    inte = 0
    valu = 0
    name = ''
    for key, value in hero_dict.items():
        valu = int(value)
        if int(inte) < valu:
            inte = value
            name = key
        else:
            pass
    result = print(f'В самый умный с Тиной Канделаки победил {name} с результатом {inte}')
    return result



get_top_1_intelligence()





