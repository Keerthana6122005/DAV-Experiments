{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPmr8F03uLqWE6cq7C13H+D",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Keerthana6122005/DAV-Experiments/blob/main/main.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "7d3F4rh25Ylw"
      },
      "outputs": [],
      "source": [
        "import numpy as np\n",
        "import pandas as pd\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a = np.array([10, 20, 30, 40, 50])\n"
      ],
      "metadata": {
        "id": "oqdbmXQJ5foL"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Array:\", a)\n",
        "print(\"Mean:\", a.mean())\n",
        "print(\"Reshaped 2D:\\n\", a.reshape(5, 1))\n",
        "print(\"Sliced:\", a[1:4])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WOSC8MHV5jEy",
        "outputId": "128e9677-0ee7-473a-9e91-361003cfe18c"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Array: [10 20 30 40 50]\n",
            "Mean: 30.0\n",
            "Reshaped 2D:\n",
            " [[10]\n",
            " [20]\n",
            " [30]\n",
            " [40]\n",
            " [50]]\n",
            "Sliced: [20 30 40]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data = {\n",
        "    \"Name\": [\"Asha\", \"Rani\", \"Meera\", \"Karan\"],\n",
        "    \"Marks\": [88, 72, 91, 65],\n",
        "    \"Branch\": [\"CSE\", \"ECE\", \"CSE\", \"ISE\"]\n",
        "}\n"
      ],
      "metadata": {
        "id": "ep5ODxiq5m2V"
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df = pd.DataFrame(data)"
      ],
      "metadata": {
        "id": "z_4Q09r_5qcj"
      },
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(df)\n",
        "\n",
        "print(\"\\nFirst 2 rows:\\n\", df.iloc[0:2])\n",
        "\n",
        "print(\"\\nMarks column:\\n\", df[\"Marks\"])\n",
        "\n",
        "print(\"\\nRows where marks > 70:\\n\", df[df[\"Marks\"] > 70])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7nL-l9Ni51g8",
        "outputId": "44083bda-d984-499a-f3b5-dc2906af125e"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "    Name  Marks Branch\n",
            "0   Asha     88    CSE\n",
            "1   Rani     72    ECE\n",
            "2  Meera     91    CSE\n",
            "3  Karan     65    ISE\n",
            "\n",
            "First 2 rows:\n",
            "    Name  Marks Branch\n",
            "0  Asha     88    CSE\n",
            "1  Rani     72    ECE\n",
            "\n",
            "Marks column:\n",
            " 0    88\n",
            "1    72\n",
            "2    91\n",
            "3    65\n",
            "Name: Marks, dtype: int64\n",
            "\n",
            "Rows where marks > 70:\n",
            "     Name  Marks Branch\n",
            "0   Asha     88    CSE\n",
            "1   Rani     72    ECE\n",
            "2  Meera     91    CSE\n"
          ]
        }
      ]
    }
  ]
}