#!/usr/bin/env python
# coding: utf-8

# # Super Bowl Prediction
# Yiting Fu | #25169055 | 02/02/2019 | BANA 290

# ## Rams Wins

# ### Result: 
# ### Los Angeles Rams VS. New England Patriots:
# ### 29 : 27

# Unlike to predict the other kinds of categories, to predict the result of sports should use the latest data. The change of player/coach or the strategy/tactic the team uses could heavily affect the prediction. In this case, to preform this prediction for Super Bowl, I use the data from NFL 2018 season.
# 
# I used all the gaming result as my dataset to develop a linear regression. As we can see in the following, both of the plot and score show a strong linear relationship.
# 
# Regarding the Game Location, I set it to dummy variables. Since Rams will be the home team, I manually changed it to 1 as HOME, and the Game Location for Patriots is 0 as AWAY.
# 
# In order to conduct the prediction, I used the average performance of each team (Rams and Patriots) as the values and got the final result of 29:27, Rams wins. I chose the average as the values is beacuse I believe the average could show how the team is currently doing.
# 
# Please see the following for the prediction model.

# In[83]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import seaborn as sns


# In[69]:


FEATURE_LIST = ['Game Location',
                'Team_Rushing',
                'Team_Passing', 
                'Total Team Yards', 
                'Team_Turnovers', 
                'Opponent_Passing', 
                'Opponent_Rushing',
                'Total Opponent Yards',
                'Opponent_Turnovers']
LABEL_COL = 'Team_Score'


# In[70]:


data = pd.read_excel("./NFL+2018+Season+Data.xlsx")
data['Game Location'] = data['Game Location'].map({"HOME": 1, "AWAY": 0})
data.head()


# In[71]:


X = data[FEATURE_LIST]
Y = data[LABEL_COL]


# In[72]:


X = np.nan_to_num(X)
Y = np.nan_to_num(Y)


# In[73]:


lm = linear_model.LinearRegression()
lm.fit(X, Y)


# In[74]:


print(lm.coef_)
print(lm.intercept_)
print(lm.score(X,Y))


# In[75]:


plt.scatter(Y, lm.predict(X))


# In[76]:


d1 = data.groupby(by = "Team").mean()
X_d1 = d1[FEATURE_LIST]
Y_d1 = d1[LABEL_COL]


# In[84]:


corr = d1.corr()
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True
f, ax = plt.subplots(figsize=(11, 9))
cmap = sns.diverging_palette(220, 10, as_cmap=True)
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})


# In[77]:


plt.scatter(Y_d1, lm.predict(X_d1))


# In[78]:


d1.loc['Los Angeles Rams']['Game Location'] = 1
x = d1.loc['Los Angeles Rams']
y = x[LABEL_COL]
x = x[FEATURE_LIST]


# In[79]:


lm.predict(x.values.reshape(1, -1))


# In[80]:


d1.loc['New England Patriots']['Game Location'] = 0
x = d1.loc['New England Patriots']
y = x[LABEL_COL]
x = x[FEATURE_LIST]


# In[81]:


lm.predict(x.values.reshape(1, -1))

