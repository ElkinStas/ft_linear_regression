import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def regression(teta0, teta1, mileage):

    return (teta0 + teta1 * mileage)

def main():

    Intercept = 0
    Slope = 0
    mileage = input("Please enter a mileage: ")
    try:
        mileage = float(mileage)
        data = pd.read_csv('data.csv')
        data = data.sort_values(['km'])
        try:
            with open('theta_value_file', 'r') as f:
                Slope= f.readline()
                Intercept = f.readline()

        except Exception as e:
            pass
        print("Estimate price:")
        print(regression(float(Intercept), float(Slope), mileage))
        new_km = []
        for line in data['km']:
            ret = regression(float(Intercept), float(Slope),line)
            new_km.append(ret)
        plt.plot(data['km'], data['price'])
        plt.plot(data['km'], new_km)
        plt.show()
    except ValueError as e:
        print(e)
        print("error: Please enter a number.")

if __name__ == '__main__':
    main()