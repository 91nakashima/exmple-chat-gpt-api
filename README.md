source .venv/bin/activate

deactivate

pip freeze > requirements.txt

pip install -r requirements.txt
