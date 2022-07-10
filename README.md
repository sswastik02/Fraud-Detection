# Fraud Detection using ML

## Backend

### Setup

#### <u>Clone Repository</u>
```sh
git clone https://github.com/sswastik02/Fraud-Detection.git

```

#### <u>Requirements</u>

You need `virtualenv` installed for this
```sh
# in the root of project
virtualenv -v venv
source venv/bin/activate
pip3 install -r requirements.txt

```

## ML Deployment
It contains the django application which hosts the machine learning models

#### <u>Environment Variables</u>
You need to define a `.env` file in the `backend/ML_Deployment` folder

```
SECRET_KEY=your-secret-key
DEBUG=True # False for production

```

an example can be found in `.env.example`

#### <u>ML</u>

You can either build a joblib file from the jupyter notebook and include it in `backend/ML_Deployment/ML/` or use the script present in `backend/ML_Deployment/ML/` to train and create joblib file using a csv


### Run

```sh
cd backend/ML_Deployment
python3 manage.py runserver

```
