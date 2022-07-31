# Robust AI

## About the App

It is a E-Commerce Site that relies on ML Algoritms to detect fraudulent activity

## Objectives

## Technologies Used

* Frontend         : React, Redux
* Backend Services : Node, Express, DjangoRestFramework
* Machine Learning : Tensorflow, Keras, Scipy
* Blockchain       : Truffle Suite, Metamask, Solidity

## Contributors

* [Archit Lall](https://github.com/Architlall)
* [Epshita Chakravarty](https://github.com/docilefiasco)
* [Swastik Sarkar](https://github.com/sswastik02)
* [Vedika Agrawal](https://github.com/vedikaag78)

## Instructions

### Frontend

1. Clone the Respository
2. Install Yarn by running `npm i yarn --global`
3. Run `yarn` to install all dependencies in `client` folder
4. Start the server using `yarn start`

### Backend

#### <u>ML_Deployment</u>

1. Create Python Virtual Environment using `virtualenv` and activate it
2. Run `pip install -r requirements.txt`
3. Run `sudo apt install tesseract-ocr` for document verification
4. Run `cp .env.example .env`
5. Add your own Mongo Database URI to .env
6. `pytohn3 manage.py makemigrations`
7. `python3 manage.py migrate`
8. `python3 manage.py createsuperuser` to create admin user
9. `python3 manage.py runserver` to run the server
10. Create api keys by going to `http://localhost:8000/admin`, you will need this in the node application

#### <u>Server</u>

1. `npm install`
2. Get Cloudinary API key from cloudinary website
3. Get API Keys from python backend
4. Get MongoDB Database URI from mongodb
5. `cp .env.example .env`
6. Add the relevant values to `.env`
7. `npm start`

### <u>Machine Learning Models</u>
1. Run `ML/bin/main.py` with relevant csv files from `datasets` folder to train the model
2. `sudo apt install tesseract-oct`

### <u>Blockchain</u>

1. `npm install -g truffle` For truffle suite blockchain
2. On Chrome/Firefox/Brave : 
   1. Go to the extensions page of your browser and install the metamask plugin, click [here](https://chrome.google.com/webstore/detail/metamask/nkbihfbeogaeaoehlefnkodbefgpgknn).
   2. On installation the user will be redirected to a setup page and the user has to choose a password and a recovery phrase.



