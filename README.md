# Airly file generator for SUPLA_FILESENSORS

#### Python 3.6 or newer required!

Required dependencies
 - requests

to install type `pip install requests`

### How to run
```
chmod 777 airly_get.py
```
```
./airly_get.py --url "https://airapi.airly.eu/v2/measurements/nearest?lat=YOUR_LAT&lng=YOUR_LON&maxDistanceKM=20&apikey=YOUR_API_KEY" --air "/home/pi/air.txt"
```
#### Available arguments:
```
-h, --help  show this help message and exit
--url URL   Airly API url with API_KEY
--air AIR   File destination for air quality
--th TH     File destination for temperature and humidity
--pre PRE   File destination for air pressure
```
#### Setting crontab

Open terminal and type:
```
crontab -e
```
Paste this text at the bottom of the opened file. This cronjob will run every 15 minutes. Make sure you have right permission to that script file
```
*/15 * * * * ./airly_get.py --url "https://airapi.airly.eu/v2/measurements/nearest?lat=YOUR_LAT&lng=YOUR_LON&maxDistanceKM=20&apikey=YOUR_API_KEY" --air "/home/pi/air.txt"

```