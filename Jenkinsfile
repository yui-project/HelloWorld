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
                sh '''
                    eval "$(pyenv init -)"
                    echo $PATH
                '''
                sh 'echo $PATH'
                sh 'pyenv versions'
                sh 'pyenv local 3.7.0'
                sh 'python -V'
                sh 'which python'
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
                sh 'gcc hello.c -o hello.out'
            }
        }
        
        stage('Test'){
            steps {
                sh 'python -V'
                sh 'which python'
                sh 'poetry debug:info'
                sh 'ls -la'
                sh './hello.out'
                sh './test.sh'
            }
        }
    }
}
