import pandas as pd
import numpy as np

from nltk.corpus import stopwords
nltk_stopwords = stopwords.words('english')

# Sklearn TF-IDF Libraries
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df_dataset = pd.read_csv("../crawler/layer_three_data.csv")
print("Database loaded")

df_dataset = df_dataset.drop_duplicates(subset=['df_paper_title'])  # remove duplicates

def search(keyword):
    vectorizer = TfidfVectorizer()

    # Index paper titles
    X = vectorizer.fit_transform(df_dataset['df_paper_title'])

    query_vec = vectorizer.transform([keyword])  # Ip -- (n_docs,x), Op -- (n_docs,n_Feats)
    results = cosine_similarity(X, query_vec).reshape((-1,))

    search_result = []
    # Print Top 100 results
    data = {}

    df_data = pd.DataFrame(columns=["Title", "URL", "Abstract", "Author", "Date"])

    for i in results.argsort()[-100:][::-1]:
        data["Title"] = df_dataset.iloc[i, 0]
        data["URL"] = df_dataset.iloc[i, 1]
        data["Abstract"] = df_dataset.iloc[i, 2]
        data["Author"] = df_dataset.iloc[i, 3]
        data["Date"] = df_dataset.iloc[i, 4]

        df_data = df_data.append(data, ignore_index=True)

    # df_data = df_data.to_numpy()
    print(df_data)
    return df_data

