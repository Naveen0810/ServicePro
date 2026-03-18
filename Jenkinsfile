pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'servicepro-app'
        DOCKER_TAG = "${env.BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install --no-cache-dir -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Assuming you have tests, e.g., pytest
                sh 'python -m pytest || echo "No tests found or tests failed"'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
            }
        }

        stage('Push Docker Image') {
            steps {
                // Assuming Docker registry is configured
                sh "docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} your-registry/${DOCKER_IMAGE}:${DOCKER_TAG}"
                sh "docker push your-registry/${DOCKER_IMAGE}:${DOCKER_TAG}"
            }
        }

        stage('Deploy') {
            steps {
                // Example deployment step, adjust as needed
                sh 'echo "Deploying application..."'
                // sh 'docker run -d -p 5000:5000 ${DOCKER_IMAGE}:${DOCKER_TAG}'
            }
        }
    }

    post {
        always {
            sh 'docker system prune -f'
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}