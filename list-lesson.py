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
      "source": "ls = [\"a\",\"b\", \"c\", \"d\",\"e\", \"j\"]\nprint(ls)\nprint(len(ls))\nprint(ls[2:-3])\nls.append(\"s\")\nprint(ls)\nls.remove(\"b\")\nprint(ls)\nd = {'a':'1'}\nd['b'] = '2'\nprint(d)\nd['a'] = '3'\nprint(d)\n",
      "metadata": {
        "trusted": 'True'
      },
      "execution_count": 1,
      "outputs": [
        {
          "name": "stdout",
          "text": "['a', 'b', 'c', 'd', 'e', 'j']\n6\n['c']\n['a', 'b', 'c', 'd', 'e', 'j', 's']\n['a', 'c', 'd', 'e', 'j', 's']\n{'a': '1', 'b': '2'}\n{'a': '3', 'b': '2'}\n",
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
