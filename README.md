# projectNameGoesHere

## Install 

Create a virtual environment (optional)

    pip install virtualenv
    virtualenv env
    source env/bin/activate

Install projectNameGoesHere and its requirements (developper install)

    pip install -e .


## Tests
Install dependencies and run the tests

    pip install pytest pytest-mock
    pytest

View tests coverage

    pip install pytest-cov
    pytest --cov=projectNameGoesHere

Naviguate coverage details

    coverage html
    open htmlcov/index.html


## Documentation
Install dependencies and build the documentation

    pip install sphinx sphinx-rtd-theme
    cd docs
    make html

Open `docs/build/html/index.html`. If there are no files in the `docs/` directory, first run

    sphinx-quickstart 
    
Choose separate source and build directories, and follow instructions. Change line 50 in `docs/conf.py` to use theme

    html_theme = 'sphinx-rtd-theme'


## License
[Unlicense](https://unlicense.org)