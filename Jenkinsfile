pipeline {
    agent any

    environment {
        IMAGE_NAME = "streamlit-app"
        CONTAINER_NAME = "streamlit-container"
    }

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker stop $CONTAINER_NAME || true'
                sh 'docker rm $CONTAINER_NAME || true'
            }
        }

        stage('Run New Container') {
            steps {
                sh 'docker run -d -p 8501:8501 --name $CONTAINER_NAME $IMAGE_NAME'
            }
        }
    }
}
