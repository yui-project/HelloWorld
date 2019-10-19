pipeline {
    agent {
        node {
            label 'Slave1'
        }
    }
    stages {
        stage('Set Environment Values') {
            steps {
                sh 'source ~/.bash_profile'
                sh 'echo $PATH'
                sh 'python -V'
            }
        }
        stage('Git Pull'){
            steps {
                git url: 'https://github.com/yui-project/HelloWorld.git', branch: 'master'
            }
        }
        stage('Compile and Build'){
            steps {
                sh 'ls -la'
                sh 'chmod 777 build.sh'
                sh './build.sh'
            }
        }
        stage('Compile'){
            steps {
                sh 'ls -la'
                sh 'gcc hello.c'
            }
        }
        
        stage('Test'){
            steps {
                sh 'ls -la'
                sh './test.sh'
            }
        }
    }
}
