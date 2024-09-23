import os

import pandas as pd

from datasetLoader import get_dataset
from sentenceTransformerEncoder import encode

Train, Test, Labels = get_dataset()
TrainEncoded, TestEncoded = encode(Train, Test)
print(os.pwd)
TrainEncoded.to_pickle("EncodedDataset//Train.pkl")
TestEncoded.to_pickle("EncodedDataset//Test.pkl")
