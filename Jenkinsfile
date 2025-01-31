pipeline {
    agent any

    environment {
        DOCKER_HUB_USER = "hfmartinez"
        DOCKER_IMAGE = "fastapi-app"
        KUBE_DEPLOYMENT = "fastapi-deployment"
        SERVICE_NAME = "fastapi-service"
    }

    stages {
        stage('Code checkout') {
            steps {
                git 'https://github.com/hfmartinez/FastAPI_app.git'
            }
        }

        stage('Build and publish docker image') {
            steps {
                script {
                    def IMAGE_TAG = "$DOCKER_HUB_USER/$DOCKER_IMAGE:latest"

                    sh "docker build -t $IMAGE_TAG ."
                    sh "docker push $IMAGE_TAG"
                }
            }
        }

        stage('Blue-Green Deployment') {
            steps {
                script {
                    def currentVersion = sh(
                        script: "kubectl get svc $SERVICE_NAME -o=jsonpath='{.spec.selector.version}'",
                        returnStdout: true
                    ).trim()
                    
                    def newVersion = (currentVersion == "blue") ? "green" : "blue"
                    def IMAGE_TAG = "$DOCKER_HUB_USER/$DOCKER_IMAGE:latest"

                    /
                    sh """
                    kubectl apply -f - <<EOF
                    apiVersion: apps/v1
                    kind: Deployment
                    metadata:
                      name: $KUBE_DEPLOYMENT-$newVersion
                    spec:
                      replicas: 2
                      selector:
                        matchLabels:
                          app: fastapi
                          version: $newVersion
                      template:
                        metadata:
                          labels:
                            app: fastapi
                            version: $newVersion
                        spec:
                          containers:
                          - name: fastapi
                            image: $IMAGE_TAG
                            ports:
                            - containerPort: 8000
                    EOF
                    """

                    
                    sh "kubectl patch svc $SERVICE_NAME -p '{\"spec\":{\"selector\":{\"app\":\"fastapi\", \"version\":\"$newVersion\"}}}'"
                }
            }
        }

        stage('Validate Deployment') {
            steps {
                sh "kubectl get pods -o wide"
                sh "kubectl get svc $SERVICE_NAME"
            }
        }
    }
}
