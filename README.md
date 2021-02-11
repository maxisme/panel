# packages
To add a new package run:
```shell
poetry add hypercorn
poetry export -f requirements.txt --output requirements.txt  
```

# k8s
To setup secrets run:
```shell
kubectl create secret generic panel --from-env-file .env
```
