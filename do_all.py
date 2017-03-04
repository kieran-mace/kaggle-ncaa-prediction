# Import stuff
import pandas as pd
import numpy as np

# Function Definitions

# Scores
def get_logloss(guess, actual):
    logloss = -np.mean(actual * np.log(guess)) + (1.0 - actual) * np.log((1.0 - guess))
    return logloss

def score_predictions(truth, predicitons):
    scores = list()
    for i in range(0,len(truth)-1)
        scores[i] = get_logloss[predicitons[i], truth[i]]
    return np.mean(scores)

# Predictions
def make_prediction(input):
    # Currently just going to return a random Number
    Season, team1, team2 = input.split('_')
    team1_data = Summary.loc[int(Season)].loc[int(team1)]
    team2_data = Summary.loc[int(Season)].loc[int(team2)]
    ratio = team1_data / team2_data
    return np.log2(ratio['outcome']) + 0.5
    #return np.random.random() # random number between 0 and 1


def apply_prediction(dataframe):
    dataframe['pred'] = dataframe['id'].apply(lambda x: make_prediction(x))
    sample_submission.to_csv('test.csv',index=False)
    return(dataframe)

# Load data

RegularSeasonCompactResults = pd.read_csv("data/RegularSeasonCompactResults.csv")
RegularSeasonDetailedResults = pd.read_csv("data/RegularSeasonDetailedResults.csv")
sample_submission = pd.read_csv("data/sample_submission.csv")
Seasons = pd.read_csv("data/Seasons.csv")
Teams = pd.read_csv("data/Teams.csv")
TourneyCompactResults = pd.read_csv("data/TourneyCompactResults.csv")
TourneyDetailedResults = pd.read_csv("data/TourneyDetailedResults.csv")
TourneySeeds = pd.read_csv("data/TourneySeeds.csv")
TourneySlots = pd.read_csv("data/TourneySlots.csv")

# Format data

convert = {}
convert['N'] = 'N' # Neutral to Neutral
convert['H'] = 'A' # Home to away
convert['A'] = 'H' # Away to home
Lloc = [convert[x] for x in RegularSeasonDetailedResults['Wloc']]

RegularSeasonDetailedResults['Lloc'] = Lloc

Winner_data = RegularSeasonDetailedResults[['Season',
                                           'Daynum',
                                           'Wteam',
                                           'Wscore',
                                           'Wloc',
                                           'Numot',
                                           'Wfgm',
                                           'Wfga',
                                           'Wfgm3',
                                           'Wfga3',
                                           'Wftm',
                                           'Wfta',
                                           'Wor',
                                           'Wdr',
                                           'Wast',
                                           'Wto',
                                           'Wstl',
                                           'Wblk',
                                           'Wpf']]

Looser_data = RegularSeasonDetailedResults[['Season',
                                           'Daynum',
                                           'Lteam',
                                           'Lscore',
                                           'Lloc',
                                           'Numot',
                                           'Lfgm',
                                           'Lfga',
                                           'Lfgm3',
                                           'Lfga3',
                                           'Lftm',
                                           'Lfta',
                                           'Lor',
                                           'Ldr',
                                           'Last',
                                           'Lto',
                                           'Lstl',
                                           'Lblk',
                                           'Lpf']]

columns=['Season',
         'Daynum',
         'team_number',
         'score',
         'location',
         'Number_OT',
         'field_goals_made',
         'field_goals_attempted',
         'three_pointers_made',
         'three_pointers_attempted',
         'free_throws_made',
         'free_throws_attempted',
         'offensive_rebounds',
         'defensive_rebounds',
         'assists',
         'turnovers',
         'steals',
         'blocks',
         'personal_fowls']

Winner_data.columns = columns
Winner_data['outcome'] = 1
Looser_data.columns = columns
Looser_data['outcome'] = 0

All = Winner_data
All = All.append(Looser_data)
del All['Daynum'] # I cant see how this is going to be helpful, unless we want
# to see if a team is "getting hot" closer to the end of the season.
Summary = All.groupby(['Season', 'team_number']).mean()
