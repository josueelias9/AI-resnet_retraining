#!/bin/bash

# ---------------------------
# antes de ejecutar bash
# ---------------------------

# actualizar sistema
sudo apt update
sudo apt upgrade -y
sudo apt install python3-pip -y

# install github cli for ubuntu
# https://github.com/cli/cli/blob/trunk/docs/install_linux.md
type -p curl >/dev/null || sudo apt install curl -y
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg \
&& sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg \
&& echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
&& sudo apt update \
&& sudo apt install gh -y

# hay que crear token. Reemplazar "xxx" por el token creado.
# https://docs.github.com/es/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token#creating-a-token
export GH_TOKEN=xxx

# crear carpeta de trabajo y bajar repositorio
mkdir proyecto
cd proyecto
gh repo clone josueelias9/AI-resnet_retraining

# virtual env
cd AI-resnet_retraining/django_temp
sudo apt install python3.10-venv -y
python3 -m venv venv
source ./venv/bin/activate
pip3 install -r requirements.txt