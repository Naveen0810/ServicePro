pipeline {
    agent any

    environment {
        DOCKERHUB_USER = 'naveen0810'
    }

    stages {

        stage('Clone Code') {
        steps {
        git branch: 'main', url: 'https://github.com/Naveen0810/ServicePro'
    }
}

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t $DOCKERHUB_USER/servicepro .
                '''
            }
        }

        stage('Push Docker Image') {
            steps {
                sh '''
                docker login -u $DOCKERHUB_USER -p Naveen/08
                docker push $DOCKERHUB_USER/servicepro
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                export KUBECONFIG=/etc/rancher/k3s/k3s.yaml
                kubectl apply -f k8s/deployment.yaml
                kubectl rollout restart deployment servicepro
                kubectl rollout status deployment servicepro
                '''
            }
        }
    }
}