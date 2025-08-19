@NonCPS
def reverseString(str) {
    return str.reverse()
}
pipeline {
    agent any

    // ==============================================
    // Environment Constants
    // Used for consistent paths, cache dirs, reports, etc..
    // Best practice: avoids hardcoding paths in multiple places
    // ==============================================
    environment {
        ARTIFACT_DIR = 'artifacts'      // Where build artifacts are stored
        REPORT_DIR   = 'reports'        // Test or quality reports
        CACHE_DIR    = '.ci-cache'      // Cache directory for dependencies
        PYTHON_HOME  = '/usr/bin/python3' // Python executable
    }

    // ==============================================
    // Parameters
    // Make pipeline flexible: environment choice, optional Python execution
    // ==============================================
    parameters {
        choice(name: 'ENV', choices: ['dev','qa','prod'], description: 'Select target environment')
        booleanParam(name: 'RUN_PYTHON', defaultValue: true, description: 'Run Python scripts?')
    }

    // ==============================================
    // Pipeline Options
    // Timestamps, build retention, timeout, disable concurrent builds
    // ==============================================
    options {
        timestamps()                     
        buildDiscarder(logRotator(numToKeepStr: '10')) 
        timeout(time: 30, unit: 'MINUTES') 
        disableConcurrentBuilds()        
    }

    stages {

        // ==============================================
        stage('Checkout') {
            steps {
                echo "Checking out source code from GitHub"
                git branch: 'main', url: 'https://github.com/Simrankaurbumrah/best_practices_demo.git'
            }
        }

        // ==============================================
        // Dynamic Parallel Stage
        // Demonstrates how to run multiple builds/tests/scripts in parallel dynamically
        // Benefits: faster builds, modular stages, easily extendable
        // ==============================================
        stage('Dynamic Parallel Build & Test') {
            steps {
                script {
                    // --------------------------
                    // Closure: reusable logging function
                    // --------------------------
                    def logInfo = { msg -> echo "[INFO] ${msg}" }

                    // --------------------------
                    // Map to hold parallel stages
                    // Key = stage name, Value = closure that contains steps
                    // --------------------------
                    def parallelStages = [:]

                    // --------------------------
                    // Java Build Stage
                    // --------------------------
                    parallelStages['Java Build'] = {
                        node {
                            logInfo("Running Maven build for Java project...")
                            // Uncomment for real build: sh 'mvn clean install'
                        }
                    }

                    // --------------------------
                    // Node Build Stage
                    // --------------------------
                    parallelStages['Node Build'] = {
                        node {
                            logInfo("Installing npm packages for Node project...")
                            // Uncomment for real build: sh 'npm install'
                        }
                    }

                    // --------------------------
                    // Python Scripts Stage
                    // Loops + Non-CPS usage
                    // Only run if RUN_PYTHON is true
                    // --------------------------
                    if (params.RUN_PYTHON) {
                        parallelStages['Python Scripts'] = {
                            node {
                                logInfo("Executing Python scripts dynamically...")
                                def scripts = ['etl.py','validation.py','reporting.py']

                                // Loop through scripts (iterative execution)
                                scripts.each { s ->
                                    echo "Running Python script: ${s}"
                                    // sh "${PYTHON_HOME} scripts/${s}"  // Uncomment for real execution
                                }

                                // --------------------------
                                // Non-CPS Example: simple string reversal
                                // Useful for computations that don’t require Jenkins CPS serialization
                                // --------------------------
                                // Non-CPS Example: Reverse strings
                                // Shows loop + Non-CPS usage
                                // --------------------------
                                def words = ['Pipeline','Demo','Python']
                                for (w in words) {  // Loop through each word
                                    def reversed = reverseString(w)  // Call Non-CPS method
                                    echo "Original: ${w}, Reversed (Non-CPS): ${reversed}"
                                }
                            }
                        }
                    }

                    // --------------------------
                    // Quality Gates Stage
                    // Example: can run tests, linting, SonarQube, etc.
                    // --------------------------
                    parallelStages['Quality Gates'] = {
                        node {
                            logInfo("Running tests & quality gates...")
                            // Uncomment for real test: sh 'pytest tests/'
                        }
                    }

                    // --------------------------
                    // Execute all defined stages in parallel
                    // This is dynamic: you can add/remove stages in the map and pipeline adapts automatically
                    // --------------------------
                    parallel parallelStages
                }
            }
        }

        // ==============================================
        // stage('Artifacts & Caching')
        // // Demonstrates usage of environment constants
        // // Archives build artifacts and uses caching directories
        // // ==============================================
        stage('Artifacts & Caching') {
            steps {
                echo "Archiving build artifacts to ${ARTIFACT_DIR}"
                echo "Using cache directory: ${CACHE_DIR}"
                // Example commands:
            }
        }
    }
}
