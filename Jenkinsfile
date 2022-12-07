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
                sh 'python3 -m pip install -r requirements.txt'
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
                //Creating dummy Scores file
                writeFile file: 'Scores.txt', text: '666'
                //Running the docker image in a container
                sh 'docker compose up'
            }
        }
        stage('Test') {
            steps {
                //Running the playwright test - will fail if exit code is 1
                sh "python e2e.py"
            }
        }
        stage('Finalize') {
            steps {
                //Terminate the container
                sh "docker-compose down"
                //Pushing the image to dockerhub
                sh "docker-compose push"
            }
        }
    }
}