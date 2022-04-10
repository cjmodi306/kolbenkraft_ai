# -*- coding: utf-8 -*-
"""utils.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wfUXqOxaLfIshtJ52iZW_i_E24coDCwP
"""

import numpy as np
import h5py

def load_data():
    train_dataset = h5py.File('/content/drive/MyDrive/Colab_Notebooks/Kolbenkraft/cat_noncat/datasets/train_catvnoncat.h5', "r")
    train_set_x_orig = np.array(train_dataset["train_set_x"][:]) # your train set features
    train_set_y_orig = np.array(train_dataset["train_set_y"][:]) # your train set labels

    test_dataset = h5py.File('/content/drive/MyDrive/Colab_Notebooks/Kolbenkraft/cat_noncat/datasets/test_catvnoncat.h5', "r")
    test_set_x_orig = np.array(test_dataset["test_set_x"][:]) # your test set features
    test_set_y_orig = np.array(test_dataset["test_set_y"][:]) # your test set labels

    classes = np.array(test_dataset["list_classes"][:]) # the list of classes
    
    train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))
    test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))
    
    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes

def sigmoid(z):
    a = 1/(1+np.exp(-z))
    return a

def relu(z):
    a = np.maximum(0,z)
    return z

def sigmoid_backward(dA, cache):
    z = cache
    s = 1/(1+np.exp(-z))
    dZ = dA*s*(1-s)
    assert(dZ.shape == z.shape)
    return dZ
    
def relu_backward(dA, cache):
    z = cache
    dZ = np.array(dA, copy=True)
    dZ[z <= 0] = 0
    assert(dZ.shape == z.shape)
    return dZ