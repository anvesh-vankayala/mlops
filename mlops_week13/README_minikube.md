# Kubernetes (K8S):

## Local setup
- `brew install minikube` To install minikube in mac local setup.
- `minikube start` : Launches the Minikube cluster.
    - `minikube start --driver=docker` for the first time, we need to docker as driver.
       Also ensure that docker is added to env path and docke is running.
- `minikube addons list` - To list all the addons. 
- `minikube delete --all` - To delete all minikube clusters.
- `minikube stop` : Stops the running Minikube cluster.
- `minikube status` : Checks the status of the Minikube cluster.
- `minikube dashboard` : Opens the Kubernetes dashboard in your web browser (if it's installed).