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





if __name__ == "__main__":
    main()
