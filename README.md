# EdgeComputing

1. Create docker image for the Flask Application.
  `Docker build -t pank05081985/flask-app .`

2. Try to run the docker image locally.
   `Docker run -p 80:5000 pank05081985/flask-app`

3. Once you are satisfied with the image, You can push it to the docker repository.
   `Docker login`
   `Docker push pank05081985/flask-app:latest` 
  
4. Deploy the created image to local K8 or Minikube environment.
   `kubectl apply -f deployment.yaml`

5. Add a node port service for testing purpose on local.
   `kubectl port-forward service/flask-app-service 80:80`

