pipeline {
  agent any
  environment {
    PATH = "/var/lib/jenkins/.local/bin:$PATH"
  }
    stages {
        stage('Build and Execute Unit Tests') {
            steps {
                sh '''
                export PYTHONPATH=$PYTHONPATH:$WORKSPACE
                echo $WORKSPACE
                echo $PYTHONPATH
                whoami
                chmod +x $WORKSPACE/ExtremeAutomation/Unittests/Jenkins/Scripts/*.sh
                chmod +x $WORKSPACE/ExtremeAutomation/Library/Utils/Siesta/MakeNetSightUtilitiesZip.sh $WORKSPACE/ExtremeAutomation/Library/Utils/Siesta/MakeRestServerZip.sh
                cd $WORKSPACE
                $WORKSPACE/ExtremeAutomation/Unittests/Jenkins/Scripts/JenkinsTests.sh
                '''
            }
        }
        stage('Collect Flake8 Information') {
            steps {
                sh '''
                export PYTHONPATH=$PYTHONPATH:$WORKSPACE
                echo $WORKSPACE
                echo $PYTHONPATH
                cd $WORKSPACE
                touch flake8.out && touch flake8_ui.out && touch flake8_api.out && touch flake8_net.out && touch flake8_tgen.out && touch flake8_data.out
                rm flake8.out
                rm flake8_ui.out
                rm flake8_api.out
                rm flake8_tgen.out
                rm flake8_net.out
                rm flake8_data.out
                python3 -m flake8 --config ExtremeAutomation/Utilities/flake8/flake8_full.conf --output-file flake8.out --exit-zero ExtremeAutomation/Keywords ExtremeAutomation/Library
                python3 -m flake8 --config ExtremeAutomation/Utilities/flake8/flake8_api.conf --output-file flake8_api.out --exit-zero ExtremeAutomation/Apis
                python3 -m flake8 --config ExtremeAutomation/Utilities/flake8/flake8_rest_data.conf --output-file flake8_data.out --exit-zero ExtremeAutomation/Apis/NetworkElement/GeneratedApis/CommandApis/REST
                python3 -m flake8 --config ExtremeAutomation/Utilities/flake8/flake8_tgen.conf --output-file flake8_tgen.out --exit-zero ExtremeAutomation/Library/Device/TrafficGeneration
                python3 -m flake8 --config ExtremeAutomation/Utilities/flake8/flake8_net.conf --output-file flake8_net.out --exit-zero ExtremeAutomation/Library/Net
                touch flake8.out && touch flake8_ui.out && touch flake8_api.out && touch flake8_tgen.out && touch flake8_net.out && touch flake8_data.out
                cat flake8_ui.out >> flake8.out
                cat flake8_api.out >> flake8.out
                cat flake8_tgen.out >> flake8.out
                cat flake8_net.out >> flake8.out
                cat flake8_data.out >> flake8.out
                '''
            }
        }
    }
      post {
        always {
          recordIssues (
			    tool: flake8(pattern: 'flake8.out'),
			    qualityGates: [[threshold: 1, type: 'TOTAL', unstable: false]]
            )
          junit 'ExtremeAutomation/Unittests/PythonTests/jenkins_reports/*.xml'
        }
      }
      options {
        buildDiscarder(logRotator(numToKeepStr: '30'))
        disableConcurrentBuilds()
        lock resource: 'Unit_Test_Resources'
      }
}
