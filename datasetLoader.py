import pandas as pd
from sklearn.datasets import fetch_20newsgroups
import re
import nltk
from nltk.corpus import stopwords

nltk.download("punkt_tab")
nltk.download("stopwords")


def get_dataset():
    dataset = fetch_20newsgroups(
        subset="train", shuffle=True, remove=("headers", "footers", "quotes")
    )
    # print(dataset.target_names)
    data = {"text": dataset.data, "target": dataset.target}
    df = pd.DataFrame(data)
    df["text"] = df["text"].apply(lambda text: preprocess_text(text))
    df = df[df["text"] != ""]
    df["Labels"] = df["target"].apply(lambda text: dataset.target_names[text])
    dataset_test = fetch_20newsgroups(
        subset="test", shuffle=True, remove=("headers", "footers", "quotes")
    )
    # print(dataset_test.target_names)
    data_test = {"text": dataset_test.data, "target": dataset_test.target}
    df_test = pd.DataFrame(data_test)
    df["text"] = df_test["text"].apply(lambda text: preprocess_text(text))
    df_test = df_test[df_test["text"] != ""]
    df_test["Labels"] = df["target"].apply(lambda text: dataset.target_names[text])
    print(
        "Train DataFame shape: "
        + str(df.shape)
        + " and Test Dataframe shape "
        + str(df_test.shape)
    )
    return [df, df_test, dataset.target_names]


def preprocess_text(text: str) -> str:
    # remove links
    text = re.sub(r"http\S+", "", text)
    # remove special chars and numbers
    text = re.sub("[^A-Za-z]+", " ", text)

    # remove stopwords
    tokens = nltk.word_tokenize(text)
    tokens = [w for w in tokens if not w.lower() in stopwords.words("english")]
    text = " ".join(tokens)
    text = text.lower().strip()

    return text
