import os
from init import get_csv

def exec_model(model,data,temp=False):
    if not os.path.exists(model.PIPE_SAV_FILE):
        print(model.PIPE_SAV_FILE,"not found")
        if temp : 
            model.create_and_train_model()
        else :
            CSV_FILE = get_csv()
            model.create_and_train_model(CSV_FILE)
    else :
        op = input('\n\n model already created\n Would you like to recreate ? (y/n): ')
        if op == 'y':
            if temp:
                model.create_and_train_model()
            else:
                CSV_FILE = get_csv()
                model.create_and_train_model(CSV_FILE)

    op = input('\n do you want to evaluate ? (y/n)')
    if op == "y":
        if temp:
            print("Model Score : ", model.evaluate())
        else:
            CSV_FILE = get_csv()
            print("Model Score : ",model.evaluate(CSV_FILE))
    print("Prediction:",model.predict(data),end="\n")