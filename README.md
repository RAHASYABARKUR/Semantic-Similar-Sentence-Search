# Semantically Similar Sentences Search
The project aims to develop a search tool for sentences that are semantically similar. The process currently uses publicly available UCI's News20 Dataset. The dataset is cleaned, encoded using Mini LM Transformer and then clustered using KMeans. The tool takes a sample text as input, which is encoded similarly to the train sentences, and the cluster with the closest semantic value is predicted with the help of the pre-trained Kmeans. All the sentences from the dataset which has context similar to the sample sentence are saved in Clustered.xlsx.

This project is part of an Independent Study under the supervision of Brian Levine and Prasanna Lakkur Subramanyam COMPSCI 596E - MAchine Learning Applied to Child Rescue.



![Architecture](images/Algorithm.png)|
|:--:|
| <b> Fig.1 - Architecture</b>|

## Dependencies
To install dependencies execute the following command

    pip install -r requirements.txt

## Usage
To Encode the Dataset and save it in Encoded Dataset folder please follow the below command. Please do not execute if you want to use the pre encoded dataset which is available in

    python main.py

To evaluate the clustering process, we need to start the server. Please run the following command in the terminal
    
    python server.py

To test a sample statement. Please run the following command in a new terminal (please make sure the server is running)
    
    python client.py "text_message" 
    # (For Example run -> python client.py "I am a little confused on all of the models of the 88-89 bonnevilles. I have heard of the LE SE LSE SSE SSEI. Could someone tell me the differences are far as features or performance. I am also         curious to know what the book value is for prefereably the 89 model. And how much less than book value can you usually get them for. In other words how much are they in demand this time of year. I have heard that the mid-spring             early summer is the best time to buy.")

This generates an output excel file called "Clustered.xlsx" which scrapes all the text statements from the database that are related to the sample statement provided by client. The columns ['target','Labels'] is the groundtruth in the dataset. Column['Encoded'] is th embeddings of the text denerated as part of the process and column['Prediction'] is this models prediction.  
## Citation
If you find our work useful in your research, please consider citing:  

    @misc{twenty_newsgroups_113,
          author       = {Mitchell, Tom},
          title        = {{Twenty Newsgroups}},
          year         = {1997},
          howpublished = {UCI Machine Learning Repository},
          doi          = {10.24432/C5C323}
         }
