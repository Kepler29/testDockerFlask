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
                    docker build -t flaskapp .
                    docker run -it -p 4000:4000 --name testDF -d flaskapp
                '''
            }
        }
    }
}