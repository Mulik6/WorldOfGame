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
                 // Create a virtual environment
                sh 'python3 -m venv venv'
                // Activate the virtual environment and install dependencies
                sh '. venv/bin/activate && pip install -r requirements.txt'
                // Install pytest-playwright plugin and playwright
                sh '. venv/bin/activate && pip install pytest-playwright'
                sh '. venv/bin/activate && playwright install'
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
                //Running the playwright test in the virtual environment - will fail if exit code is 1
                sh ". venv/bin/activate && python3 ./Utilities/e2e.py"
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