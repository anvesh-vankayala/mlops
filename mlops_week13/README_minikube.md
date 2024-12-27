# Kubernetes (K8S):

## Local setup
- `brew install minikube` To install minikube in mac local setup.
- `minikube start` : Launches the Minikube cluster.
    - `minikube start --driver=docker` for the first time, we need to docker as driver.
       Also ensure that docker is added to env path and docker is running.
    - `export PATH="$PATH:/Applications/Docker.app/Contents/Resources/bin/"` if docker path is not added.
- `minikube addons list` - To list all the addons. 
- `minikube delete --all` - To delete all minikube clusters.
- `minikube stop` : Stops the running Minikube cluster.
- `minikube status` : Checks the status of the Minikube cluster.
- `minikube dashboard` : Opens the Kubernetes dashboard in your web browser (if it's installed).
- `eval $(minikube docker-env -u)` : To switch to docker demon env.
- `eval $(minikube docker-env)` : to switch to minikube's docker env.
- `minikube tunnel` : Minikube tunnel is a command that creates a network tunnel to your Minikube cluster, allowing you to access services that are exposed via LoadBalancer type services. When you run minikube tunnel, it sets up a local network route to the Minikube cluster, enabling you to access these services using their assigned external IP addresses.
- `minikube image load classifier-k8s:latest` : To load the image to minikube.