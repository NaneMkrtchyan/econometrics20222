Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
{  
  "metadata": {
    "language_info": {
      "codemirror_mode": {
        "name": "python",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8"
    },
    "kernelspec": {
      "name": "python",
      "display_name": "Pyolite",
      "language": "python"
    }
  },
  "nbformat_minor": 4,
  "nbformat": 4,
  "cells": [
    {
      "cell_type": "code",
      "source": "import numpy as np",
      "metadata": {
        "trusted": "true"
      },
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "arr1 = np.array([1,2,3,4,5])",
      "metadata": {
        "trusted": "true"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "arr1.shape",
      "metadata": {
        "trusted": "true"
      },
      "execution_count": 3,
      "outputs": [
        {
          "execution_count": 3,
          "output_type": "execute_result",
          "data": {
            "text/plain": "(5,)"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": "arr1.dtype",
      "metadata": {
        "trusted": "true"
      },
      "execution_count": 4,
      "outputs": [
        {
          "execution_count": 4,
          "output_type": "execute_result",
          "data": {
            "text/plain": "dtype('int32')"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": "arr1.ndim",
      "metadata": {
        "trusted": "true"
      },
      "execution_count": 5,
      "outputs": [
        {
          "execution_count": 5,
          "output_type": "execute_result",
          "data": {
            "text/plain": "1"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": "arr1.dtype",
      "metadata": {
        "trusted": "true"
      },
      "execution_count": 6,
      "outputs": [
        {
          "execution_count": 6,
          "output_type": "execute_result",
          "data": {
            "text/plain": "dtype('int32')"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": "arr3 = np.arange(0,10,1.5)\narr3",
      "metadata": {
        "trusted": "true"
      },
      "execution_count": 7,
      "outputs": [
        {
          "execution_count": 7,
          "output_type": "execute_result",
          "data": {
            "text/plain": "array([0. , 1.5, 3. , 4.5, 6. , 7.5, 9. ])"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": "arr_random = np.random.random((10,))",
      "metadata": {
        "trusted": "true"
      },
      "execution_count": 8,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "arr_random",
      "metadata": {
        "trusted": "true"
      },
      "execution_count": 9,
      "outputs": [
        {
          "execution_count": 9,
          "output_type": "execute_result",
          "data": {
            "text/plain": "array([0.98089096, 0.37901846, 0.8459299 , 0.95582719, 0.64649341,\n       0.87545039, 0.91310441, 0.56303572, 0.87657151, 0.42136956])"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": "matrix = np.array([(11, 12, 13), (1, 2, 3), (21, 22, 23)])",
      "metadata": {
        "trusted": "true"
      },
      "execution_count": 10,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "matrix",
      "metadata": {
        "trusted": "true"
      },
      "execution_count": 11,
      "outputs": [
        {
          "execution_count": 11,
          "output_type": "execute_result",
          "data": {
            "text/plain": "array([[11, 12, 13],\n       [ 1,  2,  3],\n       [21, 22, 23]])"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": "matrix.shape",
      "metadata": {
        "trusted": "true"
      },
      "execution_count": 12,
      "outputs": [
        {
          "execution_count": 12,
          "output_type": "execute_result",
          "data": {
            "text/plain": "(3, 3)"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": "matrix.ndim",
      "metadata": {
        "trusted": "true"
      },
      "execution_count": 13,
      "outputs": [
        {
          "execution_count": 13,
          "output_type": "execute_result",
          "data": {
            "text/plain": "2"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": "matrix.size",
      "metadata": {
        "trusted": "true"
      },
      "execution_count": 14,
      "outputs": [
        {
          "execution_count": 14,
          "output_type": "execute_result",
          "data": {
            "text/plain": "9"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": "",
      "metadata": {},
      "execution_count": "null",
      "outputs": []
    }
  ]
} 