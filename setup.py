from setuptools import setup, find_packages
# To use a consistent encoding
#from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open( path.join(path.abspath(path.dirname(__file__)) , 'README.md' ), encoding = 'utf-8') as f:
    long_description = f.read()

setup(
    name = 'vernam',
    version = '1.0.0',

    description = 'Vernam cipher',
    long_description = long_description,

    url = 'https://github.com/roysoup/vernam',

    author = 'Roy Siu',
    author_email = '',

    license = 'MIT',

    classifiers = [
        'Development Status :: 4 - Beta'
        #'Development Status :: 5 - Production/Stable'
    ],
    
    install_requires = [''],
)