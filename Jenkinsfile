pipeline {
    agent any

    environment {
        IMAGE = "husna615/malware-detector"
    }

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/ha55454/cyber-def25.git'
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t $IMAGE .'
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh 'echo $PASS | docker login -u $USER --password-stdin'
                }
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push $IMAGE'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker compose up -d'
            }
        }
    }
}
