# TODO visualiseer de data en haal info uit de dataset zodat we daar iets over kunnen schrijven
df = pd.read_csv('/content/drive/MyDrive/iml.csv', on_bad_lines='skip', sep=',', index_col=0)
df_price = df['price']
df = df.drop(columns=['id', 'sqft_lot15', 'price'])

def show_feature_and_price():
  for feature in df:
    plt.scatter(df[str(feature)], df_price, color = 'magenta')
    plt.title(str(feature) + ' correlation with price')
    plt.xlabel(str(feature))
    plt.ylabel('price')
    plt.show()


def feature_selection():
  #selection
  fs = SelectKBest(score_func=f_regression, k='all')
  fs.fit(X_train, y_train)
  X_train_fs = fs.transform(X_train)
  X_test_fs = fs.transform(X_test)

  #plotting
  for i in range(len(fs.scores_)):
  	print('Feature score %s: %f' % (df.columns[i], fs.scores_[i]))
  plt.bar([i for i in df.columns], fs.scores_)
  plt.xlabel('Feature')
  plt.ylabel('K-Score based on SelectKBest function')
  plt.xticks(rotation=90)
  plt.show()

show_feature_and_price()
feature_selection()
