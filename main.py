import requests
import datetime

global_id = ''


def get_player_info(user_name, api_key,region_code):
    user_name = user_name.replace(' ','%20')
    region_code = region_code.lower()
    request_url = 'https://'+region_code+'.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + user_name + '?api_key=' + api_key
    status = requests.get(request_url)  # this is for debugging
    if status.status_code == 404:
        return {'Status:':'Summoner not found'}
    elif status.status_code == 401:
        return {'Status':'API key is invalid'}
    else:
        info = status.json()
        global global_id
        # global_id = info['puuid']
        return info


# def get_player_match_info(user_name,api_key):
def get_match_list(id, api_key, num):
    requests_url = 'https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/' + id + '/ids?start=0&count=' + str(
        num) + '&api_key=' + \
                   api_key
    status = requests.get(requests_url)

    match_list = status.json()
    return match_list


def get_match_info_by_id(match_id, uuid, api_key):
    requests_url = 'https://asia.api.riotgames.com/lol/match/v5/matches/' + match_id + '?api_key=' + api_key
    status = requests.get(requests_url)

    match_info = status.json()

    my_index = match_info['metadata']['participants'].index(uuid)
    # trivial info
    timeStamp1 = match_info['info']['gameCreation']
    # FIXME: convert unix time into readable form
    timeStamp1 = datetime.datetime.fromtimestamp(timeStamp1 / 1000)
    timeStamp1 = timeStamp1.strftime('%Y-%m-%d %H:%M:%S')
    timeStamp2 = match_info['info']['gameDuration']
    timeStamp2 = round(timeStamp2 / 60, 0)
    mode = match_info['info']['gameMode']
    version = match_info['info']['gameVersion']
    print('Time: ', timeStamp1)
    print('Duration: ', timeStamp2, ' mins')
    print('Game mode: ' + mode)
    print('Version: ' + version)
    # role
    role = match_info['info']['participants'][my_index]['role']
    print('Role: ', role)
    champ = match_info['info']['participants'][my_index]['championName']
    print('Champion played: ', champ)
    # kda
    kills = match_info['info']['participants'][my_index]['kills']
    assists = match_info['info']['participants'][my_index]['assists']
    deaths = match_info['info']['participants'][my_index]['deaths']
    if deaths != 0:
        kda = (kills + assists) / deaths
    else:
        kda = 'Perfect KDA!'
    print('Kills: ' + str(kills))
    print('Deaths: ' + str(deaths))
    print('Assists: ' + str(assists))

    if type(kda) == str:
        print(kda)
    else:
        print('KDA: ' + str(round(kda, 2)))

    # damage dealt
    damage_dealt = match_info['info']['participants'][my_index]['totalDamageDealt']
    print('Damage Dealt:' + str(damage_dealt))
    # damage taken
    damage_taken = match_info['info']['participants'][my_index]['totalDamageTaken']
    print('Damage Taken: ', damage_taken)
    # cc
    time_cc = match_info['info']['participants'][my_index]['timeCCingOthers']
    print('CC time on others: ', time_cc)
    # minions
    creep = match_info['info']['participants'][my_index]['totalMinionsKilled']
    print('Total minions killed: ', creep)
    # gold
    gold_earned = match_info['info']['participants'][my_index]['goldEarned']
    gold_spent = match_info['info']['participants'][my_index]['goldSpent']
    print('Gold Earned:', gold_earned)
    print('Gold Spent: ', gold_spent)

    # vision score
    visionScore = match_info['info']['participants'][my_index]['visionScore']

    print('Vision score: ' + str(visionScore))

    # wins
    wins = match_info['info']['participants'][my_index]['win']

    if wins:
        print("Player Won\n")
    else:
        print("Player Lost\n")


if __name__ == "__main__":
    key = 'RGAPI-c2e73f9c-7723-46df-85dd-ba66186b4218'  # api key expired after 2 days!

    get_player_info('Hide on bush', key)
    # print(get_match_list(global_id,key))
    # get_match_info_by_id('KR_6571202211', global_id, key)

    # 20 matches
    for i in get_match_list(global_id, key, 30):
        get_match_info_by_id(i, global_id, key)
