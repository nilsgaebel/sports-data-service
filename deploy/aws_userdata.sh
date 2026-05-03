set -e

dnf update -y
dnf install -y git python3-pip

git clone https://github.com/nilsgaebel/sports-data-service.git /app
cd /app

pip install -r requirements.txt
python3 app.py