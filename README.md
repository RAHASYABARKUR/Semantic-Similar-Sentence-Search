# Semantically Similar Sentences Search
The project aims to develop a search tool for sentences that are semantically similar. The process currently uses publicly available UCI's News20 Dataset. The dataset is cleaned, encoded using Mini LM Transformer and then clustered using KMeans. The client provides a sample text, which is similarly encoded and semantic value is predicted with the help of the pre-trained Kmeans. The semantic value of this text is used to find all the sentences in the database with similar semantic values.

This project is part of an Independent Study under the supervision of Brian Levine and Prasanna Lakkur Subramanyam. 


![Architecture](images/Algorithm.png)|
|:--:|
| <b> Fig.1 - Architecture</b>|

## Dependencies
To install dependencies execute the following command

    pip install -r requirements.txt

## Usage
To Encode the Dataset and save it in Encoded Dataset folder please follow the below command 

    python main.py

To evaluate the clustering process please run the server and client in two different terminals
    # To start the server
    python server.py
    # To Push sample statement to the client 
    python client.py "text_message" 
    # (For Example run -> python client.py "I am a little confused on all of the models of the 88-89 bonnevilles. I have heard of the LE SE LSE SSE SSEI. Could someone tell me the differences are far as features or performance. I am also curious to know what the book value is for prefereably the 89 model. And how much less than book value can you usually get them for. In other words how much are they in demand this time of year. I have heard that the mid-spring early summer is the best time to buy.")

## Citation
If you find our work useful in your research, please consider citing:  

    @misc{twenty_newsgroups_113,
          author       = {Mitchell, Tom},
          title        = {{Twenty Newsgroups}},
          year         = {1997},
          howpublished = {UCI Machine Learning Repository},
          doi          = {10.24432/C5C323}
         }
