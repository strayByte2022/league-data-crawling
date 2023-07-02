import requests


def get_player_info(user_name, api_key):
    request_url = 'https://vn2.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+user_name+'?api_key='+api_key
    info = requests.get(request_url).json()
    print(info)
#def get_player_match_info(user_name,api_key):


if __name__ == "__main__":
    key = 'RGAPI-9d4ba430-98df-48ca-b249-f7958883df94'
    get_player_info('TinChuanChuaAnh',key)
