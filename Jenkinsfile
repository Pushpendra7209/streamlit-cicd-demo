pipeline {
    agent any

    stages {

        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Git Pull') {
            steps {
                sh 'git pull origin main'
            }
        }

        stage('Add Configuration') {
            steps {
                sh 'echo "Configuration step completed"'
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t streamlit-app .'
            }
        }

        stage('Delete Previous Container') {
            steps {
                sh 'docker rm -f streamlit || true'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 8501:8501 --name streamlit streamlit-app'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished'
        }
        success {
            echo 'Build Successful'
        }
        failure {
            echo 'Build Failed'
        }
    }
}
