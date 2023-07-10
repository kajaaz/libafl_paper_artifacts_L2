#!/bin/sh

echo "getting git submodules for EVMs"
git submodule init
git submodule update

echo "building go-ethereum (install go for this)"
make -C ./go-ethereum all

echo "building openethereum (install rust for this)"
make -C ./offchainlabs-go-ethereum all

echo "Installing reqs for us, creating virtualenv"
#virtualenv -p "$(command -v python3)" "$(pwd)/.env"
#. .env/bin/activate
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt

echo "Done building :)"
echo "Activate the virtualenv with:"
echo ". .env/bin/activate"
