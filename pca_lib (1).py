import numpy as np

class MyPCALibrary:
    """ Custom PCA library for Advanced Linear Algebra """
    def __init__(self, n_components=2):
        self.n_components = n_components
        self.components = None
        self.mean = None

    def fit(self, X):
        self.mean = np.mean(X, axis=0)
        X_adj = X - self.mean
        cov = np.cov(X_adj.T)
        vals, vecs = np.linalg.eig(cov)
        idx = np.argsort(vals)[::-1]
        self.components = vecs[:, idx][:, :self.n_components].real

    def transform(self, X):
        X_adj = X - self.mean
        return np.dot(X_adj, self.components)
