import numpy as np
from sklearn.metrics import accuracy_score

class Logistic:
    """
    Parameters
    ----------
    tol: double, optional, the stopping criteria for the weights
    max_iter: int, optional, the maximal number of iteration
    """
    def __init__(self, tol=1e-4, max_iter=100):

        self.tol = tol
        self.max_iter = max_iter

    def get_params(self, deep=False):
        """Get parameters for this estimator"""
        return {'tol': self.tol, 'max_iter': self.max_iter}

    def _iteration_step(self, x_train, y_train):
        # put your training code here
        pass

    def train(self, x_train, y_train):
        """Receive the input training data, then learn the model.

        Parameters
        ----------
        x_train: np.array, shape (num_samples, num_features)
        y_train: np.array, shape (num_samples, )

        Returns
        -------
        None
        """
        self.w = np.zeros(x_train.shape[1])
        for _ in range(self.max_iter):
            last_w = self.w.copy()
            self._iteration_step(x_train, y_train)
            if np.linalg.norm(self.w - last_w) < self.tol:
                break
        return

    def fit(self, x_train, y_train):
        # alias for train
        self.train(x_train, y_train)

    def score(self, X, y):
        y_pred = self.predict(X)
        return accuracy_score(y, y_pred)

    def predict(self, x_test):
        """Predict class labels for samples in x_test

        Parameters
        ----------
        x_test: np.array, shape (num_samples, num_features)

        Returns
        -------
        pred: np.array, shape (num_samples, )
        """
        return np.argmax(self.predict_proba(x_test), axis=1)

    def log_loss(self, x_train, y_train):
        """Negative of Likelihood"""

        y_expand = np.vstack([1 - y_train, y_train])
        predict_prob = self.predict_proba(x_train)
        predict_prob += self.tol * (predict_prob == 0).astype(np.float)
        return -np.sum(y_expand.T * np.log(predict_prob))

    def predict_proba(self, x_data):
        """Predict class labels for samples in x_test

        Parameters
        ----------
        x_data: np.array, shape (num_samples, num_features)

        Returns
        -------
        pred: np.array, shape (num_samples, n_classes),
              the probability of the sample for each class in the model
        """
        pred = np.zeros([x_data.shape[0], 2])
        # put your predicting code here
        return pred