pipeline {
    agent any
    stages {
        stage('Checkout') {
        steps {
            // Get the code from a GitHub repository
            git url: 'https://github.com/Mulik6/WorldOfGame.git', branch: 'master'
            }
        }
        stage('Build') {
            steps {
                //Building the docker image using the compose file
                sh 'docker compose -f docker-compose.yml'
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
        stage('Finalize') {
            steps {
                //Terminate the container
                sh "docker-compose down"
                //Pushing the image to dockerhub
                sh "docker-compose push"
            }
    }
}