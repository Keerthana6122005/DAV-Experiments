{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPtljEdGv+FxhCVhuiLlrgB",
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
      "execution_count": null,
      "metadata": {
        "id": "rOzi1UII6l_f"
      },
      "outputs": [],
      "source": [
        "\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "df = pd.read_csv(\"tested.csv\")\n",
        "print(\"Dataset loaded successfully!\")"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.head()\n"
      ],
      "metadata": {
        "id": "HIHKWNeH6n6X"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.tail()"
      ],
      "metadata": {
        "id": "rGh0pTpG6wM0"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.shape"
      ],
      "metadata": {
        "id": "SF0ZINNj61Kp"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.columns"
      ],
      "metadata": {
        "id": "soJUjLdr65al"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.dtypes\n",
        "\n"
      ],
      "metadata": {
        "id": "pT5eNZdI686t"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.info()"
      ],
      "metadata": {
        "id": "rZuZzafJ7ApT"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.describe()\n"
      ],
      "metadata": {
        "id": "9U2534Ul7FUD"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df[\"Age\"].mean()"
      ],
      "metadata": {
        "id": "o4FFNwYW7Ism"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df[\"Age\"].median()\n"
      ],
      "metadata": {
        "id": "fr-pyurp7M5h"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df[\"Age\"].mode()\n"
      ],
      "metadata": {
        "id": "kxXnLp-i7QnW"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df[\"Age\"].var()\n"
      ],
      "metadata": {
        "id": "dxaFOLz_7USI"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df[\"Age\"].std()"
      ],
      "metadata": {
        "id": "ncGPJVXC7dCQ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df[\"Age\"].min()\n"
      ],
      "metadata": {
        "id": "Wh49l2WC70Ye"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df[\"Age\"].max()\n"
      ],
      "metadata": {
        "id": "GOujoU7N74ZC"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df[\"Age\"].count()\n"
      ],
      "metadata": {
        "id": "5PvRtvUf8B5U"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df[\"PassengerId\"].unique()\n"
      ],
      "metadata": {
        "id": "selKYOt38IZm"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df[\"Fare\"].nunique()"
      ],
      "metadata": {
        "id": "boUtYCTx8KRK"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df[\"Ticket\"].value_counts()\n"
      ],
      "metadata": {
        "id": "ahqVfL8K8P5Y"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.isnull()"
      ],
      "metadata": {
        "id": "IwoLm-TZ8USd"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.isnull().sum()"
      ],
      "metadata": {
        "id": "o1hiQ4T-8Yfz"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.isnull().mean()*100\n"
      ],
      "metadata": {
        "id": "Ee0CR54_8bv7"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_no_missing = df.dropna()\n",
        "\n",
        "df_no_missing.head()\n",
        "\n"
      ],
      "metadata": {
        "id": "dxID3DRJ8lOi"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df[\"Fare\"] = df[\"Fare\"].fillna(\"Unknown\")"
      ],
      "metadata": {
        "id": "2Szfr9gg8p-V"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.duplicated()"
      ],
      "metadata": {
        "id": "bzUacDXD8zFn"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df=df.drop_duplicates()"
      ],
      "metadata": {
        "id": "tveY8Tvq82uV"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df[\"Name\"]"
      ],
      "metadata": {
        "id": "GQFHvlsR83_a"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df[[\"Name\",\"PassengerId\",\"Age\"]]"
      ],
      "metadata": {
        "id": "Ggjh9vo28-Xa"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.iloc[0:5]"
      ],
      "metadata": {
        "id": "-1A0Bia98_5T"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df[df[\"Age\"]>30]\n"
      ],
      "metadata": {
        "id": "HMj2IvGv9ESI"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.sort_values(\"Age\")"
      ],
      "metadata": {
        "id": "F5rBE2_k9H-l"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.sort_values(\"Age\",ascending=False)"
      ],
      "metadata": {
        "id": "6AXNhg4W9L2l"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.rename(columns={\"Age\": \"Age\"}, inplace=True)\n",
        "\n",
        "df.head()"
      ],
      "metadata": {
        "id": "7Q5J_OIO9Sgo"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.groupby(\"Name\").size()"
      ],
      "metadata": {
        "id": "IY2k9rts9Tgy"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.groupby(\"Name\")[\"Age\"].mean()\n"
      ],
      "metadata": {
        "id": "C6SGOucZ9XG0"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df1 = df.iloc[:3000]\n",
        "df2 = df.iloc[3000:]\n",
        "\n",
        "combined_df = pd.concat([df1, df2])\n",
        "\n",
        "combined_df.shape\n"
      ],
      "metadata": {
        "id": "JDYKDXwB9aj8"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df1 = df[[\"PassengerId\", \"Name\"]]\n",
        "df2 = df[[\"PassengerId\", \"Age\"]]\n",
        "\n",
        "merged_df = pd.merge(df1, df2, on=\"PassengerId\")\n",
        "\n",
        "merged_df.head()"
      ],
      "metadata": {
        "id": "18IUjVHF9fgt"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "wxi3y9149jGP"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}