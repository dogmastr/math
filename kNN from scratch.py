"""

    Author: @dogmastr
    Description: Implementation of a K-nearest neighbors algorithm from scratch.

"""

import math
from collections import Counter

def euclidean_distance(x, y):
    return sum([(xi - yi)**2 for xi, yi in zip(x, y)]) ** 0.5

def knn(X, y, x_pred, k=3):
    
    # We create an array of tuples (i, d) where:
    # i is the index of each vector x ∈ X,
    # d is the Euclidean distance d(x, x_pred).
    neighbors = []
    for i, x in enumerate(X):
        neighbors.append((i, euclidean_distance(x, x_pred)))

    # We sort neighbors by Euclidean distance in ascending order and select the k nearest:
    neighbors = sorted(neighbors, key = lambda x: x[1])[:k]

    # We extract labels for these neighbors:
    neighbor_labels = [y[i] for i, _ in neighbors]

    # Now we count the occurrences of each label, obtaining a dictionary {label: count}.
    label_counts = Counter(neighbor_labels)

    # Finally, compute the dictionary {label: probability}.
    total = sum(label_counts.values())
    return {label: count / total for label, count in label_counts.items()}

"""
    
    Example usage:

"""

X = [[1, 2], [2, 3], [3, 1], [4, 5], [3, 4]]
y = [0, 0, 0, 1, 1]

x_pred = [2.5, 3.5]

prediction = knn(X, y, x_pred, k=3)
print("Prediction:", prediction)