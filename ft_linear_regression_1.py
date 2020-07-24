import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


def Regression(Intercept, Slope,mileage):
    return (Intercept + Slope * mileage)

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
        print(Regression(float(Intercept), float(Slope), mileage))
        gav = []
        for line in data['km']:
            ret = Regression(float(Intercept), float(Slope),line)
            gav.append(ret)
        plt.plot(data['km'], data['price'])
        plt.plot(data['km'], gav)
        plt.show()
    except ValueError as e:
        print(e)
        print("error: Please enter a number.")

main()