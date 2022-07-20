import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

import joblib
import sys, os
from tqdm import tqdm

fpath = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(fpath)
# Adding access to super parent directory

from paths import PIPES_DIR, TEMP_DIR
from helpers.phishing.urls_feature_extraction import URLFeatureExtractor

class URLFeatureTransformer(BaseEstimator,TransformerMixin):
    def __init__(self):
        pass
    def fit(self,X,y=None):
        return self
    def transform(self,X,y=None):
        A = X.copy()
        features = []
        for i in (pbar := tqdm(range(len(A)),colour="green",bar_format = "{desc} {percentage:.3f}% |{bar}| ({n_fmt}/{total_fmt}) [Elapsed: {elapsed}, Remaining: {remaining}]")):
            pbar.set_description(A[i][:30] + ' '*(30 - len(A[i][:30])))
            ufe = URLFeatureExtractor(A[i])
            featuresSingle = [
                ufe.havingIP(),
                ufe.long_url(),
                ufe.have_at_symbol(),
                ufe.redirection(),
                ufe.prefix_suffix_separation(),
                ufe.sub_domains(),
                ufe.shortening_service(),
                ufe.domain_registration_length(),
                ufe.dns_record(),
                ufe.age_domain(),
                ufe.https_token(),
            ]
            features.append(featuresSingle)
        if(not os.path.exists(os.path.join(TEMP_DIR,'urlfeatures.dump'))):
            joblib.dump(features,os.path.join(TEMP_DIR,'urlfeatures.dump'))
        return features




class PhishingURL:
    PIPE_SAV_FILE = os.path.join(PIPES_DIR,"phishingurl.pipe")

    def get_model(self):
        random_forest_classifier = RandomForestClassifier()
        return random_forest_classifier

    def get_dataset(self,csv_file):
        df = pd.read_csv(csv_file)
        df = df[['url','status']]

        X = df.url.values
        Y = [0 if status == 'legitimate' else 1 for status in df.status]
        return X,Y

    def process_dataset(self,dataset):
        X,Y = dataset
        X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3)
        return X_train, X_test, Y_train, Y_test

    def create_and_train_model(self,csv_file):
        dataset = self.get_dataset(csv_file)
        processed_dataset = self.process_dataset(dataset)
        X_train, X_test, Y_train, Y_test = processed_dataset

        pipe = Pipeline([
            ('transformer',URLFeatureTransformer()),
            ('clf',self.get_model()),
        ])

        pipe = pipe.fit(X_train,Y_train)
        print(pipe.score(X_test,Y_test))

        joblib.dump(pipe,self.PIPE_SAV_FILE)

    def evaluate(self,csv_file):
        loaded_pipe = joblib.load(self.PIPE_SAV_FILE)
        dataset = self.get_dataset(csv_file)
        processed_dataset = self.process_dataset(dataset)
        X_train, X_test, Y_train, Y_test = processed_dataset
        return loaded_pipe.score(X_test,Y_test)

    def predict(self,url):
        loaded_pipe = joblib.load(os.path.join(self.PIPE_SAV_FILE))
        prediction = loaded_pipe.predict([url])

        return prediction