
# Loosers home data is not provided. so we need to do a conversion to have that data
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
