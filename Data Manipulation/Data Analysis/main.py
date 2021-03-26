import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


def main():
    plt.style.use('bmh')
    # Store the data
    col_list = [ "average_water_level"]
    data_store = pd.read_csv('../../Data/tcc-water-dam-levels.csv', usecols=col_list)
    print(data_store)

    # Visualize the Storage Rate
    plt.figure(figsize=(16, 8))
    plt.title('Storage/day')
    plt.xlabel('Days')
    plt.ylabel('Storage Level')
    plt.plot(data_store['average_water_level'])
    plt.savefig('../Data Visualisation/foo.png')
    plt.show()

    # Create a variable to predict
    future_days = 365
    # Create a new column
    data_store['prediction'] = data_store[['average_water_level']].shift(-future_days)

    # Create the feature date set and convert it to a numpy array, and remove last rows
    X = np.array(data_store.drop('prediction', axis=1), dtype=str)[:-future_days]
    # print(X)

    # Create the target data set and convert it to numpy array and give it all target values except the last rows
    y = np.array(data_store['prediction'])[:-future_days]
    print(y)



if __name__ == "__main__":
    main()
