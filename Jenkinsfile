pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Get the code from a GitHub repository
                git url: 'https://github.com/Mulik6/WorldOfGame.git', branch: 'master'
            }
        }
        stage('install dependencies') {
            steps {
                // Installing Python 3 and pip
                sh 'sudo apt-get update && sudo apt-get install -y python3 python3-pip'
                // Installing dependencies
                sh 'python3 -m pip install -r requirements.txt'
                //Creating dummy Scores file
                writeFile file: './Main/Scores.txt', text: '666'
            }
        }
        stage('Build') {
            steps {
                //Building the docker image using the compose file
                sh 'docker-compose build'
            }
        }
        stage('Run') {
            steps {
                //Running the docker image in a container
                sh 'docker-compose up -d'
            }
        }
        stage('Test') {
            steps {
                //Running the playwright test - will fail if exit code is 1
                sh "python3 ./Utilities/e2e.py"
            }
        }
        stage('Finalize') {
            steps {
                //Terminate the container
                sh "docker-compose down"
                //Pushing the image to dockerhub
                withCredentials([usernamePassword(credentialsId: 'dockerHubCreds', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sh "echo ${PASSWORD} | docker login -u ${USERNAME} --password-stdin"
                    sh "docker-compose push"
                }
            }
        }
    }
}