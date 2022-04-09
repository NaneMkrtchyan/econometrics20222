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
      "source": "ls = [9, 10, 11, 12, 13,14]\nprint(ls)\nfor el in ls: \n    print (el)",
      "metadata": {
        "trusted": "True"
      },
      "execution_count": 31,
      "outputs": [
        {
          "name": "stdout",
          "text": "[9, 10, 11, 12, 13, 14]\n9\n10\n11\n12\n13\n14\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "code",
      "source": "for i in range(9,15): \n    i *= 5 \n    print(i)\n",
      "metadata": {
        "trusted": "True"
      },
      "execution_count": 32,
      "outputs": [
        {
          "name": "stdout",
          "text": "45\n50\n55\n60\n65\n70\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "code",
      "source": "ls2 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]\nprint(len(ls2))\nwhile(len(ls2)>0):\n    ls2.pop()\n    print(ls2)\n    ",
      "metadata": {
        "trusted": "True"
      },
      "execution_count": 45,
      "outputs": [
        {
          "name": "stdout",
          "text": "10\n[3, 4, 5, 6, 7, 8, 9, 10, 11]\n[3, 4, 5, 6, 7, 8, 9, 10]\n[3, 4, 5, 6, 7, 8, 9]\n[3, 4, 5, 6, 7, 8]\n[3, 4, 5, 6, 7]\n[3, 4, 5, 6]\n[3, 4, 5]\n[3, 4]\n[3]\n[]\n",
          "output_type": "stream"
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
