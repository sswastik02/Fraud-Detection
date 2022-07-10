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
virtualenv -v venv
source venv/bin/activate
pip3 install -r requirements.txt

```

### <u>Environment Variables</u>
You need to define a `.env` file in the `backend` folder

```
SECRET_KEY=your-secret-key
DEBUG=True # False for production
ML_SAVE_DIR=ML # Dir where the pipes will be saved after fitting

```

an example can be found in `.env.example`

#### <u>ML</u>

You can either build a joblib file from the jupyter notebook and include it in `backend/ML/` or use the script present in `backend/ML/` to train and create joblib file using a csv

### <u>Server</u>

```sh
cd backend
# backend does not commit data to a database

# optional create admin
python3 manage.py createsuperuser

```

### Run

```sh
python3 manage.py runserver

```
