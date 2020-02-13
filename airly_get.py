import requests
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--url", help="Airly API url with API_KEY")
parser.add_argument("--air", help="File destination for air quality")
parser.add_argument("--th", help="File destination for temperature and humidity")
parser.add_argument("--pre", help="File destination for air pressure")

args = parser.parse_args()

if args.url:
  try:
    req = requests.get(args.url)
    if req.status_code == 200:
      result = req.json()['current']['values']

      if args.air:
        file = open(args.air, "w")
        file.write(f"{result[2]['value']}\n{result[1]['value']}")
        file.close()

      if args.th:
        file = open(args.th, "w")
        file.write(f"{result[5]['value']}\n{result[4]['value']}")
        file.close()

      if args.pre:
        file = open(args.pre, "w")
        file.write(f"{result[3]['value']}")
        file.close()
    elif req.status_code == 429:
      print("API rate limit was exceeded")
    elif req.status_code == 401:
      print("Please provide API key within a link")


  except requests.RequestException:
    print("URL error, please correct your URL")
  except:
    print("Unexpected error ocurred")
    

else:
  print("Error, you must provide an URL")
