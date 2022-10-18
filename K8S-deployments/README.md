# Configure and Deploy on AWS EKS

This cheatsheet can help you deploy a DVWA server with 2 replicas on K8S
using AWS EKS.

Note you should put an allowed IP in the `loadbalancer.yml` file so you can access the url.
You can get the DNS of the loadbalancer using `kubectl get all -A`.

Deploy the daemonset for Cortex XDR or Prisma Cloud Compute by using the UI for the respective tool to download
the configuration file.

## Prerequisite
* AWS account
* kubectl installed
* eksctl installed

#### References:
* https://docs.aws.amazon.com/eks/latest/userguide/sample-deployment.html
* https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html


#### Create the EKS cluster
```
eksctl create cluster --name sample-cluster --region us-west-1
```

#### Create the DVWA pod
```
kubectl apply -f nginx.yml
```

#### Create the Loadbalancer
```
kubectl apply -f loadbalancer.yml
```

#### Apply daemonset for PCC or XDR
```
kubectl apply -f <daemonset.yml>
```


#### View deployed resources
```
kubectl get all -A
```

#### Destroy Cluster
```
eksctl delete cluster --name sample-cluster --region us-west-1
```
