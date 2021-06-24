
sudo apt-get install postgresql postgresql-contrib \ postgis \ git


Sudo apt-get install python-virtualenv
virtualenv venv
cd venv && . bin/activate


git clone https://github.com/wanjohikibui/Geodjango-series.git



sudo -u postgres createuser -P salman
sudo -u postgres createdb -O salman djangogeo
#Enable PostGIS
sudo -u postgres psql -c "CREATE EXTENSION postgis; CREATE EXTENSION postgis_topology;" djangogeo


pip install -r requirements.txt


cd agricom
python manage.py migrate
python manage.py runserver
on browser: localhost:8000
```

