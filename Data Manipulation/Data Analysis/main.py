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

   


if __name__ == "__main__":
    main()
