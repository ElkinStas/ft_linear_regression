import pandas as pd


data = pd.read_csv('data.csv')
SigmaXY = sum(data['price']*data['km'])
SigmaX_SigmaY = (sum(data['price'])*sum(data['km']))/len(data)
Slope = (SigmaXY - SigmaX_SigmaY)/(sum(data['km']**2) - (sum(data['km'])**2/len(data)))
Intercept = (sum(data['price'])/len(data)) - Slope*(sum(data['km'])/len(data))
with open('theta_value_file', 'w') as f:
    f.write(str(Slope)+'\n')
    f.write(str(Intercept))