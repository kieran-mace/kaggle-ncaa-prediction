
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
import tensorflow as tf
from keras.models import Sequential



# In[66]:

df_train = pd.read_csv('games_to_train.csv')
X = df_train[['team1seed', 'team2seed', 'team1_score', 'team1_fgm', 'team1_fga',
       'team1_fgm3', 'team1_fga3', 'team1_ftm', 'team1_fta', 'team1_or',
       'team1_dr', 'team1_ast', 'team1_to', 'team1_stl', 'team1_blk',
       'team1_Wpf', 'team2_score', 'team2_fgm', 'team2_fga', 'team2_fgm3',
       'team2_fga3', 'team2_ftm', 'team2_fta', 'team2_or', 'team2_dr',
       'team2_ast', 'team2_to', 'team2_stl', 'team2_blk', 'team2_Wpf']].as_matrix()
y = df_train[['team1win']].as_matrix()


# In[67]:

X.shape


# In[68]:

model = Sequential()
from keras.layers import Dense, Activation

model.add(Dense(output_dim=64, input_dim=30))
model.add(Activation("relu"))
model.add(Dense(output_dim=1))
model.add(Activation("linear"))
model.compile(loss='mean_squared_error', optimizer='adam')
#model.compile(loss='rms', optimizer='sgd', metrics=['accuracy'])
#model.fit(X, y)
model.fit(X, y, nb_epoch=3000)


# In[29]:

df_predict = pd.read_csv('games_to_predict.csv')
X = df_predict[['team1seed', 'team2seed', 'team1_score', 'team1_fgm', 'team1_fga',
       'team1_fgm3', 'team1_fga3', 'team1_ftm', 'team1_fta', 'team1_or',
       'team1_dr', 'team1_ast', 'team1_to', 'team1_stl', 'team1_blk',
       'team1_Wpf', 'team2_score', 'team2_fgm', 'team2_fga', 'team2_fgm3',
       'team2_fga3', 'team2_ftm', 'team2_fta', 'team2_or', 'team2_dr',
       'team2_ast', 'team2_to', 'team2_stl', 'team2_blk', 'team2_Wpf']].as_matrix()
y_hat = model.predict(X)


# In[52]:

#sns.plt.plot(y_hat[:,1],y_hat[:,2])
yhat = pd.DataFrame(y_hat)

yhat.columns = ['diff', 'win']
#yhat


# In[63]:

pred = pd.read_csv('data/sample_submission.csv')
pred['pred'] = y_hat[:,1]
pred.to_csv('keras.csv',index=False)


# In[ ]:
