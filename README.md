# Document-Scan


### Project Structure

```

Flask Application

├───app
│   │   .gitignore
│   │   main.py
│   │   requirements.txt
│   │
│   ├───data
│   │       bad_privacy.txt
│   │       good_privacy.txt
│   │
│   ├───model
│   │       logistic_regression.pkl
│   │       vectorizer.pkl
│   │
│   ├───script
│   │   │   clean_data.py
│   │   │   model.py
│   │   │   scrape.py
│   │   │   __init__.py
│   │
│   ├───static
│   │   │   design.css
│   │   │
│   │   └───bootstrap
│   │       └───css
│   │               bootstrap.css
│   │               bootstrap.css.map
│   │               bootstrap.min.css
│   │               bootstrap.min.css.map
│   │
│   ├───templates
│   │       home.html

Jupyter Notebook
└───jupyter-notebooks
    │   getting_privacy_text.ipynb
    │   privacy_policy_predictor.ipynb
    │
    │
    ├───Data
    │       bad_privacy.txt
    │       Data.csv
    │       good_privacy.txt
    │
    └───Model
            logistic_regression.pkl
            vectorizer.pkl
```


### Run the Flask Application

Make sure you have python3 and pip installed


Create and activate virtual environment using virtualenv
```bash
$ python -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies

```bash
pip install -r requirements.txt
```

## Usage


Start flask server
```bash
$ export FLASK_APP=main.py
$ flask run
```
Note: Use set inplace of export in windows

