# Robust AI

## About the App

The MERN-based web app replicates any web app on the internet that facilitates online transactions and requires users to submit personal information.
This web app uses trained Machine Learning Models, applied on top of the base of the application that aids fraud detection and online reliability.
The application additionally ensures maximum security from data breaches using blockchain technology to secure transaction data.

## Objectives
Our objective is to find a solution that helps to accurately achieve data and financial fraud detection and to employ good data practices to secure it from exploitation. We aim to build a socially inclusive solution that is accessible to all sorts of people, from senior citizens to differently-abled, making sure that technology is not driven by an ableist ideology.

As a web application, it will facilitate online transactions and requires users to submit personal information.This app will have Machine Learning Models applied on top of the base of the application to reduce the risks of fraud and increase user reliability. When a person makes a certain transaction, the Model trained to detect net banking fraud will rely on information such as the previous patterns of user transactions, if they are making transactions from a high-risk country, the number of transactions, etc. This model uses a Convoluted Neural Network to provide maximum accuracy and recall with respect to other classification algorithms. The app will further store data on Blockchain to ensure maximum security and prevent data breaches.


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

### **Ganache Local Development Blockchain**
The dependency is a personal blockchain, which is a local development blockchain that can be used to mimic the behavior of a public blockchain. We recommend using [Ganache](https://www.trufflesuite.com/ganache) as your personal blockchain for Ethereum development. It will allow you to deploy smart contracts, develop applications, and run tests. It is available on Windows, Mac, and Linux as a desktop application and a command-line tool !

Download it by clicking [here](https://www.trufflesuite.com/ganache).  *(For both Windows and Linux)*

##### **For Linux Users :**

*Once the download is complete, go to the folder where you have downloaded the file and open the terminal and type the following to make the file executable :*
```
Chmod a+x <filename.AppImage>
```
### **Truffle Framework**
Now let's install the [Truffle Framework](https://www.trufflesuite.com/docs/truffle/overview), which provides a suite of tools for developing Ethereum smart contracts with the Solidity programming language.
##### **For Windows Users :**
Go to your cmd and type :
```
npm install -g truffle
```
##### **For Linux Users :**
Go to your terminal and type :
```
$ sudo npm install -g truffle
```
<br>

### **Metamask Wallet**

For this project, we would require an ethereum wallet, and here we will use the popular open-source wallet metamask.

**On chrome/firefox/brave :** *(It is recommended that you use Brave browser)*

1. Go to the extensions page of your browser and install the metamask plugin, click [here](https://chrome.google.com/webstore/detail/metamask/nkbihfbeogaeaoehlefnkodbefgpgknn).
2. On installation the user will be redirected to a setup page and the user has to choose a password and a recovery phrase.




