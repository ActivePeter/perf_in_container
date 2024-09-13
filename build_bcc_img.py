import os
os.system("git clone https://github.com/iovisor/bcc.git")

os.chdir("bcc")

os.system("docker build -t bcc-docker -f docker/Dockerfile.ubuntu .")

os.system("docker save -o bcc-docker.tar bcc-docker:latest")