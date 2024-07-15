# Assessment

# qa-test

Prerequisites:
-Docker
-kubectl
-minicube
-Python

git clone https://github.com/Vengatesh-m/qa-test


**Kubernetes Deployment:**

-Install minicube

-Start minicube
 # minicube start

-Verify minicube is running 
# minikube status

-Ensure kubectl is configured to communicte with minikube cluster 
# kubectl config use-context minikube

-Navigate to the deployment directory
# cd/path/Deployment

-Apply the Kubernnetes Manifests
# kubectl apply -f.

**Verification:**

-Verify the deployment
# kubectl get deployments
# kubectl get services
# kubectl get pods

-Get the frontend pod name
# kubectl get pods -l app=frontend 
ex:(frontend-deployment-6485c5c85c-nqzlj)

Check the logs of the frontend pod
# kubectl logs frontend-deployment-6485c5c85c-nqzlj

-Access the frontend service
# minikube service frontend-service --url ex:(URL:http://127.0.0.1:59894)

-Getting the Minikube IP
# minikube ip

-Get the NodePort of the frontend service
# kubectl get services
(http://minikube ip : nodeport)

**Automated Testing:**

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_frontend_backend_integration():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:62217")
    time.sleep(5)
    welcome_message_element = driver.find_element(By.TAG_NAME,"h1")
    welcome_message = welcome_message_element.text
    print("Welcome message:", welcome_message)

# Can run the test.script on cmd "pytest -v -s test_script.py"


