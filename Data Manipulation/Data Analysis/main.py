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
    plt.savefig('../Data Visualisation/foo.png')

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

    



if __name__ == "__main__":
    main()
