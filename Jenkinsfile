pipeline {
    agent {
        node {
            label 'Slave1'
        }
    }
    stages {
        stage('Git Pull'){
            git url: 'https://github.com/yui-project/HelloWorld.git', branch: 'master'
        }
        stage('Compile and Build'){
            sh 'ls -la'
            sh 'chmod 777 build.sh'
            sh './build.sh'
        }
        stage('Compile'){
            sh 'ls -la'
            sh 'gcc hello.c'
        }
        
        stage('Test'){
            sh 'ls -la'
            sh './a.out'
        }
    }
}
