# Docker / Kubernetes PoC

For better integration of Flask app as microservice in the suite, we have created dockerized version and Kubernetes config.

## Infrastructure

First, you need to setup Kubernetes cluster. For Kubernetes managed service in Azure, check following guide: 
[Tutorial: Deploy an Azure Kubernetes Service (AKS) cluster](https://docs.microsoft.com/en-us/azure/aks/tutorial-kubernetes-deploy-cluster)

Alongside, you need Container Registry in Azure (or alternatively other option like Docker Hub). For Azure Container Registry, check following:
[Tutorial: Deploy and use Azure Container Registry](https://docs.microsoft.com/en-us/azure/aks/tutorial-kubernetes-prepare-acr)

## Build and run

When ACR and AKS are ready, let's build it.

1. First, we need to build docker image from the source. In Azure Cloud Shell, cd to source `devops-nano-project2` and run following command:
```azurecli
az acr build --image flask:1.0.0 --registry <YOUR_ACR_NAME>.azurecr.io .
```
where you replaced <YOUR_ACR_NAME> with ACR name just created.
2. After successful push to registry, let's deploy it to our cluster. First, we need to modify `deploy.yaml` and replace <YOUR_ACR> placeholder with ACR name just created. 
3. Next, we need to get access to AKS from Azure Cloud Shell. We can do it with following Azure CLI command:
```azurecli
az aks get-credentials --resource-group <YOUR_AKS_RESOURCE_GROUP> --name <YOUR_AKS_NAME> --admin
```
where you replaced <YOUR_AKS_RESOURCE_GROUP> and <YOUR_AKS_NAME> with actual values of your AKS.
5. Finally, run following `kubectl` command:
```sh
kubectl apply -f deploy.yaml
```
6. After deployment and service creation, check if application Pod is running with the command:
```sh
kubectl get po
```

## Verify app is responding

To verify, if application running in Pod is responding, map remote port to local one:
```sh
kubectl port-forward svc/flask-app 5000:5000
```
and in new Azure Cloud Shell session, try to execute following script:
```sh
sh .\make_prediction.sh
```

> Output should be like:
>
> ![kubernetes-port-forward](https://user-images.githubusercontent.com/9935013/113152152-1dc0dc80-9236-11eb-94af-1867c76ed1c7.png)

## 🎉👏
