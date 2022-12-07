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
                // Installing dependencies
                sh 'python3 -m pip install -r requirements.txt'
                //Creating dummy Scores file
                //sh 'echo 666 > /Main/Scores.txt'
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
                sh 'docker-compose up'
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