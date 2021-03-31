[![Python application test with Github Actions](https://github.com/lukasgejdos/devops-nano-project2/actions/workflows/pythonapp.yml/badge.svg)](https://github.com/lukasgejdos/devops-nano-project2/actions/workflows/pythonapp.yml)

# Overview

This project is Flask application for making predictions of housing prices in Boston according to several features - f.e. average rooms in a home, data about highway access, teacher-to-pupil ratios, etc. Application uses pre-trained `sklearn` model and as a Machine Learning (ML) API is able to respond with predicted price. 

Application supports following endpoints:

`POST` method to `/predict` endpoint with example JSON input:
```json
{
    "CHAS": {
      "0": 0
    },
    "RM": {
      "0": 6.575
    },
    "TAX": {
      "0": 296.0
    },
    "PTRATIO": {
      "0": 15.3
    },
    "B": {
      "0": 396.9
    },
    "LSTAT": {
      "0": 4.98
    }
}
```
will respond with following JSON output:
```json
{ "prediction": [ 20.35373177134412 ] }
```

## Project Plan
You can find spreadsheet with project plan on this link:
[📝 Project management](https://github.com/lukasgejdos/devops-nano-project2/files/6234685/project-management.xlsx)

Trello board for the project is located here:
[📅 Project board](https://trello.com/b/98M5XAQA/project-2)

## Instructions

### Architectural Diagram
![architecture-diagram](https://user-images.githubusercontent.com/9935013/113122389-dd506700-9213-11eb-9c0e-08bff5e14329.png)

### Instructions for running the Python project in Azure Cloud Shell
1. Open Azure Cloud Shell session
2. Clone project into your working directory:
```sh
git clone git@github.com:lukasgejdos/devops-nano-project2.git 
```
> ![git-clone](https://user-images.githubusercontent.com/9935013/113044335-ca9b4b00-919d-11eb-92b8-e866835bb987.png)
> 
> Project cloned into Azure Cloud Shell
3. Change directory to cloned project `devops-nano-project2`:
```sh
cd devops-nano-project2
```
4. To enable virtual environment, run following command from `Makefile` and `source` command:
```sh
make setup
source ~/.udacity-devops/bin/activate
```
5. To install dependencies, lint code and run tests, use following command:
```sh
make all
```
> ![make-all-tests](https://user-images.githubusercontent.com/9935013/113044372-d6870d00-919d-11eb-8c81-cfedf1dadc13.png)
> 
> Passing tests that are displayed after running the `make all` command from the `Makefile`
6. Start the application:
```sh
python3 app.py
```
Application should start serving on port `5000`. In new Azure Cloud Shell session, you can reach it on http://localhost:5000. To test it, execute following script:
```sh
sh ./make_prediction.sh
```
> ![azure-cloud-shell-test-run1](https://user-images.githubusercontent.com/9935013/113122432-e93c2900-9213-11eb-8f7f-7fa049ff70ad.png)
> ![azure-cloud-shell-test-run2](https://user-images.githubusercontent.com/9935013/113122434-e9d4bf80-9213-11eb-9425-778465037668.png)
> 
> Output of a test run
7. You can deploy application to Azure App Service with following command:
```azurecli
az webapp up -n flaskml-lg --sku F1
```
> ![project-running-azure-app-service](https://user-images.githubusercontent.com/9935013/113045994-cbcd7780-919f-11eb-8027-34ec64069a00.png)
> 
> Project running on Azure App Service

After successful deployment you can browse to app ULR [https://flaskml-lg.azurewebsites.net](https://flaskml-lg.azurewebsites.net) and check, if it is running:
> ![running-app-from-code](https://user-images.githubusercontent.com/9935013/113055330-c3c70500-91aa-11eb-9e6b-2f718255b6ee.png)

### Instructions for CI/CD
1. If you would like to contribute, you need to setup f.e. `ssh` access to repository. First, create your ssh key pair:
```sh
ssh-keygen -t ed25519 -C "<YOUR EMAIL>"
cat ~/.ssh/id_ed25519.pub
```
2. Send output of the `cat` command to me :)
3. After successful setup, you can commit and push to repository (f.e. change message on homepage). After push to master branch, there is a GitHub action which lints and tests code. 
> ![git-actions-build](https://user-images.githubusercontent.com/9935013/113054608-e60c5300-91a9-11eb-8ab4-2f8eeb1a06cb.png)
> 
> Passing GitHub Actions build

4. After successful tests, deployment to Azure App Service via Azure Pipelines is triggered:
> ![ado-build](https://user-images.githubusercontent.com/9935013/113045943-b8221100-919f-11eb-97da-1cf0a7fdbf3c.png)
> ![ado-deploy](https://user-images.githubusercontent.com/9935013/113045950-bb1d0180-919f-11eb-92c2-f4beadbf7587.png)
> 
> Successful deploy of the project in Azure Pipelines

[Official documentation of Python Webapp CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

5. After successful deployment, app should be running on [https://flaskml-lg.azurewebsites.net](https://flaskml-lg.azurewebsites.net) and you can see the change in the message:
> ![running-app-from-ado](https://user-images.githubusercontent.com/9935013/113055323-c32e6e80-91aa-11eb-881d-6260acc96351.png)
> 
> Running Azure App Service from Azure Pipelines after automatic deployment

6. Next, you can check if prediction is working. Open Azure Cloud Shell session, cd to `devops-nano-project2` and execute following script:
```sh
sh ./make_predict_azure_app.sh
```
It should output something like:  
> ![make-predict-output](https://user-images.githubusercontent.com/9935013/113045985-c8d28700-919f-11eb-9a11-cd9b91e82077.png)
> 
> Successful prediction from deployed flask app in Azure Cloud Shell

7. To see app logs, you can browse to this URL: [https://flaskml-lg.scm.azurewebsites.net/api/logs/docker](https://flaskml-lg.scm.azurewebsites.net/api/logs/docker).
> ![logs](https://user-images.githubusercontent.com/9935013/113045956-bfe1b580-919f-11eb-93b3-8a13fbe201ef.png)
> 
> Output of streamed log files from deployed application


## Enhancements

There is a lot of space for improvements:
* Implement monitoring f.e. using Azure Monitor
* Improve logging using Azure App Insights or Log Analytics, implement Alerts 
* Performance tests	
* Consider releasing Docker / K8S PoC to production
* Create nice Vue frontend

## Demo 

You can watch demo here (preferably at 1.25 speed :)
📺 [https://youtu.be/_TC8oVeOGuI](https://youtu.be/_TC8oVeOGuI)

