## kubectl :
- It is a command line interface to access the cluster.
- `alias kubectl="minikube kubectl --"` :kubectl on minikube is run with `minikube kubectl --` but we can create an alias to just use kubectl
- `kubectl get all` : lists all the parts of a Kubernetes cluster, including services, deployments, replica sets, and stateful sets, with in the default namespace.
- `kubectl get all -n kube-system` : will list everything inside the kube-system namespace.
- `kubectl cluster-info` is a Kubernetes command used to display the addresses of the control plane and services within your cluster.

## creating deployment:
- `kubectl create -h` : kubectl create is used to create resources like Pods, Deployments, Services, ConfigMaps, etc., from a file or from specified arguments. The -h flag (which stands for "help") shows the documentation for the command, including its syntax, available flags.

- `kubectl create deployment fastapi --image=tiangolo/uvicorn-gunicorn-fastapi:python3.11-2024-12-09` : For example Here, `fastapi` is the deployment name and image is `tiangolo/uvicorn-gunicorn-fastapi:python3.11-slim-2024-12-09`

- `kubectl get deployment`: To get deployments.
- `kubectl get pods` : gets the pods
- `kubectl get pods -o wide` :
    -o wide: The -o flag specifies the output format. By using wide, you get a more detailed view of the Pods, including additional columns like:
    - Node: The node (worker machine) where the pod is running.
    - IP: The internal IP address of the Pod.
    - Container IDs: The IDs of the containers running inside the pod.
    - Labels: Labels attached to the Pod.

- `kubectl describe pod <pod-name>` :  It gives all these info about the pod, namespace, Node with IP it belongs to, labels, IP of Pod, status, list of containers it have and their status, volume details etc.

- `kubectl delete deployment <deployment-name>` : deletes the deployment. 

- `kubectl delete -n <namespace> service <service-name>` : deletes the service, at the given namespace.

- `kubectl get namespaces` : gets the name spaces.

- `kubectl apply -f .` :  will look in the current directory for all files that match the pattern *.yaml or *.yml and apply them to the Kubernetes cluster. This is typically used when you want to apply multiple configuration files in one go (for example, if there are multiple Kubernetes resources like Deployments, Services, and ConfigMaps in the current directory).

- `kubectl get deployment <deployment-name> -o yaml` : The command will fetch the configuration of the Deployment named fastapi-deployment from the Kubernetes cluster and display it in YAML format.

- `kubectl get service <service-name> -o yaml` : The command will fetch the configuration of the service named fastapi-svc from the Kubernetes cluster and display it in YAML format.

- `kubectl delete -f <resources yaml>.yaml` : The command  is used to delete a Kubernetes resource (in this case, a Deployment) that is defined in the specified YAML. 

- `minikube service fastapi-svc` : To start the service.

### To activate conda package:
`source /Users/anvesh/opt/anaconda3/bin/activate`