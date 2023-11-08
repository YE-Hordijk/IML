import os
import pandas as pd
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression
import matplotlib.pyplot as plt
#import FancyFunctions as ff


#*******************************************************************************

def show_feature_and_price(df):
	fig, axs = plt.subplots(4, 5)
	fig.set_size_inches(22, 14)
	for i, feature in enumerate(df):
		axs[i//5, i%5].scatter(df[str(feature)], df['price'], c = 'magenta', marker='.', s=10, alpha = 0.25)
		axs[i//5, i%5].set_title(str(feature), fontsize=14)
		#axs[i//5, i%5].set_xlabel(str(feature))
		#axs[i//5 , i%5].set_ylabel('price')
	fig.delaxes(axs[3][4])
	fig.tight_layout()
	plt.savefig(f'Results/FeatureCorrelation.png', dpi = 150) # store in "Results"-folder
	plt.close()

#*******************************************************************************

def feature_selection(df):
	print(f"\n\033[42m <-> K-Score of the features based on SelectKBest\033[0m")
	# Selection
	fs = SelectKBest(score_func=f_regression, k='all')
	fs.fit(df.drop(columns=['price']), df['price'])

	# Plotting
	for i in range(len(fs.scores_)):
		print('Feature score %s: %f' % (df.columns[i], fs.scores_[i]))
	plt.bar([i for i in df.drop(columns=['price']).columns], fs.scores_)
	plt.xlabel('Feature')
	plt.ylabel('K-Score based on SelectKBest function')
	plt.xticks(rotation=90)
	plt.tight_layout()
	plt.savefig(f'Results/FeatureRelevance.png', dpi = 150) # store in "Results"-folder
	plt.close()

#*******************************************************************************

def Price_Distribution(df):
	nrBins = 150
	plt.figure(figsize=(8, 6)) # set size of the graph
	plt.hist(df['price'], bins=nrBins, color='skyblue', edgecolor='black') # bar plot
	# Line graph
	#width = 0.5
	#counts, bins, bars = plt.hist(df['price'], bins=nrBins, color='skyblue', edgecolor='black')
	#plt.close()
	#plt.plot(bins[:-1] + width/2, counts)

	plt.xlabel('Price') 
	plt.ylabel('Frequency')
	plt.yscale("log")
	plt.title('Price Distribution Plot')
	plt.savefig(f'Results/price_distribution_plot_[{nrBins}].png') # store in "Results"-folder
	plt.close()

#*******************************************************************************

def plot_missing_values(df):
	missing_values = df.isnull().sum() # count # missing values per column
	plt.figure(figsize=(10, 6))
	missing_values.plot(kind='bar', color='skyblue')
	plt.title('Number of Missing Values in Each Column')
	plt.xlabel('Columns')
	plt.ylabel('Missing Values Count')
	plt.xticks(rotation=45)
	plt.tight_layout()
	plt.savefig(f'Results/MissingValues.png') # store in "Results"-folder
	plt.close()

#*******************************************************************************

def calculate_price_correlation(df):
	print(f"\n\033[42m <-> Correlation values of Features vs Price\033[0m")
	columns_to_compare = df.columns[df.columns != 'price']
	correlations = {}
	for col in columns_to_compare: # for each feature find correlation with price
		correlation = df['price'].corr(df[col])
		correlations[col] = correlation
	df_corr = pd.DataFrame.from_dict(correlations, orient='index', columns=['Correlation'])
	df_corr = df_corr.sort_values(by=['Correlation'], ascending=False, key=abs)
	df_corr.plot.bar(rot=70, title="Correlation features vs price")
	plt.tight_layout()
	plt.savefig(f'Results/FeaturePriceCorrelationValues.png') # store in "Results"-folder
	print(df_corr)

#*******************************************************************************

