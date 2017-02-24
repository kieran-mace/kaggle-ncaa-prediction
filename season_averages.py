
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
         'team',
         'score',
         'loc',
         'Numot',
         'fgm',
         'fga',
         'fgm3',
         'fga3',
         'ftm',
         'fta',
         'or',
         'dr',
         'ast',
         'to',
         'stl',
         'blk',
         'pf']

Winner_data.columns = columns
Winner_data['outcome'] = 1
Looser_data.columns = columns
Looser_data['outcome'] = 0

All = Winner_data
All = All.append(Looser_data)

Summary = All.groupby(['Season', 'team']).mean()
