pipeline {
    agent any

    environment {
        IMAGE_NAME = "streamlit-app"
        CONTAINER_NAME = "streamlit"
        PORT = "8501"
    }

    stages {

        stage('Declarative: Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Git Pull') {
            steps {
                sh 'git pull origin main || true'
            }
        }

        stage('Add Configuration') {
            steps {
                echo "Adding configuration..."
                sh 'echo "Environment Ready"'
            }
        }

        stage('Build Image') {
            steps {
                echo "Building Docker image..."
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Delete Previous Container') {
            steps {
                echo "Removing old container if exists..."
                sh 'docker rm -f $CONTAINER_NAME || true'
            }
        }

        stage('Run container') {
            steps {
                echo "Starting new container..."
                sh 'docker run -d -p $PORT:$PORT --name $CONTAINER_NAME $IMAGE_NAME'
            }
        }
    }

    post {

        success {
            echo "Build Successful ✅"
        }

        failure {
            echo "Build Failed ❌"
        }

        always {
            echo "Declarative: Post Actions"
            sh 'docker ps'
        }
    }
}
