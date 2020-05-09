Adjutant :robot:
========== 

Adjutant is an ability handler to communicate through Slack 


Available abilities
-------------------

- Waker: Enables WakeOnLan capabilities


How to get Adjutant
-------------------

``bash
    cd ~/Documents
    git clone https://github.com/acorbat/adjutant.git
    cd adjutant
    pip install .
``

Development guide
-----------------

``bash
    cd ADJUTANT_REPO_DIR
    pip install -e ".[test]"
``

You can run the tests

``bash
    cd ADJUTANT_REPO_DIR
    pytest
``

And to see a coverage report of the test suit

``bash
    cd ADJUTANT_REPO_DIR
    pytest --cov --cov-report html
    python -m http.server -d htmlcov
``