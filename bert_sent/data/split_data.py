import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle

def read_data(path):
    total_df = pd.read_csv(os.path.join(path, "training_data.csv"))
    # shuffle
    total_df = shuffle(total_df)
    # "review" is the text content, "label 0" is negative, "label 1" is posistive
    return total_df.review, total_df.label

if __name__ == '__main__':
    path = "./training_data/"
    review, label = read_data(path)
    # split the training data into 9:1 train-valid data sets
    review_train, review_valid, label_train, label_valid = train_test_split(review, label, test_size = 0.1, shuffle=shuffle)
    # store split data sets
    train = pd.DataFrame({'label':label_train, 'review': review_train})
    train.to_csv("train.csv", index=False, sep='\t')
    valid = pd.DataFrame({'label':label_valid, 'review': review_valid})
    valid.to_csv("dev.csv", index=False, sep='\t')