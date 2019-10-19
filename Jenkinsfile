pipeline {
    agent {
        node {
            label 'Slave1'
        }
    }
    environment {
        PYENV_ROOT="$HOME/.pyenv"
        PATH = "$HOME/.poetry/bin:$PYENV_ROOT/bin:$PATH"
    }
    stages {
        stage('Set Environment Values') {
            steps {
                sh 'eval "$(pyenv init -)"'
                sh 'echo $PATH'
                sh 'pyenv local 3.7.0'
                sh 'python -V'
                sh 'poetry debug:info'
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
