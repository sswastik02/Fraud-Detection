import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn import preprocessing

from keras.models import Sequential
from keras.layers import Dense

import pickle
import sys, os

MODEL_SAV_FILE = 'credit-card.sav'
CSV_FILE = 'creditcard-fraud.csv'

def create_model():
    df = pd.read_csv(os.path.join(sys.path[0],CSV_FILE))
    dataset = df.values
    print(df.shape)
    
    X = dataset[:,0:10] # Catergorical Data
    Y = dataset[:,10]  # Class Data

    min_max_scaler = preprocessing.MinMaxScaler()
    X_scale = min_max_scaler.fit_transform(X)

    # training data
    X_train, X_val_and_test, Y_train, Y_val_and_test = train_test_split(X_scale, Y, test_size=0.3)

    # testing data
    X_val, X_test, Y_val, Y_test = train_test_split(X_val_and_test, Y_val_and_test, test_size=0.5)


    # model architecture
    model = Sequential([
        Dense(32, activation='relu', input_shape=(10,)),
        Dense(32, activation='relu'),
        Dense(1, activation='sigmoid'),
    ])

    # compile model
    model.compile(
        optimizer='sgd',
        loss='binary_crossentropy',
        metrics=['accuracy']
    )

    # fit model
    hist = model.fit(
        X_train,
        Y_train,
        batch_size=32, epochs=100,
        validation_data=(X_val, Y_val)
    )

    # evaluate model
    print(model.evaluate(X_test, Y_test)[1])

    # save model
    pickle.dump(model,open(os.path.join(sys.path[0],MODEL_SAV_FILE),'wb'))


def predict_fraud():
    loaded_model = pickle.load(open(os.path.join(sys.path[0],MODEL_SAV_FILE),'rb'))
    prediction = loaded_model.predict([[
        0.64143747, 
        0.2034085 , 
        0.0911139 , 
        0. , 
        0. ,
        0. ,
        0. , 
        0. , 
        0. , 
        0. ,
    ]])

    return prediction


def main():
    if not os.path.exists(os.path.join(sys.path[0],MODEL_SAV_FILE)):
        create_model()
    else :
        op = input('\n\n credit card model already created\n Would you like to recreate (y/n)?')
        if op == 'y':
            create_model()
    print(predict_fraud())

if __name__ == "__main__":
    main()
    
