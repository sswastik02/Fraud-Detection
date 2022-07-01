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

#### <u>ML</u>

You can either build a pickle file from the jupyter notebook and include it in `backend/ML/` or use the script present in `backend/ML` to train and create pickle file using a csv

### <u>Server</u>

```sh
cd backend
python3 manage.py makemigrations
python3 manage.py migrate

# optional create admin
python3 manage.py createsuperuser

```

### Run

```sh
python3 manage.py runserver

```
