# AI Sentiment Analysis - CI/CD Pipeline

An AI-based Sentiment Analysis web application integrated with a complete CI/CD pipeline using **GitHub, Jenkins, Docker, Docker Hub, Kubernetes, and Minikube**.

The application accepts text from the user and classifies the sentiment as **Positive, Negative, or Neutral**.

---

## Project Overview

The main objective of this project is to demonstrate how a web application can be automatically tested, containerized, and deployed whenever a developer makes changes to the source code.

Instead of manually building and deploying the application after every update, the CI/CD pipeline automates the complete process.

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application programming language |
| Flask | Web framework |
| VADER Sentiment | Sentiment analysis |
| Pytest | Automated testing |
| Git | Version control |
| GitHub | Source code repository |
| Jenkins | CI/CD automation |
| Docker | Containerization |
| Docker Hub | Docker image registry |
| Kubernetes | Container orchestration |
| Minikube | Local Kubernetes cluster |
| Ubuntu WSL | Linux development environment |

---

## Application Features

- Analyze text entered by the user
- Detect Positive sentiment
- Detect Negative sentiment
- Detect Neutral sentiment
- Display sentiment confidence
- REST API for sentiment analysis
- Health-check endpoint
- Automated testing using Pytest
- Docker containerization
- Automated CI/CD pipeline
- Kubernetes deployment
- Multiple application replicas
- Kubernetes health monitoring

---

## Project Architecture

```text
Developer
    |
    | git push
    v
GitHub Repository
    |
    v
Jenkins
    |
    +---- Checkout Source Code
    |
    +---- Install Dependencies
    |
    +---- Run Pytest Tests
    |
    +---- Build Docker Image
    |
    +---- Push Image to Docker Hub
    |
    v
Kubernetes / Minikube
    |
    +---- Deployment
    |
    +---- Pods
    |
    v
Kubernetes Service
    |
    v
Sentiment Analysis Web Application
```

---

## CI/CD Pipeline

The pipeline is defined using the `Jenkinsfile`.

### 1. Checkout

Jenkins retrieves the latest source code from the GitHub repository.

### 2. Setup Python Environment

Jenkins creates a Python virtual environment and installs the dependencies from:

```text
requirements.txt
```

### 3. Automated Testing

Jenkins executes the automated tests using:

```bash
pytest -v
```

If a test fails, the pipeline stops and the faulty version is not deployed.

### 4. Docker Build

After successful testing, Jenkins builds a new Docker image.

Example:

```text
aarmaxx17/sentiment-app:5
```

The Jenkins build number is used as the Docker image version.

### 5. Docker Hub Push

Jenkins pushes the new Docker image to Docker Hub.

Docker image:

```text
aarmaxx17/sentiment-app
```

### 6. Kubernetes Deployment

Jenkins updates the Kubernetes Deployment with the newly created Docker image.

Kubernetes performs a rolling update so that the latest version of the application is deployed.

---

## Project Structure

```text
sentiment-cicd/
|
|-- app.py
|-- Dockerfile
|-- Jenkinsfile
|-- requirements.txt
|-- README.md
|-- .gitignore
|-- .dockerignore
|
|-- templates/
|   `-- index.html
|
|-- tests/
|   `-- test_app.py
|
`-- k8s/
    |-- deployment.yaml
    `-- service.yaml
```

---

## Sentiment Analysis

The application uses VADER Sentiment Analysis.

Example:

```text
Input:
I really love this application.

Output:
Positive
```

Another example:

```text
Input:
This service is terrible.

Output:
Negative
```

Neutral example:

```text
Input:
The meeting starts at 5 PM.

Output:
Neutral
```

---

## Run the Application Locally

Create and activate the Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python3 app.py
```

The Flask application runs on port:

```text
5000
```

---

## Run Tests

Execute:

```bash
pytest -v
```

The tests verify the web application, health endpoint, and sentiment classification.

---

## Docker

Build the Docker image:

```bash
docker build -t aarmaxx17/sentiment-app:latest .
```

Run the container:

```bash
docker run -p 5000:5000 aarmaxx17/sentiment-app:latest
```

Check running containers:

```bash
docker ps
```

---

## Kubernetes Deployment

Start Minikube:

```bash
minikube start --driver=docker
```

Deploy the application:

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

Check deployment:

```bash
kubectl get deployments
```

Check pods:

```bash
kubectl get pods
```

Check services:

```bash
kubectl get services
```

Access the application:

```bash
minikube service sentiment-service --url
```

---

## Resume Project After Restart

Start Docker Desktop first.

Then open Ubuntu WSL and run:

```bash
cd ~/sentiment-cicd

minikube start --driver=docker

sudo systemctl start jenkins

kubectl get pods
```

Open Jenkins at:

```text
http://localhost:8080
```

To access the application:

```bash
minikube service sentiment-service --url
```

---

## Updating the Application

After changing the source code:

```bash
git add .
git commit -m "Update application"
git push origin main
```

Jenkins detects the change and executes the CI/CD pipeline.

```text
Code Change
    |
    v
GitHub
    |
    v
Jenkins
    |
    v
Automated Tests
    |
    v
Docker Build
    |
    v
Docker Hub
    |
    v
Kubernetes Deployment
    |
    v
Updated Application
```

---

## Benefits of the Project

- Automated software testing
- Faster application deployment
- Consistent Docker environments
- Versioned Docker images
- Automated Kubernetes deployment
- Reduced manual deployment work
- Easy application updates
- Demonstrates a complete DevOps workflow

---

## Author

**Aryan Rulekar**

GitHub: **Aarmaxx17**

---

## Conclusion

This project demonstrates a complete CI/CD workflow for an AI Sentiment Analysis application. GitHub manages the source code, Jenkins automates testing and deployment, Docker packages the application, Docker Hub stores the container images, and Kubernetes manages the running application.

The pipeline allows a new application version to move from a source-code change to a running Kubernetes deployment with minimal manual intervention.
