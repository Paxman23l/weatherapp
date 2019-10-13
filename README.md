# weatherapp
SenseHat application for raspberry pi

<!-- # Install Python 3.7.4
sudo chmod +x setup.sh
sudo ./setup.sh -->

# update pip3.7
sudo pip3 install --upgrade pip

# install requirements
sudo pip3 install -r requirements.txt  

# How to run
sudo python3 main.py  

# ENV Variables
ACCOUNT_FOR_CPU_TEMP=true  
METRIC_UNITS=true  
IMPERIAL_UNITS=true  
PRINT_TEMP=true  
OPEN_WEATHER_APIKEY=""  
MISSOULA_GPS=[46.877106,-114.004434]  
GUATEMALA_GPS=[14.614377,-90.469710]
COUCHDB_URL = "SOME_COUCHDB_URL"
COUCHDB_USERNAME="SOME_COUCHDB_USERNAME"
COUCHDB_PASSWORD="SOME_COUCHDB_PASSWORD"
INTERNAL_WEATHER_DATABASE = "SOME_WEATHER_DATABASE" 
EXTERNAL_WEATHER_DATABASE = "SOME_WEATHER_DATABASE" 
ENABLE_STORAGE = False
