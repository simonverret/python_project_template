# Foo (template project)

## Install 
Create a virtual environment (optional)

    pip install virtualenv
    virtualenv env
    source env/bin/activate

Install foo and its requirements (developper install)

    pip install -e .

## Tests
Install dependencies and run the tests

    pip install pytest pytest-mock
    pytest

View tests coverage

    pip install pytest-cov
    pytest --cov=foo

Navigate coverage details

    coverage html
    open htmlcov/index.html

## Documentation
Build and navigate the Sphinx documentation

    pip install sphinx furo
    cd docs
    make html
    open build/html/index.html

Docstrings are added to the documentation automatically using the `napoleon` extension to Sphinx (to support Google and Numpy style docstrings). After modifying the code, you can regenerate the automatic pages. This will overwrite any edit to the documentation.

    cd docs
    sphinx-apidoc -f -o source ..;

## License
This template project is in the public domain (see the `LICENSE` file). If you edit this project, you should change the license if you don't want your code to end up in the public domain.

