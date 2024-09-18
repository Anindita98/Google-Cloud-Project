import http.client

conn = http.client.HTTPSConnection("aerodatabox.p.rapidapi.com")

headers = {
    'x-rapidapi-key': ".........",
    'x-rapidapi-host': "aerodatabox.p.rapidapi.com"
}

conn.request("GET", "/airports/search/location?lat=52.31&lon=13.24&radiusKm=50&limit=10&withFlightInfoOnly=true", headers=headers)

res = conn.getresponse()  
data = res.read()

print(data.decode("utf-8"))
response.json()

def icao_airport_codes(latitudes, longitudes):

  list_for_df = []

  for index, value in enumerate(latitudes):

    url = f"https://aerodatabox.p.rapidapi.com/airports/search/location/{value}/{longitudes[index]}/km/100/16"

    querystring = {"withFlightInfoOnly":"true"}

    headers = {
      "X-RapidAPI-Host": "aerodatabox.p.rapidapi.com",
      "X-RapidAPI-Key": "........."
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    list_for_df.append(pd.json_normalize(response.json()['items']))
      
  return pd.concat(list_for_df, ignore_index=True)