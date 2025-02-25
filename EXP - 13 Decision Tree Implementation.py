class DecisionTree:
    def __init__(self):
        self.tree = {}

    def fit(self, X, y):
        self.tree = self.build_tree(X, y)

    def build_tree(self, X, y):
        if all(label == y[0] for label in y):  # If all labels are the same, return that label
            return y[0]

        best_feature = 0  # Since we have only two features, we split on Feature 1
        left_X, left_y, right_X, right_y = [], [], [], []

        for i in range(len(X)):
            if X[i][best_feature] == 1:
                left_X.append(X[i])
                left_y.append(y[i])
            else:
                right_X.append(X[i])
                right_y.append(y[i])

        return {
            'feature': best_feature,
            'left': self.build_tree(left_X, left_y),
            'right': self.build_tree(right_X, right_y)
        }

    def predict_one(self, row, tree):
        if isinstance(tree, int):
            return tree
        feature = tree['feature']
        return self.predict_one(row, tree['left'] if row[feature] == 1 else tree['right'])

    def predict(self, X):
        return [self.predict_one(row, self.tree) for row in X]


# Training Data (Features & Labels)
X = [[1, 1], [1, 0], [0, 1], [0, 0]]
y = [1, 1, 0, 0]

# Train Decision Tree
clf = DecisionTree()
clf.fit(X, y)

# Predict for (1,1)
prediction = clf.predict([[1, 1]])
print("Prediction for (1,1):", prediction[0])
