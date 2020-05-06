import pandas as pd
import nltk
import pickle
import random
import preprocess as pre

# Generate documents from training dataset
def doc(df):
  documents = []
  for i in range(len(df.label)):
    documents.append((df.review[i].split(" "), df.label[i]))
  # Shuffle the documents
  random.shuffle(documents)
  return documents

# Use the 1000 most frequent words in the documents as feature words
def words_features(documents):
  all_words_list = [word for (sent, cat) in documents for word in sent] 
  all_words = nltk.FreqDist(all_words_list)
  word_items = all_words.most_common(1000)
  # Remove numbers and signs
  word_features = [word for (word, freq) in word_items if word.isalpha()]
  return word_features

# Bag of words feature algorithm
def bag_of_words_feature(document, word_features):
  # Check if each feature word appears in the documents
  # Use the results as features
  document_words = set(document)
  features = {}
  for word in word_features:
      features['V_{}'.format(word)] = (word in document_words)
  return features

# Train Naive Bayes classifier
def train(training_data_path):
  # read the training data
  df = pd.read_csv(training_data_path, sep="\t")
  # generate documents
  documents = doc(df)
  # Generate bag-of-words feature sets
  features = words_features(documents)
  feature_sets = [(bag_of_words_feature(doc, features), cat) for (doc, cat) in documents]
  # Train Naive Bayes classifier with 90% of the feature sets
  length = len(feature_sets)
  train_set, test_set = feature_sets[length//10:], feature_sets[:length//10]
  classifier = nltk.NaiveBayesClassifier.train(train_set)
  # Evaluate the accuracy of the classifier
  accuracy = round(nltk.classify.accuracy(classifier, test_set) * 100, 2)
  print("Using Naive-Bayes classifier and \"bag-of-words\" features get " + str(accuracy) + "% accuracy.")
  # save the trained classifier
  f = open('./model/NBclassifier.pickle', 'wb')
  pickle.dump(classifier, f)
  f.close()

# Use trained classifier to predict classification
def prediction(model_path, training_data_path, test_data_path):
  # Load the trained classifier model
  f = open(model_path, 'rb')
  classifier = pickle.load(f)
  f.close()
  
  # Read the training data
  training_df = pd.read_csv(training_data_path, sep="\t")
  # Generate documents
  documents = doc(training_df)
  # Generate bag-of-words feature sets
  features = words_features(documents)

  # Read the test data
  test_df = pd.read_csv(test_data_path, sep="\t")

  # Tokenize, clean and classification
  results_table = {"review": [], "label": []}
  for sentence in test_df.review:
    tokens = nltk.word_tokenize(sentence)
    clean_tokens = pre.data_clean(tokens)
    test_feature_set = bag_of_words_feature(clean_tokens, features)
    label = classifier.classify(test_feature_set)
    results_table["label"].append(label)
    results_table["review"].append(sentence)

  # Save the results
  results_df = pd.DataFrame.from_dict(results_table)
  results_df.to_csv("./output/result.csv", index=False, sep='\t')

if __name__ == '__main__':
  # train the model
  train("./data/cleaned_training_data.csv")
  # classify the test data
  # prediction("./model/NBclassifier.pickle", "./data/cleaned_training_data.csv", "./data/en2.csv")
