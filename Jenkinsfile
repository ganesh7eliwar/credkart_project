pipeline {
    agent any

    environment {
        VENV_DIR = '.venv'
        PYTHON = "${VENV_DIR}\\Scripts\\python.exe"
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
                echo 'Creating virtual environment & installing dependencies...'
                bat """
                    if not exist %VENV_DIR% (
                        python -m venv %VENV_DIR%
                    )

                    %PYTHON% -m pip install --upgrade pip
                    %PYTHON% -m pip install --quiet --no-input --disable-pip-version-check -r requirements.txt
                """
            }
        }

        stage('Run CredKart Tests') {
            steps {
                echo 'Running tests for CredKart...'
                retry(2) {
                    bat """
                        %PYTHON% -m pytest -vs testcases/ --browser ${params.BROWSER} --alluredir=allure_reports -n 4
                    """
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed.'
            archiveArtifacts artifacts: 'reports/*.html, screenshots/*.png, logs/*.log', fingerprint: true

            allure([
                includeProperties: false,
                jdk: '',
                results: [[path: "allure_reports"]]
            ])
        }

        success {
            echo 'All Tests Passed!'
        }

        failure {
            echo 'Test or setup failed. Check logs.'
        }
    }
}