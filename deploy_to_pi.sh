# !/bin/sh 

export PATH=$PATH:/home/pi/.local/bin
echo $PATH 
rm -rf /home/pi/deploy/conan_package
conan install hello/1.0.0@vw/testing -g deploy -pr=rpi_3bplus -r artifactory -if=/home/pi/deploy/conan_package

echo "Running the binary......" 
/home/pi/deploy/conan_package/hello/bin/hello
