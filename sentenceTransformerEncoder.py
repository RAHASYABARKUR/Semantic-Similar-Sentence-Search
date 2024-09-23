from sentence_transformers import SentenceTransformer


def encode(TrainDf, TestDf):
    model = SentenceTransformer("paraphrase-MiniLM-L6-v2")
    TrainDf["Encoded"] = TrainDf["text"].apply(
        lambda text: model.encode(text, convert_to_numpy=True).flatten()
    )
    TestDf["Encoded"] = TestDf["text"].apply(
        lambda text: model.encode(text, convert_to_numpy=True).flatten()
    )
    return TrainDf, TestDf


def encodeSentence(message):
    model = SentenceTransformer("paraphrase-MiniLM-L6-v2")
    return (
        model.encode(message, convert_to_numpy=True, clean_up_tokenization_spaces=True)
        .flatten()
        .reshape(1, -1)
    )
