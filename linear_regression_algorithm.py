import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random


def square_trick(base_price, price_per_room, num_rooms, price, learning_rate):

    predicted_price = base_price + price_per_room * num_rooms
    base_price += learning_rate * (price - predicted_price)
    price_per_room += learning_rate * (price - predicted_price) * num_rooms
    return price_per_room, base_price

def linear_regression(features, labels, learning_rate=0.01, epochs=1000):
    
    price_per_room = random.random()
    base_price = random.random()
    
    for epoch in range(epochs):
        i = random.randint(0, len(features) - 1)
        num_rooms = features[i]
        price = labels[i]
        price_per_room, base_price = square_trick(base_price, price_per_room, num_rooms, price, learning_rate = learning_rate)

    return price_per_room, base_price


# Create dataset
features = np.array([1, 2, 3, 5, 6, 7])
labels = np.array([155, 197, 244, 356, 407, 448])

price_per_room, base_price = linear_regression(features, labels, learning_rate = 0.01, epochs = 10000)

# predicted line
predicted_labels = base_price + price_per_room * features

# plot with equation
plt.scatter(features, labels, label='Actual Data')
plt.plot(features, predicted_labels, color='red', label=f'Price = {price_per_room:.2f} * Rooms + {base_price:.2f}')
plt.legend()
plt.show()
