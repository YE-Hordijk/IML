import os
import pandas as pd
import preprocessing as pp
import datavisualisation as dv
import machinelearning as ml



# Create folder for results
if not os.path.exists('Results'): os.makedirs('Results')


# Read the data
file_path = 'Data/HousePriceDataset.csv' 
df = pd.read_csv(file_path, sep=',', index_col=0)


# Preprocessing
df = pp.preprocessing(df)


# Data Exploration and Visualisation
dv.show_feature_and_price(df)
dv.feature_selection(df)
dv.Price_Distribution(df)
dv.plot_missing_values(df)
dv.calculate_price_correlation(df)





# TODO paas de data naar machinelearning. train modellen en gooi metrics terug
ans = ml.Regression(df, "price")

# Hypothese: waterfront & view gaan geen belangrijke features zijn en geen interesante targets door hun monotone waardes
# Hypothese: Year renovated gaan niet interesant zijn omdat er heel veel NaN values in zitten. 

