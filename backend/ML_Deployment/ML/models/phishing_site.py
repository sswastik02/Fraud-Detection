import math
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from tokenizers.implementations import ByteLevelBPETokenizer
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn import preprocessing
from xgboost import XGBClassifier
from sklearn.pipeline import Pipeline

import joblib
import sys, os
import collections
import requests

fpath = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(fpath)
# Adding access to super parent directory

from paths import PIPES_DIR
from helpers.phishing.site_temp_to_dataset import temp_files_to_dataset

class BPETransformer(BaseEstimator, TransformerMixin):

    def __init__(self):
        self.tokenizer = ByteLevelBPETokenizer()
        self.token_dict = collections.defaultdict(list)

    def fit(self,X,y = None):
        self.tokenizer.train_from_iterator(X) # we need path for training this, passing raw data won't work
        for fileData in X:
            output = self.tokenizer.encode(fileData)
            output_dict = collections.Counter(output.ids)

            for token in output_dict:
                self.token_dict[token].append("1") # adding first 10 characters, we just need it to keep count

        return self

    def transform(self, X, y = None):
        X_ = X.copy()
        features = []

        for fileData in X_:
            output = self.tokenizer.encode(fileData)
            output_dict = collections.Counter(output.ids)

            feature = [0] * self.tokenizer.get_vocab_size()
            for item in output_dict:
                if len(self.token_dict[item]) > 0:
                    feature[item] = (output_dict[item]) * math.log10(len(X_) / len(self.token_dict[item]))
            features.append(feature)
        return features



class PhishingSite:

    PIPE_SAV_FILE = os.path.join(PIPES_DIR,"phishingsite.pipe")

    def get_model(self):
        model = XGBClassifier(n_estimators = 300)
        return model

    def get_transformer(self,X,path_to_dataset):
        transformer = BPETransformer()
        transformer.fit(X,path_to_dataset)
        return transformer

    def process_dataset(self,dataset):
        X, Y = dataset
        X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.5)
        return X_train,X_test,Y_train, Y_test

    def create_and_train_model(self):
        dataset,dataset_path = temp_files_to_dataset()
        transformer = self.get_transformer(dataset[0],dataset_path)
        processed_dataset = self.process_dataset(dataset)
        X_train, X_test, Y_train, Y_test = processed_dataset

        pipe = Pipeline([
            ('transformer',BPETransformer()),
            ('clf',self.get_model()),
        ])

        pipe = pipe.fit(
            X_train,
            Y_train,
        )

        print(pipe.score(X_test,Y_test))
        
        joblib.dump(pipe,self.PIPE_SAV_FILE)

    def evaluate(self):
        loaded_pipe = joblib.load(self.PIPE_SAV_FILE)
        dataset,dataset_path = temp_files_to_dataset()
        processed_dataset = self.process_dataset(dataset)
        X_train, X_test, Y_train, Y_test = processed_dataset

        return loaded_pipe.score(X_train,Y_train)

    def predict(self,url):
        loaded_pipe = joblib.load(self.PIPE_SAV_FILE)

        try:
            request = requests.get(url)
            webpageHtml = str(request.text)
            webpageHtml = webpageHtml.replace("\n", " ")
            prediction = loaded_pipe.predict([webpageHtml])
            return prediction

        except Exception as e:
            return -1