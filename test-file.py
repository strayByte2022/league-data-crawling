import requests


api_keys = "RGAPI-9d4ba430-98df-48ca-b249-f7958883df94"
#please notice that '&api_key'
requests_url = "https://sea.api.riotgames.com/lol/match/v5/matches/by-puuid/TEYgEV3A6HxegeRhjEtmu6jn0jFC3_dFnKz" \
               "-yY3PGfFj3Hru5cKdDuTEgUoL9iSzrj56vlO2hz27iA/ids?start=0&count=20"+'&api_key='+api_keys
status = requests.get(requests_url)
match_list = status.json()
count = 0
uuid = 'TEYgEV3A6HxegeRhjEtmu6jn0jFC3_dFnKz-yY3PGfFj3Hru5cKdDuTEgUoL9iSzrj56vlO2hz27iA'

latest_match_url = "https://sea.api.riotgames.com/lol/match/v5/matches/"+match_list[0]+'?api_key='+api_keys
match_info = requests.get(latest_match_url).json()
attributes = match_info['info']['participants'][0]['win']
print(attributes)