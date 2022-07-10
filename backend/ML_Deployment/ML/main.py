from models.creditcard import CreditCard

import os, sys

def get_csv():
    if len(sys.argv) > 1 and sys.argv[1] != "":
        if(os.path.exists(sys.argv[1])):
            return sys.argv[1]
        print("",sys.argv[1], "not found")
        sys.exit(0)
    print("","Usage : python3 file.py path/to/csv")
    sys.exit(0)

def main():
    model = CreditCard()
    if not os.path.exists(os.path.join(sys.path[0],model.PIPE_SAV_FILE)):
        print(model.PIPE_SAV_FILE,"not found")
        CSV_FILE = get_csv()
        model.create_and_train_model(CSV_FILE)
    else :
        op = input('\n\n credit card model already created\n Would you like to recreate ? (y/n): ')
        if op == 'y':
            CSV_FILE = get_csv()
            model.create_and_train_model(CSV_FILE)

    op = input('\n do you want to evaluate ? (y/n)')
    if op == "y":
        CSV_FILE = get_csv()
        print("Model Score : ",model.evaluate(CSV_FILE))
    data = [
            537.2396194,
            537.2396194,
            0 , 
            1 ,
            0 ,
            0 , 
            0 , 
            0 , 
            0 , 
        ]  
    print("Prediction:",model.predict(data),end="\n")
    

if __name__ == "__main__":
    main()