## Output of the project:
kubectl describe <your_deployment>
kubectl describe <your_pod>
kubectl describe <your_ingress>
kubectl top pod
kubectl top node
kubectl get all -o yaml
 
## Output of the project:
`kubectl describe deployment.apps/classifer-deployment`
Name:                   classifer-deployment
Namespace:              default
CreationTimestamp:      Fri, 27 Dec 2024 20:25:00 +0530
Labels:                 app=classifier
Annotations:            deployment.kubernetes.io/revision: 1
Selector:               app=classifier
Replicas:               2 desired | 2 updated | 2 total | 2 available | 0 unavailable
StrategyType:           RollingUpdate
MinReadySeconds:        0
RollingUpdateStrategy:  25% max unavailable, 25% max surge
Pod Template:
  Labels:  app=classifier
  Containers:
   classifier:
    Image:         classifier-k8s:latest
    Port:          7860/TCP
    Host Port:     0/TCP
    Environment:   <none>
    Mounts:        <none>
  Volumes:         <none>
  Node-Selectors:  <none>
  Tolerations:     <none>
Conditions:
  Type           Status  Reason
  ----           ------  ------
  Available      True    MinimumReplicasAvailable
  Progressing    True    NewReplicaSetAvailable
OldReplicaSets:  <none>
NewReplicaSet:   classifer-deployment-5545798ff5 (2/2 replicas created)
Events:
  Type    Reason             Age   From                   Message
  ----    ------             ----  ----                   -------
  Normal  ScalingReplicaSet  59m   deployment-controller  Scaled up replica set classifer-deployment-5545798ff5 to 2

`kubectl describe pod/classifer-deployment-5545798ff5`
Name:             classifer-deployment-5545798ff5-8zknf
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Fri, 27 Dec 2024 20:25:00 +0530
Labels:           app=classifier
                  pod-template-hash=5545798ff5
Annotations:      <none>
Status:           Running
IP:               10.244.0.66
IPs:
  IP:           10.244.0.66
Controlled By:  ReplicaSet/classifer-deployment-5545798ff5
Containers:
  classifier:
    Container ID:   docker://278f7e32812eec07039f9c6cedd84f7939705628a62d11e8a104b5dc753c98ff
    Image:          classifier-k8s:latest
    Image ID:       docker://sha256:edffefa162a2736c3b36eeb17c0a452f1b1e0cdfe1bb6074778442f41d11f68e
    Port:           7860/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Fri, 27 Dec 2024 20:25:01 +0530
    Ready:          True
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-cbttx (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True 
  Initialized                 True 
  Ready                       True 
  ContainersReady             True 
  PodScheduled                True 
Volumes:
  kube-api-access-cbttx:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age   From               Message
  ----    ------     ----  ----               -------
  Normal  Scheduled  61m   default-scheduler  Successfully assigned default/classifer-deployment-5545798ff5-8zknf to minikube
  Normal  Pulled     61m   kubelet            Container image "classifier-k8s:latest" already present on machine
  Normal  Created    61m   kubelet            Created container classifier
  Normal  Started    61m   kubelet            Started container classifier


`kubectl describe ingress classifier-ingress`
Name:             classifier-ingress
Labels:           <none>
Namespace:        default
Address:          192.168.49.2
Ingress Class:    nginx
Default backend:  <default>
Rules:
  Host              Path  Backends
  ----              ----  --------
  anvesh.vankayala  
                    /   classifier-service:80 (10.244.0.66:7860,10.244.0.67:7860)
Annotations:        nginx.ingress.kubernetes.io/affinity: cookie
                    nginx.ingress.kubernetes.io/affinity-mode: balanced
                    nginx.ingress.kubernetes.io/session-cookie-expires: 172800
                    nginx.ingress.kubernetes.io/session-cookie-max-age: 172800
                    nginx.ingress.kubernetes.io/session-cookie-name: INGRESSCOOKIE
Events:
  Type    Reason  Age                From                      Message
  ----    ------  ----               ----                      -------
  Normal  Sync    66m (x2 over 67m)  nginx-ingress-controller  Scheduled for sync

`kubectl top pod`
NAME                                    CPU(cores)   MEMORY(bytes)   
classifer-deployment-5545798ff5-8zknf   13m          1079Mi          
classifer-deployment-5545798ff5-scfbf   13m          1026Mi          

`kubectl top node`
NAME       CPU(cores)   CPU(%)   MEMORY(bytes)   MEMORY(%)   
minikube   147m         1%       2778Mi          35%   

`kubectl get all -o yaml`

apiVersion: v1
items:
- apiVersion: v1
  kind: Pod
  metadata:
    creationTimestamp: "2024-12-27T14:55:00Z"
    generateName: classifer-deployment-5545798ff5-
    labels:
      app: classifier
      pod-template-hash: 5545798ff5
    name: classifer-deployment-5545798ff5-8zknf
    namespace: default
    ownerReferences:
    - apiVersion: apps/v1
      blockOwnerDeletion: true
      controller: true
      kind: ReplicaSet
      name: classifer-deployment-5545798ff5
      uid: 50418064-e514-4c21-a703-bf7d08d453d0
    resourceVersion: "94483"
    uid: d0ba8cc8-bee5-4f62-82f1-31ea0779e5fb
  spec:
    containers:
    - image: classifier-k8s:latest
      imagePullPolicy: Never
      name: classifier
      ports:
      - containerPort: 7860
        protocol: TCP
      resources: {}
      terminationMessagePath: /dev/termination-log
      terminationMessagePolicy: File
      volumeMounts:
      - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
        name: kube-api-access-cbttx
        readOnly: true
    dnsPolicy: ClusterFirst
    enableServiceLinks: true
    nodeName: minikube
    preemptionPolicy: PreemptLowerPriority
    priority: 0
    restartPolicy: Always
    schedulerName: default-scheduler
    securityContext: {}
    serviceAccount: default
    serviceAccountName: default
    terminationGracePeriodSeconds: 30
    tolerations:
    - effect: NoExecute
      key: node.kubernetes.io/not-ready
      operator: Exists
      tolerationSeconds: 300
    - effect: NoExecute
      key: node.kubernetes.io/unreachable
      operator: Exists
      tolerationSeconds: 300
    volumes:
    - name: kube-api-access-cbttx
      projected:
        defaultMode: 420
        sources:
        - serviceAccountToken:
            expirationSeconds: 3607
            path: token
        - configMap:
            items:
            - key: ca.crt
              path: ca.crt
            name: kube-root-ca.crt
        - downwardAPI:
            items:
            - fieldRef:
                apiVersion: v1
                fieldPath: metadata.namespace
              path: namespace
  status:
    conditions:
    - lastProbeTime: null
      lastTransitionTime: "2024-12-27T14:55:02Z"
      status: "True"
      type: PodReadyToStartContainers
    - lastProbeTime: null
      lastTransitionTime: "2024-12-27T14:55:00Z"
      status: "True"
      type: Initialized
    - lastProbeTime: null
      lastTransitionTime: "2024-12-27T14:55:02Z"
      status: "True"
      type: Ready
    - lastProbeTime: null
      lastTransitionTime: "2024-12-27T14:55:02Z"
      status: "True"
      type: ContainersReady
    - lastProbeTime: null
      lastTransitionTime: "2024-12-27T14:55:00Z"
      status: "True"
      type: PodScheduled
    containerStatuses:
    - containerID: docker://278f7e32812eec07039f9c6cedd84f7939705628a62d11e8a104b5dc753c98ff
      image: classifier-k8s:latest
      imageID: docker://sha256:edffefa162a2736c3b36eeb17c0a452f1b1e0cdfe1bb6074778442f41d11f68e
      lastState: {}
      name: classifier
      ready: true
      restartCount: 0
      started: true
      state:
        running:
          startedAt: "2024-12-27T14:55:01Z"
      volumeMounts:
      - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
        name: kube-api-access-cbttx
        readOnly: true
        recursiveReadOnly: Disabled
    hostIP: 192.168.49.2
    hostIPs:
    - ip: 192.168.49.2
    phase: Running
    podIP: 10.244.0.66
    podIPs:
    - ip: 10.244.0.66
    qosClass: BestEffort
    startTime: "2024-12-27T14:55:00Z"
- apiVersion: v1
  kind: Pod
  metadata:
    creationTimestamp: "2024-12-27T14:55:00Z"
    generateName: classifer-deployment-5545798ff5-
    labels:
      app: classifier
      pod-template-hash: 5545798ff5
    name: classifer-deployment-5545798ff5-scfbf
    namespace: default
    ownerReferences:
    - apiVersion: apps/v1
      blockOwnerDeletion: true
      controller: true
      kind: ReplicaSet
      name: classifer-deployment-5545798ff5
      uid: 50418064-e514-4c21-a703-bf7d08d453d0
    resourceVersion: "94488"
    uid: dd7a00e6-98e8-4887-b825-5ab21f177036
  spec:
    containers:
    - image: classifier-k8s:latest
      imagePullPolicy: Never
      name: classifier
      ports:
      - containerPort: 7860
        protocol: TCP
      resources: {}
      terminationMessagePath: /dev/termination-log
      terminationMessagePolicy: File
      volumeMounts:
      - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
        name: kube-api-access-257v9
        readOnly: true
    dnsPolicy: ClusterFirst
    enableServiceLinks: true
    nodeName: minikube
    preemptionPolicy: PreemptLowerPriority
    priority: 0
    restartPolicy: Always
    schedulerName: default-scheduler
    securityContext: {}
    serviceAccount: default
    serviceAccountName: default
    terminationGracePeriodSeconds: 30
    tolerations:
    - effect: NoExecute
      key: node.kubernetes.io/not-ready
      operator: Exists
      tolerationSeconds: 300
    - effect: NoExecute
      key: node.kubernetes.io/unreachable
      operator: Exists
      tolerationSeconds: 300
    volumes:
    - name: kube-api-access-257v9
      projected:
        defaultMode: 420
        sources:
        - serviceAccountToken:
            expirationSeconds: 3607
            path: token
        - configMap:
            items:
            - key: ca.crt
              path: ca.crt
            name: kube-root-ca.crt
        - downwardAPI:
            items:
            - fieldRef:
                apiVersion: v1
                fieldPath: metadata.namespace
              path: namespace
  status:
    conditions:
    - lastProbeTime: null
      lastTransitionTime: "2024-12-27T14:55:02Z"
      status: "True"
      type: PodReadyToStartContainers
    - lastProbeTime: null
      lastTransitionTime: "2024-12-27T14:55:00Z"
      status: "True"
      type: Initialized
    - lastProbeTime: null
      lastTransitionTime: "2024-12-27T14:55:02Z"
      status: "True"
      type: Ready
    - lastProbeTime: null
      lastTransitionTime: "2024-12-27T14:55:02Z"
      status: "True"
      type: ContainersReady
    - lastProbeTime: null
      lastTransitionTime: "2024-12-27T14:55:00Z"
      status: "True"
      type: PodScheduled
    containerStatuses:
    - containerID: docker://e5f71ce55ff2863b5a91855ed1cd66f2c967b8e9794c620ce85cbb5ff713e0f1
      image: classifier-k8s:latest
      imageID: docker://sha256:edffefa162a2736c3b36eeb17c0a452f1b1e0cdfe1bb6074778442f41d11f68e
      lastState: {}
      name: classifier
      ready: true
      restartCount: 0
      started: true
      state:
        running:
          startedAt: "2024-12-27T14:55:01Z"
      volumeMounts:
      - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
        name: kube-api-access-257v9
        readOnly: true
        recursiveReadOnly: Disabled
    hostIP: 192.168.49.2
    hostIPs:
    - ip: 192.168.49.2
    phase: Running
    podIP: 10.244.0.67
    podIPs:
    - ip: 10.244.0.67
    qosClass: BestEffort
    startTime: "2024-12-27T14:55:00Z"
- apiVersion: v1
  kind: Service
  metadata:
    annotations:
      kubectl.kubernetes.io/last-applied-configuration: |
        {"apiVersion":"v1","kind":"Service","metadata":{"annotations":{},"name":"classifier-service","namespace":"d
efault"},"spec":{"ports":[{"port":80,"protocol":"TCP","targetPort":7860}],"selector":{"app":"classifier"}}}            creationTimestamp: "2024-12-27T14:55:00Z"
    name: classifier-service
    namespace: default
    resourceVersion: "94470"
    uid: 5b021b58-6778-4627-9034-0fd24faced41
  spec:
    clusterIP: 10.101.158.167
    clusterIPs:
    - 10.101.158.167
    internalTrafficPolicy: Cluster
    ipFamilies:
    - IPv4
    ipFamilyPolicy: SingleStack
    ports:
    - port: 80
      protocol: TCP
      targetPort: 7860
    selector:
      app: classifier
    sessionAffinity: None
    type: ClusterIP
  status:
    loadBalancer: {}
- apiVersion: v1
  kind: Service
  metadata:
    creationTimestamp: "2024-12-15T06:57:46Z"
    labels:
      component: apiserver
      provider: kubernetes
    name: kubernetes
    namespace: default
    resourceVersion: "197"
    uid: c1695a87-9d1f-4443-afa2-f50baadf8406
  spec:
    clusterIP: 10.96.0.1
    clusterIPs:
    - 10.96.0.1
    internalTrafficPolicy: Cluster
    ipFamilies:
    - IPv4
    ipFamilyPolicy: SingleStack
    ports:
    - name: https
      port: 443
      protocol: TCP
      targetPort: 8443
    sessionAffinity: None
    type: ClusterIP
  status:
    loadBalancer: {}
- apiVersion: apps/v1
  kind: Deployment
  metadata:
    annotations:
      deployment.kubernetes.io/revision: "1"
      kubectl.kubernetes.io/last-applied-configuration: |
        {"apiVersion":"apps/v1","kind":"Deployment","metadata":{"annotations":{},"labels":{"app":"classifier"},"nam
e":"classifer-deployment","namespace":"default"},"spec":{"replicas":2,"selector":{"matchLabels":{"app":"classifier"}},"template":{"metadata":{"labels":{"app":"classifier"}},"spec":{"containers":[{"image":"classifier-k8s:latest","imagePullPolicy":"Never","name":"classifier","ports":[{"containerPort":7860}]}]}}}}                                     creationTimestamp: "2024-12-27T14:55:00Z"
    generation: 1
    labels:
      app: classifier
    name: classifer-deployment
    namespace: default
    resourceVersion: "94492"
    uid: 3bd26c57-53ec-40c3-93f5-d44364d9d873
  spec:
    progressDeadlineSeconds: 600
    replicas: 2
    revisionHistoryLimit: 10
    selector:
      matchLabels:
        app: classifier
    strategy:
      rollingUpdate:
        maxSurge: 25%
        maxUnavailable: 25%
      type: RollingUpdate
    template:
      metadata:
        creationTimestamp: null
        labels:
          app: classifier
      spec:
        containers:
        - image: classifier-k8s:latest
          imagePullPolicy: Never
          name: classifier
          ports:
          - containerPort: 7860
            protocol: TCP
          resources: {}
          terminationMessagePath: /dev/termination-log
          terminationMessagePolicy: File
        dnsPolicy: ClusterFirst
        restartPolicy: Always
        schedulerName: default-scheduler
        securityContext: {}
        terminationGracePeriodSeconds: 30
  status:
    availableReplicas: 2
    conditions:
    - lastTransitionTime: "2024-12-27T14:55:02Z"
      lastUpdateTime: "2024-12-27T14:55:02Z"
      message: Deployment has minimum availability.
      reason: MinimumReplicasAvailable
      status: "True"
      type: Available
    - lastTransitionTime: "2024-12-27T14:55:00Z"
      lastUpdateTime: "2024-12-27T14:55:02Z"
      message: ReplicaSet "classifer-deployment-5545798ff5" has successfully progressed.
      reason: NewReplicaSetAvailable
      status: "True"
      type: Progressing
    observedGeneration: 1
    readyReplicas: 2
    replicas: 2
    updatedReplicas: 2
- apiVersion: apps/v1
  kind: ReplicaSet
  metadata:
    annotations:
      deployment.kubernetes.io/desired-replicas: "2"
      deployment.kubernetes.io/max-replicas: "3"
      deployment.kubernetes.io/revision: "1"
    creationTimestamp: "2024-12-27T14:55:00Z"
    generation: 1
    labels:
      app: classifier
      pod-template-hash: 5545798ff5
    name: classifer-deployment-5545798ff5
    namespace: default
    ownerReferences:
    - apiVersion: apps/v1
      blockOwnerDeletion: true
      controller: true
      kind: Deployment
      name: classifer-deployment
      uid: 3bd26c57-53ec-40c3-93f5-d44364d9d873
    resourceVersion: "94490"
    uid: 50418064-e514-4c21-a703-bf7d08d453d0
  spec:
    replicas: 2
    selector:
      matchLabels:
        app: classifier
        pod-template-hash: 5545798ff5
    template:
      metadata:
        creationTimestamp: null
        labels:
          app: classifier
          pod-template-hash: 5545798ff5
      spec:
        containers:
        - image: classifier-k8s:latest
          imagePullPolicy: Never
          name: classifier
          ports:
          - containerPort: 7860
            protocol: TCP
          resources: {}
          terminationMessagePath: /dev/termination-log
          terminationMessagePolicy: File
        dnsPolicy: ClusterFirst
        restartPolicy: Always
        schedulerName: default-scheduler
        securityContext: {}
        terminationGracePeriodSeconds: 30
  status:
    availableReplicas: 2
    fullyLabeledReplicas: 2
    observedGeneration: 1
    readyReplicas: 2
    replicas: 2
kind: List
metadata:
  resourceVersion: ""
