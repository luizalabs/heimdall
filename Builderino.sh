python3 -m venv venv
source ./venv/bin/activate
pip install setuptools wheel twine
python setup.py sdist
twine upload dist/*
