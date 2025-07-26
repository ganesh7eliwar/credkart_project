pipeline {
    agent any

    environment {
        VENV_DIR = '.venv'  // Local virtual environment directory
    }

    parameters {
        string(name: 'BROWSER', defaultValue: 'chrome', description: 'Browser to use for tests')
    }

    stages {
        stage('Checkout Source') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo 'Setting up Python virtual environment...'
                bat """
                    if not exist ${VENV_DIR} (
                        python -m venv ${VENV_DIR}
                    )
                    call ${VENV_DIR}\\Scripts\\activate
                    pip install --quiet --no-input --disable-pip-version-check --requirement requirements.txt
                """
            }
        }

        stage('Lint Code') {
            steps {
                echo 'Running flake8 linting...'
                bat """
                    call ${VENV_DIR}\\Scripts\\activate
                    flake8 . --exit-zero
                """
            }
        }

        stage('Prepare Report Directory') {
            steps {
                script {
                    env.TIMESTAMP = new Date().format("ddMMyyyyHHmmss")
                    env.REPORT_DIR = "allure_reports_${env.TIMESTAMP}"
                }
            }
        }

        stage('Run CredKart Tests') {
            steps {
                echo 'Running Selenium tests for CredKart...'
                retry(2) {
                    bat """
                        call ${VENV_DIR}\\Scripts\\activate
                        pytest -v -s testcases/ --browser ${params.BROWSER} --alluredir=${env.REPORT_DIR}
                    """
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed.'
            archiveArtifacts artifacts: 'reports/*.html, screenshots/*.png, logs/*.log', fingerprint: true

            // Allure report publishing
            allure([
                includeProperties: false,
                jdk: '',
                results: [[path: "${env.REPORT_DIR}"]]
            ])
        }

        success {
            echo 'All tests passed!'
        }

        failure {
            echo 'Test or setup failed. Check logs.'
        }

        cleanup {
            echo 'Cleaning up workspace...'
            deleteDir()
        }
    }
}
