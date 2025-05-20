pipeline {
    agent any
    
    environment {
        PYTHON_VERSION = '3.8'
    }
    
    stages {
        stage('Setup Python') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    pip install pytest pytest-cov
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest test_main.py -v --cov=. --cov-report=xml
                '''
            }
        }
        
        stage('Report Coverage') {
            steps {
                cobertura coberturaReportFile: 'coverage.xml'
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
}