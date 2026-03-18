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
                docker login -u $DOCKERHUB_USER -p your_password
                docker push $DOCKERHUB_USER/servicepro
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                kubectl apply -f k8s/deployment.yaml
                '''
            }
        }
    }
}