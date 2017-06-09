# oktasdk-python
=======================

This SDK allows managing an Okta instance via Python.

## Labs fork

This repository is a fork from the original oktasdk-python of Okta team.

## Run tests

The test strategy of the project uses a web server made in Node. The tests are written in Python and hit the endpoints serve by the Web server in Node.

- Run `npm install`

- Run `pip install -r requirements.txt`

- To run the tests `npm test`

## Add code with non tests (no recommended)

- Create a virtual environment with `python 3 -m venv myvenv`

- Activate the virtual environment `source myvenv/bin/activate`

- Install the dependencies `pip install -r requirements.txt`

- Execute the python console and import and call the code intended to be tested.
