import pandas as pd

data = pd.read_csv('data.csv')
a = 0
b = 0

x_train = data['km'] / 1000
y_train = data['price'] / 1000
lr = 0.0001

def regression(teta0, teta1, mileage):
    
    return (teta0 + teta1 * mileage)

def first_sum(a, b, data):

    x = 0
    x += sum(regression(a, b, data['km']) - data['price'])
    # print(x)
    return (x / len(data))

def second_sum(a, b, data):

    x = 0
    x += sum((regression(a, b, data['km']) - data['price']) * data['km'])
    return (x / len(data))

for epoch in range(200000):
    tmp_a = lr * (first_sum(a, b, data / 1000))
    tmp_b = lr * (second_sum(a, b, data / 1000))
    a = a - tmp_a
    b = b - tmp_b

with open('theta_value_file', 'w') as f:
    f.write(str(b)+'\n')
    f.write(str(a*1000))