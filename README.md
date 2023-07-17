# web-app-simulate-workload
The goal of this app is to use it on the receiving end of a load testing tool. 

## Running the app

- Development environment

```python
uvicorn main:app --reload
```

## Running the Dockerfile

```bash
$ docker build -t simulate-workload .
$ docker run -p 8000:8000 simulate-workload
```

## Access the website

- In your browser, navigate to ```https://127.0.0.1:8000/v1/sleep?ms=1000```



## Deploy the app into argocd with:


```yaml

apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  creationTimestamp: "2023-07-14T18:35:19Z"
  generation: 1107
  name: simulate-load
  namespace: glueops-core
  resourceVersion: "1769391"
  uid: c7ad104c-48a3-4665-b984-5a8ac08b300b
spec:
  destination:
    namespace: simulate-load
    server: https://kubernetes.default.svc
  project: glueops-core
  source:
    chart: app
    helm:
      values: |
        image:
          registry: ghcr.io
          repository: glueops/web-app-simulate-workload
          tag: 0.1.0-alpha1
          pullPolicy: Always
          port: 8000

        service:
          enabled: true

        deployment:
          replicas: 2
          enabled: true
          imagePullPolicy: Always
          resources:
            requests:
              cpu: 100m
              memory: 128Mi
            # limits:
            #   cpu: 120m
            #   memory: 154Mi

          livenessProbe:
            httpGet:
              path: /v1/sleep?ms=1
              port: 8000
          readinessProbe:
            httpGet:
              path: /v1/sleep?ms=1
              port: 8000


        appName: 'simulate-workload'
        ingress:
          # annotations:
          # nginx.ingress.kubernetes.io/limit-rps: "1"
          enabled: true
          ingressClassName: public
          entries:
            - name: public
              hosts:
              - hostname: APP_DOMAIN_GOES_HERE
    repoURL: https://helm.gpkg.io/project-template
    targetRevision: 0.2.0
  syncPolicy:
    automated:
      selfHeal: true
    syncOptions:
    - CreateNamespace=true
```
