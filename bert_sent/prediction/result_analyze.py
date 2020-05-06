import pandas as pd

bert_df = pd.read_csv("./en2_classify.csv", sep="\t")
nb_df = pd.read_csv("./en2_NB_classify.csv", sep="\t")

bert_hate_id = []
bert_hate_tweet = []
nb_hate_id = []
nb_hate_tweet = []

for i in range(len(bert_df.classify)):
  if bert_df.classify[i] == 1:
    bert_hate_id.append(i)
    bert_hate_tweet.append(bert_df.tweet[i])

for i in range(len(nb_df.label)):
  if nb_df.label[i] == 1:
    nb_hate_id.append(i)
    # nb_df.review is tokenized and stemmed, not human readable
    nb_hate_tweet.append(bert_df.tweet[i])

# print(len(bert_hate)) #61
# print(len(nb_hate)) #133

bert_hate_df = pd.DataFrame({'id':bert_hate_id, 'tweet': bert_hate_tweet})
nb_hate_df = pd.DataFrame({'id':nb_hate_id, 'tweet': nb_hate_tweet})

bert_hate_df.to_excel("./bert_hate_count.xls")
nb_hate_df.to_excel("./nb_hate_count.xls")


