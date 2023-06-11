pipeline {
    agent any
    triggers {
        githubPush()
    }
    stages {
        stage('first Test') {
            steps {
                sh '''
                    #!/bin/bash
                    virtualenv venv --distribute
                    source venv/bin/activate
                    docker build -t flaskapp .
                    docker run -it -p 4000:4000 -d flaskapp
                '''
            }
        }
    }
}