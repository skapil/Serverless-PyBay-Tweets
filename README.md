# Serverless Pybay Tweets
I build this project during my pybay2018 prepration talk.
Build this project to demonstrate how to build Flask app using Serverless Framework.
This repo has one url to see recent 20 pybay tweets and an api to see recent 5 tweets on paybay.

## Getting Started

``` git clone https://github.com/skapil/Serverless-PyBay-Tweets/new/master?readme=1```


### Prerequisites
Better to have a virtualenv for python. You can build the virtualenv using these steps:
https://docs.python-guide.org/dev/virtualenvs/

### Installing

You have to install nodejs and setup virtualenv. You can also follow below steps to setup the environment.
```
* brew install node OR install manually for mac/window/linux using these steps: https://nodejs.org/en/download/
* npm install -g serverless
* npm init
* Give project name and keep entering(anything else is not  manadatory)
* npm install serverless-python-requirements --save-dev
* npm install serverless-wsgi --save-dev
* pip install -r requirements.txt  => Install all the python requirement
```

## Deployment

* Make sure you have added your aws keys. You can try this command to add aws keys on your system:
```
serverless config credentials --provider aws --key <Your-AWS-Key> --secret <Your-Secret-Keys>
```

## Run Locally

This command will run the flask app locally. It should be running on https://localhost:8000
```sls wsgi serve -p 8000```

## Deploy as lambda

This command will deploy your code into AWS lambda and available for consumption.
```sls deploy```

## Authors

* **Sunil Kapil** 
