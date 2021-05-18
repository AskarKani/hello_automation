// location of this project is /home/repos/Pipeline
def artifactory_repo = "myrepo"   // local repository supported only here.
def repo_url = 'https://github.com/AskarKani/hello_automation.git'
def repo_branch = "master"


node {
    def server = Artifactory.server "ARTIFACTORY"
    def client = Artifactory.newConanClient()
    def serverName = client.remote.add server: server, repo: artifactory_repo
    stage("Get recipe"){
        git branch: repo_branch, url: repo_url
    }
    
    stage("Get dependencies and publish build info"){
        //sh "pip3 install conan"
        sh "conan -v"
        //sh "mkdir -p build"
        //dir ('build') {
          //def b = client.run(command: "install ..")
          //server.publishBuildInfo b
        //}
    }

    stage("Build / Test recipe"){
          sh "conan create . vw/testing -pr=rpi_3bplus"
          //sh "conan build . -if=build -bf=build"
          //sh "ls build"
          //sh "conan remote list"
          sh "conan search"
    }

    stage("Upload packages"){
         //String command= sh "upload \"*\" --all -r ${serverName} --confirm"
        //def b = client.run(command: command)
        //sh " printf 'admin\nAskar@123' | conan upload hello/1.0.0@vw/testing -r artifactory --all --confirm"
        sh "conan upload hello/1.0.0@vw/testing -r artifactory --all --confirm"
    }
    
    //stage("Connecting to Test Environment"){
       //sh "hostname -I"
       //sh "#!/bin/bash"
       //sh "pwd"
        // create the abc.zip file.
       //sh "wget -O abc.zip --auth-no-challenge --user=admin --password=admin http://localhost:8080/job/artifact%20generator/lastSuccessfulBuild/artifact/*"
       
        //sh "sshpass -p 'e3-sdk' ssh -tt -o StrictHostKeyChecking=no developer@192.168.1.100 ls" //list the content in home directory of vmware
        //sh "sshpass -p 'e3-sdk' ssh -tt -o StrictHostKeyChecking=no developer@192.168.1.100 ls jenkins"
        //sh "sshpass -p 'e3-sdk' scp abc.zip developer@192.168.1.100:jenkins"    // ship abc.zip from localhost to vmware.
        //sh "sshpass -p 'e3-sdk' ssh -tt -o StrictHostKeyChecking=no developer@192.168.1.100 ls jenkins" 
    //}
    
    stage("Deploy to rpi 3"){
       //sh "curl -sSf -u 'admin:password' -O 'http://localhost:8082/ui/repos/tree/General/repofromjenkins1/hello.zip'"
       sh "pwd"
       //sh "sshpass -p 'e3-sdk' ssh -tt -o StrictHostKeyChecking=no developer@192.168.1.100 ./mytrigger.sh"  // trigger the script from virtual m/c. change the ip from script also
       sh "sshpass -p 'raspberry' ssh -tt -o StrictHostKeyChecking=no pi@192.168.0.180 /home/pi/deploy/deploy_to_pi.sh"
    }
}

