import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import seaborn as sns
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
data = pd.read_excel("./NFL+2018+Season+Data.xlsx")
data['Game Location'] = data['Game Location'].map({"HOME": 1, "AWAY": 0})
data.head()
