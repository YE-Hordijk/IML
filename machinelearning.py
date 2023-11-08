# Train models and return the metrics
import parameteropti as po # self made script

import pandas as pd # Import package for dataframes
from sklearn.linear_model import LinearRegression # Import package for regression
from sklearn.model_selection import train_test_split
#from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC, SVR




#*******************************************************************************
def Regression(df, Target):
	print(f"\n\033[42m <-> Regression\033[0m")
	# Prepare train- and test-set
	X = df.drop(Target, axis=1) # Remove the target table from the trainingset
	y = df[Target] # Targets
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

	# Create Model
	#model = LinearRegression() # Create the regression model
	#model = make_pipeline(StandardScaler(), SVR(C=500, kernel='rbf', epsilon=0.2))
	model = SVR(kernel='rbf')  # Other kernels: e.g., linear, rbf, polynomial

	model.fit(X_train, y_train) # Train the mdoel

	# Make predictions
	y_pred = model.predict(X_test)
	print(y_pred)


	# Measure performance
	print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred, squared=True)}")
	"""
	plt.scatter(X_test, y_test, color = 'magenta')
	#plt.plot(X_test, y_pred, color = 'green')
	plt.title('Support Vector Regression Model')
	plt.xlabel('square foot livingroom')
	plt.ylabel('price')
	plt.show()
	#"""
	
	return 1

#*******************************************************************************
def Classification(df, Target):
	# TODO
	return 1
#*******************************************************************************
