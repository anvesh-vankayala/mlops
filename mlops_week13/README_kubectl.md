## kubectl :
- It is a command line interface to access the cluster.
- `alias kubectl="minikube kubectl --"` :kubectl on minikube is run with `minikube kubectl --` but we can create an alias to just use kubectl
- `kubectl get all` : lists all the parts of a Kubernetes cluster, including services, deployments, replica sets, and stateful sets
- `kubectl get all -n kube-system` : will list everything inside the kube-system namespace.
- `kubectl cluster-info` is a Kubernetes command used to display the addresses of the control plane and services within your cluster.

## creating deployment:
- `kubectl create -h` : kubectl create is used to create resources like Pods, Deployments, Services, ConfigMaps, etc., from a file or from specified arguments. The -h flag (which stands for "help") shows the documentation for the command, including its syntax, available flags.