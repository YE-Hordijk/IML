import os
import pandas as pd

import preprocessing as pp
import datavisualisatie as dv
import machinelearning as ml

# Read the data
file_path = 'Data/HousePriceDataset.csv' 
df = pd.read_csv(file_path, sep=',', index_col=0)#, index_col='Timestamp')


# TODO gooi de data door preprocessing
df = pp.preprocessing(df)
print(df)


# TODO visualiseer de data en haal info uit de dataset zodat we daar iets over kunnen schrijven


# TODO paas de data naar machinelearning. train modellen en gooi metrics terug
ans = ml.Regression(df, "price")

# Hypothese: waterfront & view gaan geen belangrijke features zijn en geen interesante targets door hun monotone waardes
# Hypothese: Year renovated gaan niet interesant zijn omdat er heel veel NaN values in zitten. 

