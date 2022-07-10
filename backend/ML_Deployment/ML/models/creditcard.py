import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.pipeline import Pipeline

from keras.models import Sequential
from keras.layers import Dense
from scikeras.wrappers import KerasClassifier

import joblib
import sys, os

fpath = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(fpath)
# Adding access to super parent directory

from paths import PIPES_DIR

class CreditCard:

    
    PIPE_SAV_FILE = os.path.join(PIPES_DIR,"creditcard.pipe")
    def get_model(self):
        # model architecture
        model = Sequential([
            Dense(32, activation='relu', input_shape=(9,)),
            Dense(32, activation='relu'),
            Dense(1, activation='sigmoid'),
        ])

        # compile model
        model.compile(
            optimizer='sgd',
            loss='binary_crossentropy',
            metrics=['accuracy']
        )

        return model

    def get_dataset(self,csv_file):
        df = pd.read_csv(csv_file)
        dataset = df.values
        print(df.shape)
        
        X = dataset[:,1:10] # Catergorical Data
        Y = dataset[:,10]  # Class Data

        return X,Y

    def get_scaler(self,dataset=None):
        
        X,_ = dataset
        min_max_scaler = preprocessing.MinMaxScaler()
        min_max_scaler = min_max_scaler.fit(X)
        return min_max_scaler



    def process_dataset(self,dataset,scaler):

        X, Y = dataset

        X_train, X_val_and_test, Y_train, Y_val_and_test = train_test_split(X, Y, test_size=0.3)
        X_val, X_test, Y_val, Y_test = train_test_split(X_val_and_test, Y_val_and_test, test_size=0.5)

        X_val = scaler.transform(X_val)
        # this needs to be transformed seperately because they are passed directly to the model for validation
        
        return X_train, X_test, X_val, Y_train, Y_test, Y_val

    def create_and_train_model(self,csv_file):
        dataset = self.get_dataset(csv_file)
        scaler = self.get_scaler(dataset)
        processed_dataset = self.process_dataset(dataset,scaler)
        X_train, X_test, X_val, Y_train, Y_test, Y_val = processed_dataset

        # keras classifier wrapper class for pipeline use
        clf = KerasClassifier(
            self.get_model(),
            batch_size=32, 
            epochs=100,
        )

        # pipeline definition
        pipe = Pipeline([
            ('scaler', preprocessing.FunctionTransformer(scaler.transform)),
            ('clf',clf),
        ])

        
        # fit model
        pipe.fit(
            X_train,
            Y_train,
            clf__validation_data=(X_val, Y_val) # (model_name_in_pipeline)__validation_data
        )

        # evaluate model
        print(pipe.score(X_test, Y_test))

        # save pipe
        joblib.dump(pipe,os.path.join(sys.path[0],self.PIPE_SAV_FILE))


    def evaluate(self,csv_file):
        loaded_pipe = joblib.load(os.path.join(sys.path[0],self.PIPE_SAV_FILE))
        dataset = self.get_dataset(csv_file)
        scaler = self.get_scaler(dataset)
        processed_dataset = self.process_dataset(dataset,scaler)
        X_train, X_test, X_val, Y_train, Y_test, Y_val = processed_dataset

        return loaded_pipe.score(X_test,Y_test)

    def transaction_data_to_list(self,data):
        data = [
            data["avg_amount_days"],
            data["amount"],
            1 if data["is_declined"] else 0,
            data["number_declined_days"],
            1 if data["foreign_transaction"] else 0,
            1 if data["high_risk_countries"] else 0,
            data["daily_chbk_avg_amt"],
            data["sixm_avg_chbk_amt"],
            data["sixm_chbk_freq"],
        ]
        return data

    def predict(self,data):
        if type(data) != type([]):
            if type(data) != type(dict()):
                raise "Invalid data"
            data = self.transaction_data_to_list(data)
        loaded_pipe = joblib.load(os.path.join(sys.path[0],self.PIPE_SAV_FILE))
        prediction = loaded_pipe.predict([data])

        return prediction
    
