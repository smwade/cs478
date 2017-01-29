import numpy as np
from matplotlib import pyplot as plt

def print_decision_boundry(X, Y, model, h=.01):
    """ Show decission boundry for classification.
    Args:
      X : (np.array) Data
      Y : (np.array) Labels
      model : (BaseLearner) the model for prediction
      h : (float) resolution
    """
    plt.figure(figsize=(8,8))
    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])

    Z = Z.reshape(xx.shape)
    plt.figure(1, figsize=(4, 3))
    plt.pcolormesh(xx, yy, Z, cmap=plt.cm.Pastel2)

    # Plot also the training points
    plt.scatter(X[:, 0], X[:, 1], c=Y, edgecolors='k', cmap=plt.cm.Accent,s=50)

    plt.title("Non-Seperable Data")
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.show()
