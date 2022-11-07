#!/bin/bash

# ======= 1 =======
# attach volume
# https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-using-volumes.html

sudo mkfs -t xfs /dev/xvdf
sudo mkdir /data
sudo mount /dev/xvdf /data


# ======= 2 =======
# da permisos porque si no nolevanta
sudo chmod 777 /data


# ======= 3 =======
# install docker y docker compose
# https://docs.docker.com/engine/install/ubuntu/

sudo apt-get remove docker docker-engine docker.io containerd runc

sudo apt-get update
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin


# ======= 4 =======
# si hay problemas ejecutar el comando que dice ahi
# https://newbedev.com/javascript-got-permission-denied-while-trying-to-connect-to-the-docker-daemon-socket-at-unix-var-run-docker-sock-get-http-2fvar-2frun-2fdocker-sock-v1-24-containers-json-all-1-dial-unix-var-run-docker-sock-connect-permission-denied-a-code-example
sudo chmod 666 /var/run/docker.sock


# ======= 5 =======
# instalar contenedor de tensorflow. Notar que se modifico el segundo comando para habilitar volumenes: "/data:/home"
# /data: es la carpeta donde estara todas nuestras imagenes. Esta carpeta estara en el servidor
# /home: es la carpeta del contenedor. Recordar que el contenedor corre dentro del servidor.
# https://www.tensorflow.org/install
docker pull tensorflow/tensorflow:latest  # Download latest stable image
docker run -it -p 8888:8888 -v /data/josue:/tf/josue -w /tf/josue --gpus all tensorflow/tensorflow:latest-jupyter  # Start Jupyter server 