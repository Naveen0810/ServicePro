pipeline {
    agent any

    environment {
        DOCKERHUB_USER = 'naveen0810'
    }

    stages {

        stage('Clone Code') {
            steps {
                git 'https://github.com/Naveen0810/ServicePro'
            }
        }

        stage('Build Backend') {
            steps {
                dir('backend') {
                    sh 'docker build -t $DOCKERHUB_USER/servicepro-backend .'
                }
            }
        }

        stage('Build Frontend') {
            steps {
                dir('frontend') {
                    sh 'docker build -t $DOCKERHUB_USER/servicepro-frontend .'
                }
            }
        }

        stage('Push Images') {
            steps {
                sh '''
                docker login -u $DOCKERHUB_USER -p your_password
                docker push $DOCKERHUB_USER/servicepro-backend
                docker push $DOCKERHUB_USER/servicepro-frontend
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                kubectl apply -f k8s/backend-deployment.yaml
                kubectl apply -f k8s/frontend-deployment.yaml
                '''
            }
        }
    }
}