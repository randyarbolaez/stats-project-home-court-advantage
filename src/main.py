import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/nba_kaggle/Games.csv")

first_year_of_experiment = df.loc[(df['gameDate'] >= "2000-10-31")] 
# every_year_of_experiment = first_year_of_experiment.loc[(df['gameDate'] <= "2001-04-19")] 
every_year_of_experiment = first_year_of_experiment.loc[(df['gameDate'] <= "2015-04-16")] 


def manipulate_year(year):
    # if type(year) == int:
    year = str(year)

    return year[-2:]

def get_nba_season(x):
    date = x.split(' ')[0]
    year, month, day = date.split('-')
    
    if int(month) < 6:
        return f'{int(year)-1}-{manipulate_year(year)}'
    
    if int(month) > 8:
        return f'{year}-{manipulate_year(int(year)+1)}'

# every_year_of_experiment["date"] = blah[0]
every_year_of_experiment['year'] = every_year_of_experiment['gameDateTimeEst']
every_year_of_experiment['year'] = every_year_of_experiment['year'].apply(get_nba_season)
print(every_year_of_experiment)

# print(every_year_of_experiment)

# print(every_year_of_experiment)

hometeamwinner = (every_year_of_experiment['hometeamId'] == every_year_of_experiment['winner']).sum()

sns.barplot(every_year_of_experiment, x=hometeamwinner, y="year", orient="y")
plt.show()

# print(hometeamwinner)