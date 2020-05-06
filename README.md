# HSRadar - A Hate Speech Tweets Detection Pipeline
### This pipeline is consist of three functions:
#### 1. Twitter crawler
#### 2. Benchmark predictor based on Naive Bayes classifier
#### 3. State-of-art predictor based on Google BERT NLP model
***
### 1. Twitter crawler
This crawler is based on tweepy library and Twitter APIs. It also provides data cleaning function which removes emojis, urls, @ and #.

How to run:
1. Apply for a Twitter Developer account and replace the confidentials in the code.
2. Change the filterin keywords and valid date setting.

### 2. Benchmark predictor based on Naive Bayes classifier
This hate speech tweets predictor is based on Naive Bayes classifier and bag-of-words feature. The data pre-processor provides services of tokenization, removing emojis, urls, @ and #, removing customized stop words and stemming. The classifier defines the bag-of-words feature setting, training and validating process. The functions are developed based on NLTK library.

How to run:
1. Prepare your own training data (e.g. https://data.world/datasets/hate-speech)
2. Train the classifier (pre-process is default)
3. Predict the hate speech tweets in your test data

### 3. State-of-art predictor based on Google BERT NLP model
This hate speech tweets predictor is base on Google BERT NLP model. The run_classifier.py has been modified by extending a processor class to fit the model to this project.

How to run:
1. Prepare your own training data (e.g. https://data.world/datasets/hate-speech) and split the training and validating data sets
2. Download a pretrained model from Google BERT GitHub site
3. Train (fine-tune) the model by running train.sh
4. Predict the hate speech tweets in your test data by running predict.sh
3. Predict the hate speech tweets in your test data.
