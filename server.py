import os

import pandas as pd
from flask_ml.flask_ml_server import MLServer
from flask_ml.flask_ml_server.constants import DataTypes
from flask_ml.flask_ml_server.models import (ResponseModel, TextInput,
                                             TextResult)

from clusteringKMeans import Kmeans


class Test:
    def predict(self, data: list) -> list:
        print("Started Loading the Pre Encoded Data")
        input_data = pd.read_pickle("EncodedDataset/Train.pkl")
        print("Sucessfully Loaded the Encoded Train data")
        return Kmeans(input_data, data[0])


model = Test()

server = MLServer(__name__)


@server.route("/textclusteringmodel", DataTypes.TEXT)
def process_text(inputs: list[TextInput], parameters: dict):
    # print(inputs)
    results = model.predict(inputs)
    results = [TextResult(text=e.text, result=r) for e, r in zip(inputs, results)]
    # print(results)
    response = ResponseModel(results=results)
    return response.get_response()


server.run()
