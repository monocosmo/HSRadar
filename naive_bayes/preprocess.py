import pandas as pd
import re
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import string
from wordcloud import WordCloud
import matplotlib.pyplot as plt

NEGATION_WORDS = ['no', 'not', 'never', 'none', 'nowhere', 
'nothing', 'noone', 'rather', 'hardly', 'scarcely', 'rarely', 
'seldom', 'neither', 'nor', 'ain', 'aren', 'couldn', 'didn', 
'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma', 'mightn', 
'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn']
# complimentary stop words to nltk.stopwords
# RT (retweet) is included
MORE_STOP_WORDS = ['could','would','might','must','need','sha','wo','y',
"'s","'d","'ll","'t","'m","'re","'ve", "n't", "RT"]

def read_data(path):
  df = pd.read_csv(path)
  return df.label, df.review

# remove emojis
def remove_emoji(text):
    emoji = re.compile("["
                       u"\U0001F600-\U0001F64F"  # emoticons
                       u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                       u"\U0001F680-\U0001F6FF"  # transport & map symbols
                       u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                       u"\U00002702-\U000027B0"
                       "]+", flags=re.MULTILINE)
    return emoji.sub(r'', text)

# cleaning, tokenization and stemming
def data_clean(text):
  # remove URL
  text = re.sub(r"http\S+","",str(text))
  # remove emojis
  text = remove_emoji(text)
  # tokenization
  tokens = nltk.word_tokenize(text)
  # remove stopwords and punctuations (@ and # included)
  stop_words = stopwords.words('english') + MORE_STOP_WORDS
  modified_stop_words = [word for word in stop_words if word not in NEGATION_WORDS]
  removal_list = list(string.punctuation) + modified_stop_words
  # stemming
  ps = PorterStemmer()
  # all lower case and clean
  return [ps.stem(token.lower()) for token in tokens if token not in removal_list]

# preparing lists of normal texts or hate texts
def split_lists(list_labels, list_tokens):
  list_normal = []
  list_hate = []
  
  for i in range(len(list_labels)):
    if list_labels[i] == 0:
      list_normal.append(list_tokens[i])
    else:
      list_hate.append(list_tokens[i])
  return list_normal, list_hate

# generating word cloud
def word_cloud(list_tokens):
  text = " ".join([" ".join(tokens) for tokens in list_tokens])
  wc = WordCloud(width=800, height=600, mode='RGBA', background_color=None).generate(text)
  # display
  plt.imshow(wc, interpolation='bilinear')
  plt.axis('off')
  plt.show()
  # save
  wc.to_file('./output/wordcloud.png')

if __name__ == '__main__':
  list_label, list_text = read_data("./data/training_data.csv")
  # clean the texts
  list_text_cleaned = [data_clean(text) for text in list_text]
  # update the training data
  updated_df = pd.DataFrame({'label':list_label, 'review': [" ".join(tokens) for tokens in list_text_cleaned]})
  updated_df.to_csv("./data/cleaned_training_data.csv", index=False, sep='\t')
  # split the lists
  list_normal, list_hate = split_lists(list_label, list_text_cleaned)
  # generate word cloud with list of hate speeches
  word_cloud(list_hate)