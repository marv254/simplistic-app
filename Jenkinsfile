pipeline{
    agent any 
        stages{
            stage('Setup Virtual Environment') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate'
                sh 'pip3 install pyinstaller'
            }
        }
            stage("building and compile app"){
                steps{
                    sh ". venv/bin/activate && make build"
                }
            }
            stage("test app"){
                steps{
                     sh ". venv/bin/activate && make test"
                }
            }

            stage("package app"){
                steps{
                     sh ". venv/bin/activate && make package"
                }
            }
    }
}