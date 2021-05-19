// location of this project is /home/repos/Pipeline
def artifactory_repo = "myrepo"   // local repository supported only here.
def repo_url = 'https://github.com/AskarKani/hello_automation.git'
def repo_branch = "master"


node {
    def server = Artifactory.server "ARTIFACTORY"
    def client = Artifactory.newConanClient()
    def serverName = client.remote.add server: server, repo: artifactory_repo
    stage("Fetch Code from git"){
        git branch: repo_branch, url: repo_url
    }
    
    stage("Creating conan package"){
          sh "conan create . vw/testing -pr=rpi_3bplus"
    }

    stage("Upload packages to artifactory"){
        sh "conan upload hello/1.0.0@vw/testing -r artifactory --all --confirm"
    }
    
    stage("Deploy to raspberry pi 3"){
       sh "sshpass -p 'raspberry' ssh -tt -o StrictHostKeyChecking=no pi@192.168.0.180 /home/pi/deploy/deploy_to_pi.sh"
    }
}

