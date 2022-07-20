import os, sys

fpath = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(fpath)
# Adding access to super parent directory

from init import make_dirs
from model_executor import exec_model

from models.creditcard import CreditCard
from models.phishing_site import PhishingSite
from models.phishing_url import PhishingURL
from paths import PIPES_DIR, TEMP_DIR  

def main():
    make_dirs([PIPES_DIR,TEMP_DIR])

    # model = CreditCard()
    # transac_data = [
    #         537.2396194,
    #         537.2396194,
    #         0 , 
    #         1 ,
    #         0 ,
    #         0 , 
    #         0 , 
    #         0 , 
    #         0 , 
    #     ]  
    # exec_model(model,transac_data)

    # model = PhishingSite()
    # url = "https://www.google.com/"
    # exec_model(model,url,temp=True)

    model = PhishingURL()
    url = "https://www.google.com/"
    exec_model(model,url)
    

if __name__ == "__main__":
    main()