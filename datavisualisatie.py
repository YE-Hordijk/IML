# TODO visualiseer de data en haal info uit de dataset zodat we daar iets over kunnen schrijven
df = pd.read_csv('/content/drive/MyDrive/iml.csv', on_bad_lines='skip', sep=',', index_col=0)
df_price = df['price']
df = df.drop(columns=['id', 'sqft_lot15', 'price'])

for feature in df:
  plt.scatter(df[str(feature)], df_price, color = 'magenta')
  plt.title(str(feature) + ' correlation with price')
  plt.xlabel(str(feature))
  plt.ylabel('price')
  plt.show()
