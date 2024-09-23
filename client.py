from flask_ml.flask_ml_client import MLClient
from flask_ml.flask_ml_server.constants import DataTypes

TEXT_CLUSTERING_MODEL_URL = "http://127.0.0.1:5000/textclusteringmodel" 


client = MLClient(TEXT_CLUSTERING_MODEL_URL)  # Create an instance of the MLClient object

inputs = [
    {"text": "I am a little confused on all of the models of the 88-89 bonnevilles. I have heard of the LE SE LSE SSE SSEI. Could someone tell me the differences are far as features or performance. I am also curious to know what the book value is for prefereably the 89 model. And how much less than book value can you usually get them for. In other words how much are they in demand this time of year. I have heard that the mid-spring early summer is the best time to buy."},
    #{"text": "Another text to be classified"},
]  # The inputs to be sent to the server
data_type = DataTypes.TEXT  # The type of the input data

response = client.request(inputs, data_type)  # Send a request to the server
#print("Text Clustering Model Response:")
#print(response)  # Print the response
