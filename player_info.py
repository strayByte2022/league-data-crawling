# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
api_keys = "RGAPI-9d4ba430-98df-48ca-b249-f7958883df94"
url_api = "https://vn2.api.riotgames.com/lol/summoner/v4/summoners/by-name/TinChuanChuaAnh"+'?api_key='+api_keys

status = requests.get(url_api)
player_info = status.json()


print(status)
print(player_info)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
