pipeline {
    agent any
    triggers {
        githubPush()
    }
    stages {
        stage('first Test') {
            steps {
                sh ''' hpla'''
            }
        }
    }
}