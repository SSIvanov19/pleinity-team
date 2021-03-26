import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


def main():
    pd.options.mode.chained_assignment = None  # default='warn'
    plt.style.use('bmh')
    # Store the data
    col_list = ["average_water_level"]
    data_store = pd.read_csv('../../Data/tcc-water-dam-levels.csv', usecols=col_list)

    # Visualize the Storage Rate
    plt.figure(figsize=(16, 8))
    plt.title('Storage/day')
    plt.xlabel('Days')
    plt.ylabel('Storage Level')
    plt.plot(data_store['average_water_level'])
    plt.savefig('../Data Visualisation/basic_model.png')

    # Create a variable to predict
    future_days = int(input())
    # Create a new column
    data_store['prediction'] = data_store[['average_water_level']].shift(-future_days)

    # Create the future date set and convert it to a numpy array, and remove last rows
    X = np.array(data_store.drop('prediction', axis=1), dtype=float)[:-future_days]

    # Create the target data set and convert it to numpy array and give it all target values except the last rows
    Y = np.array(data_store['prediction'])[:-future_days]

    # Split data into training and testing
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.25)

    # Create the models
    # Create the decision tree regressor model
    decision_tree = DecisionTreeRegressor().fit(x_train, y_train)

    # Create the linear regression model
    linear_regression = LinearRegression().fit(x_train, y_train)

    # Get the last rows of the future data set
    future_set = data_store.drop(['prediction'], 1)[:-future_days]
    future_set = future_set.tail(future_days)
    future_set = np.array(future_set)

    # Show the model tree prediction
    tree_prediction = decision_tree.predict(future_set)

    # Show the model linear regression prediction
    linear_prediction = linear_regression.predict(future_set)

    # Visualize the data
    predictions = tree_prediction
    valid = data_store[X.shape[0]:]
    valid['prediction'] = predictions

    plt.figure(figsize=(16,8))
    plt.title('Tree Prediction Model')
    plt.xlabel('Days')
    plt.ylabel('Storage Level')
    plt.plot(valid[['prediction']])
    plt.savefig('../Data Visualisation/decision_tree_prediction.png')

    predictions = linear_prediction
    valid = data_store[X.shape[0]:]
    valid['prediction'] = predictions

    plt.figure(figsize=(16, 8))
    plt.title('Linear Regression Model')
    plt.xlabel('Days')
    plt.ylabel('Storage Level')
    plt.plot(valid[['prediction']])
    plt.savefig('../Data Visualisation/linear_regression_prediction.png')


if __name__ == "__main__":
    main()
