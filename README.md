# Foo

## License

This example project is in the public domain (see the `LICENSE` file). If you edit this project, you should change the license if you don't want your code to end up in the public domain.


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
Build and navigate the documentation

    cd docs
    make html
    open build/html/index.html

### From scratch
At first, there is nothing in a `docs/` directory. Here are the steps used to initialize the documentation

    pip install sphinx sphinx-rtd-theme
    sphinx-quickstart 
    
In the prompt choose separate source and build directories, and follow instruction.
To obtain the "read the docs" theme, modify `docs/source/conf.py` as

    import sphinx_rtd_theme

    extensions = [
        ...
        'sphinx_rtd_theme',
    ]

    html_theme = "sphinx_rtd_theme"

To enable automatic documentation from docstrings, modify `docs/source/conf.py` as:

    extensions = [
        'sphinx.ext.autodoc',
    ]

Then, add the desired module to the docs. You can make a new page by modifying `docs/source/index.rst` as:

    .. toctree::
       :maxdepth: 2

       newpage

which requries to add `docs/source/newpage.rst` file containing, for example:

    utils
    ===============================

    .. toctree::
       :maxdepth: 2

    .. automodule:: foo.utils
       :members:


For more information, see
[read the docs](https://readthedocs.org), 
[sphinx](https://www.sphinx-doc.org/en/master/usage/configuration.html), andthe 
[read-the-docs sphinx theme](https://sphinx-rtd-theme.readthedocs.io/en/latest/installing.html).
