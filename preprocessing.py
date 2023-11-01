# TODO gooi de data door preprocessing



def preprocessing(df):
	df.drop('id', axis=1, inplace=True) 
	#df['sqft_lot15'] = df['sqft_lot15'].astype(str).str.replace(r"b'|'", '')
	df['sqft_lot15'] = df['sqft_lot15'].apply(lambda x: x.split("'")[1])
	return df
