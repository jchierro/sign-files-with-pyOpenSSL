
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/da9e29eec06f44ed9dfca76f073f18b3)](https://www.codacy.com/app/jchierro/sign-files-with-pyOpenSSL?utm_source=github.com&utm_medium=referral&utm_content=jchierro/sign-files-with-pyOpenSSL&utm_campaign=badger)
[![Coverage Status](https://coveralls.io/repos/github/jchierro/sign-files-with-pyOpenSSL/badge.svg?branch=tests)](https://coveralls.io/github/jchierro/sign-files-with-pyOpenSSL?branch=tests)
[![Build Status](https://travis-ci.org/jchierro/sign-files-with-pyOpenSSL.svg?branch=master)](https://travis-ci.org/jchierro/sign-files-with-pyOpenSSL)

# Sign files with pyOpenSSL

Small web application to be able to digitally sign and verify a file using a digital certificate and the pyOpenSSL library. Developed with Python and Django.(https://sign-files.herokuapp.com/)

## Prerequisites
 - Django 1.11.5
 - pyOpenSSL 17.3.0
 - Have an certificate (http://www.fnmt.es/ | https://en.wikipedia.org/wiki/Self-signed_certificate)

## Features
 - Sign a file.
 - Verfify a file.
 
## Installation in development mode
 - Clone the repository (git clone).
 - Create an environment with virtualenv: python3 -m venv env.
 - Install packages from the requirements file: pip install -r requirements.txt
 - Starting the application: python3 manage.py runserver

## TODO
 - Limit the size of the files to be signed/verified.
