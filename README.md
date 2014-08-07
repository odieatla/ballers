ballers
=======

Server OS: Ubuntu 14.04 LTS

Server Commands:

sudo apt-get update 
sudo apt-get install python-pip 
sudo pip install Django  (1.6.5, latest production version) 
sudo apt-get install python-psycopg2 (for postgres)
sudo apt-get install postgresql-client (install postgres client)
### deploy ###
pip install gunicorn
sudo apt-get install nginx

run in development mode:
ubuntu@ip:~/ballers$ python manage.py runserver 0.0.0.0:8000

run in production mode:
ubuntu@ip-172-31-4-40:~/ballers/config$ gunicorn ballers_wsgi:application --bind 0.0.0.0:8002

EC2 Security Group, Inbound, open ports:
22, 8000,8002, 8080, 5432
