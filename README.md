# Kubernetes CICD Tutorial

This repo contains all the code needed to follow along with our **[YouTube Tutorial](https://youtu.be/GlhK7mz5IJo)** or **[Written Article](https://m1key0m.github.io/rayanslim/lesson.html?course=kubernetes-cicd-course&lesson=introduction)**.

## Prerequisites

To follow along with this tutorial, you'll need:

- kubectl installed and configured ([https://youtu.be/IBkU4dghY0Y](https://youtu.be/IBkU4dghY0Y))
- Helm installed: ([https://m1key0m.github.io/rayanslim/lesson.html?course=prometheus-grafana-monitoring-course&lesson=helm-installation](https://m1key0m.github.io/rayanslim/lesson.html?course=prometheus-grafana-monitoring-course&lesson=helm-installation))
- A GitHub account: ([https://github.com/](https://github.com/))

## Install ArgoCD

```bash
helm repo add argo https://argoproj.github.io/argo-helm
helm repo update
kubectl create namespace argocd
helm install argocd argo/argo-cd --namespace argocd --version 7.7.0
```

## Access ArgoCD UI

```bash
kubectl port-forward svc/argocd-server -n argocd 8080:80
```

## Retrieve Credentials

```bash
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
```
## ArgoCD Application

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: grade-submission-api
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/YOUR_USERNAME/grade-api-gitops.git
    targetRevision: HEAD
    path: .
  destination:
    server: https://kubernetes.default.svc
    namespace: default
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```

## Creating Image Pull Secrets

To allow Kubernetes to pull images from GitHub Container Registry:

```yaml
kubectl create secret docker-registry ghcr-secret \\
  --docker-server=ghcr.io \\
  --docker-username=YOUR_USERNAME \\
  --docker-password=YOUR_PAT \\
  --namespace=default
```

## Todo App (Python / Flask)

A second app, [todo-app-python](https://github.com/faizan35/todo-app-python), lives in [`todo-app/`](todo-app) and has its own pipeline in [`.github/workflows/todo-app-ci-cd.yml`](.github/workflows/todo-app-ci-cd.yml). It only runs when files under `todo-app/` change (and the grade API pipeline ignores those changes).

On each push to `main` the pipeline:

1. Builds and pushes `ghcr.io/m1key0m/kubernetes-cicd-tutorial/todo-app:<sha>` (and `:latest`).
2. Copies `todo-app/k8s/deployment.yaml` and `service.yaml` into the `todo-app/` folder of the GitOps repo (first run only) and bumps the image tag.

Create the ArgoCD Application once:

```bash
kubectl apply -f todo-app/k8s/argocd-application.yaml
```

The app is exposed on NodePort `30080`. It uses the same `ghcr-secret` image pull secret as the grade API.

## Flask Product API

A third app, [Simple-Flask-App-Docker](https://github.com/chesahkalu/Simple-Flask-App-Docker), lives in [`flask-app/`](flask-app). It's a small REST API for a product list (`GET/POST /products`, `GET/PUT/DELETE /products/<id>`). Its pipeline, [`.github/workflows/flask-app-ci-cd.yml`](.github/workflows/flask-app-ci-cd.yml), works the same way as the todo app's: it builds `ghcr.io/m1key0m/kubernetes-cicd-tutorial/flask-app` and updates `flask-app/` in the GitOps repo.

Create the ArgoCD Application once:

```bash
kubectl apply -f flask-app/k8s/argocd-application.yaml
```

The API is exposed on NodePort `30081`, for example `curl http://localhost:30081/products`.

### Become a Cloud and DevOps Engineer

Visit[https://m1key0m.github.io/rayanslim](https://m1key0m.github.io/rayanslim)
