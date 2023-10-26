#%%
import pandas as pd
import matplotlib.pyplot as plt
import requests
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder

def one_dict(list_dict):
    keys=list_dict[0].keys()
    out_dict={key:[] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict

dict_={'a':[11,21,31],'b':[12,22,32]}
df = pd.DataFrame(dict_)
print(df.head(), df.mean(), sep="\n")

nba_teams = teams.get_teams()
dict_nba_team = one_dict(nba_teams)
df_teams = pd.DataFrame(dict_nba_team)
df_warriors = df_teams[df_teams['nickname']=='Warriors']
df_warriors
id_warriors = df_warriors[['id']].values[0][0]
gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)
gamefinder.get_json()

filename = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl"

def download(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)

golden_state = "Golden_State.pkl"
download(filename, golden_state)
games = pd.read_pickle(golden_state)
games.head()
games_home=games[games['MATCHUP']=='GSW vs. TOR']
games_away=games[games['MATCHUP']=='GSW @ TOR']
fig, ax = plt.subplots()

games_away.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
games_home.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
ax.legend(["away", "home"])
# plt.show()

url_post = 'http://httpbin.org/post'
payload={"name":"Joseph","ID":"123"}
r_post = requests.post(url_post,data=payload)
#%%