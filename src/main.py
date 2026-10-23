import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/nba_kaggle/Games.csv")

first_year_of_experiment = df.loc[(df['gameDate'] >= "2000-10-31")] 
every_year_of_experiment = first_year_of_experiment.loc[(df['gameDate'] <= "2015-04-16")] 

# every_year_of_experiment.to_csv("data/clean/v_0_1.csv", index=True)

def manipulate_year(year):
    year = str(year)
    return year[-2:]

def get_nba_season(x):
    date = x.split(' ')[0]
    year, month, day = date.split('-')
    
    if int(month) < 6:
        return f'{int(year)-1}-{manipulate_year(year)}'
    
    if int(month) > 8:
        return f'{year}-{manipulate_year(int(year)+1)}'

every_year_of_experiment['year'] = every_year_of_experiment['gameDateTimeEst']
every_year_of_experiment['year'] = every_year_of_experiment['year'].apply(get_nba_season)

## cleaning up the data 

removable_gameType = ['Playoffs','Preseason']
every_year_of_experiment = every_year_of_experiment[every_year_of_experiment.gameType.isin(removable_gameType) == False]
# every_year_of_experiment.to_csv("data/clean/v_0_2.csv", index=True)
# print(">?>?>",len(every_year_of_experiment))

# getting relevant columns
final_df = every_year_of_experiment[['hometeamId','awayteamId','winner','year']]
# final_df.to_csv("data/clean/v_0_3.csv", index=True)