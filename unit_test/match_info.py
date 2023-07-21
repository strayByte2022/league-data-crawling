import requests

api_keys = "RGAPI-9d4ba430-98df-48ca-b249-f7958883df94"
#please notice that '&api_key'
requests_url = "https://sea.api.riotgames.com/lol/match/v5/matches/by-puuid/TEYgEV3A6HxegeRhjEtmu6jn0jFC3_dFnKz" \
               "-yY3PGfFj3Hru5cKdDuTEgUoL9iSzrj56vlO2hz27iA/ids?start=0&count=20"+'&api_key='+api_keys
status = requests.get(requests_url)
match_list = status.json()
count = 0
countWin = 0
uuid = 'TEYgEV3A6HxegeRhjEtmu6jn0jFC3_dFnKz-yY3PGfFj3Hru5cKdDuTEgUoL9iSzrj56vlO2hz27iA' #puuid input


for i in match_list:
    print('Game '+i+':')
    latest_match_url = "https://sea.api.riotgames.com/lol/match/v5/matches/"+i+'?api_key='+api_keys
    match_info = requests.get(latest_match_url).json()
    my_index = match_info['metadata']['participants'].index(uuid)
    # trivial info
    timeStamp1 = match_info['info']['gameCreation']
    timeStamp2 = match_info['info']['gameDuration']
    mode = match_info['info']['gameMode']
    version = match_info['info']['gameVersion']
    print('Time: '+str(timeStamp1))
    print('Duration: '+str(timeStamp2))
    print('Game mode: '+mode)
    print('Version: '+version)

    #kda
    kills = match_info['info']['participants'][my_index]['kills']
    assists = match_info['info']['participants'][my_index]['assists']
    deaths = match_info['info']['participants'][my_index]['deaths']
    if deaths != 0:
        kda = (kills+assists) / deaths

    print('Kills: '+str(kills))
    print('Assists: '+str(assists))
    print('Deaths: '+str(deaths))
    print('KDA: '+str(round(kda,2)))
    # wins
    wins = match_info['info']['participants'][my_index]['win']
    if wins:
        countWin += 1
    #vision score
    visionScore = match_info['info']['participants'][my_index]['visionScore']

    print('Vision score: '+str(visionScore)+'\n')

print('\nSUMMARY!!!!')
print('Avg kda: '+str(round(count/20, 2)))

print('Win Rate: '+str(round(countWin*100/20,2)))

