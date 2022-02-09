from distutils.core import setup
setup(name='foo',
    version='1.0',
    description='',
    author='Simon Verret',
    author_email='verret.simon@gmail.com',
    url='https://github.com/simonverret/foo',
    packages=['foo'],
    install_requires=[
        'numpy',
        'matplotlib',
    ]
)

## It is recommended to keep packages at the top directory. Otherwise:
# package_dir={'projectNameGoesHere': 'src'}
## see: https://stackoverflow.com/questions/19602582/pip-install-editable-links-to-wrong-path/19917117#19917117