pipeline {

    agent any

    triggers {
        pollSCM('H/2 * * * *')
    }

    environment {
        DOCKER_IMAGE = "aarmaxx17/sentiment-app"
    }

    stages {

        stage('Checkout') {

            steps {

                checkout scm

            }

        }


        stage('Setup Python') {

            steps {

                sh '''
                rm -rf .jenkins-venv

                python3 -m venv .jenkins-venv

                .jenkins-venv/bin/pip install --upgrade pip

                .jenkins-venv/bin/pip install -r requirements.txt
                '''

            }

        }


        stage('Run Tests') {

            steps {

                sh '''
                .jenkins-venv/bin/pytest -v
                '''

            }

        }


        stage('Build Docker Image') {

            steps {

                sh '''
                docker build \
                -t $DOCKER_IMAGE:$BUILD_NUMBER \
                -t $DOCKER_IMAGE:latest .
                '''

            }

        }


        stage('Push Docker Image') {

            steps {

                withCredentials([

                    usernamePassword(

                        credentialsId: 'dockerhub',

                        usernameVariable: 'DOCKER_USER',

                        passwordVariable: 'DOCKER_TOKEN'

                    )

                ]) {

                    sh '''

                    echo "$DOCKER_TOKEN" | \
                    docker login \
                    -u "$DOCKER_USER" \
                    --password-stdin

                    docker push $DOCKER_IMAGE:$BUILD_NUMBER

                    docker push $DOCKER_IMAGE:latest

                    '''

                }

            }

        }


        stage('Deploy to Kubernetes') {

            steps {

                sh '''

                kubectl set image \
                deployment/sentiment-app \
                sentiment-app=$DOCKER_IMAGE:$BUILD_NUMBER

                kubectl rollout status \
                deployment/sentiment-app \
                --timeout=120s

                '''

            }

        }

    }


    post {

        success {

            echo 'CI/CD Pipeline completed successfully!'

        }

        failure {

            echo 'CI/CD Pipeline failed!'

        }

    }

}
