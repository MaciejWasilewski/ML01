import pickle
import os
from sklearn.externals import joblib


def save_sets(obj, fname, force=False):
    if not os.path.isfile(fname) or force:
        pickle.dump(obj, open(fname, "wb"))


def load_sets(fname):
    with open(fname, "rb") as file:
        return pickle.load(file)


def save_estimator(obj, fname, force=False):
    if not os.path.isfile(fname) or force:
        with open(fname, "wb") as file:
            joblib.dump(obj, file)


def load_estimator(obj, fname):
    with open(fname, "wb") as file:
        return joblib.load(obj, file)
