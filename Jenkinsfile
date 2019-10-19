pipeline {
    agent {
        node {
            label 'Slave1'
        }
    }
    environment {
        PYENV_ROOT="$HOME/.pyenv"
        PATH = "$HOME/.poetry/bin:$PYENV_ROOT/bin:$PYENV_ROOT/shims:$PATH"
    }
    stages {
        stage('Check Environment Values') {
            steps {
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
        stage('Test'){
            steps {
                sh 'ls -la'
                sh 'chmod 777 test.sh'
                sh './test.sh'
            }
        }
        stage('Compile and Upload'){
            steps {
                sh 'ls -la'
                sh 'chmod 777 build.sh'
                sh './build.sh'
            }
        }
    }
}
