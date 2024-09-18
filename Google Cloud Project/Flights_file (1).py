def get_flight_data(icao_list):
    Berlin_Timezone = timezone('Europe/Berlin')
    Today = datetime.now(Berlin_Timezone).date()
    Tomorrow = (Today + timedelta(days=1))
    all_flights = []
    for icao in icao_list:
        flights_items = []
        times = [['00:00', '11:59'], ['12:00', '23:59']]
        for time in times:
            url = f"https://aerodatabox.p.rapidapi.com/flights/airports/icao/{icao}/{Tomorrow}T{time[0]}/{Tomorrow}T{time[1]}"
            querystring = {
                "withleg": "true",
                "direction": "Arrival",
                "withCancelled": "false",
                "withCodeshared": "true",
                "withCargo": "false",
                "withPrivate": "false"
            }
            headers = {
                "X-RapidAPI-Key": ".........",
                "X-RapidAPI-Host": "aerodatabox.p.rapidapi.com"
            }
            
            response = requests.request("GET", url, headers=headers, params=querystring)
            if response.status_code != 200:
                print(f"Error: Failed to fetch data for {icao}. Status code: {response.status_code}")
                continue
            
            try:
                flight_json = response.json() 
            except requests.exceptions.JSONDecodeError:
                print(f"Error: Unable to decode JSON for {icao}. Response: {response.text}")
                continue 

            retrival_time = datetime.now(Berlin_Timezone).strftime('%Y-%m-%d %H:%M')
            if 'arrivals' in flight_json:
                for item in flight_json['arrivals']:
                    flights_items.append({
                        'arrival_airport_icao': icao,
                        'departure_airport_icao': item['departure']['airport'].get('icao', None),
                        'schedule_arrival_time': item['arrival']['scheduledTime'].get('local', None),
                        'flight_number': item.get('number', None),
                        'airline': item['airline'].get('name', 'N/A'),
                        'data_retrive_at': retrival_time
                    })
        
        flight_df = pd.DataFrame(flights_items)
        if not flight_df.empty:
            flight_df['schedule_arrival_time'] = pd.to_datetime(flight_df['schedule_arrival_time']).dt.strftime('%Y-%m-%d %H:%M')
            flight_df['data_retrive_at'] = pd.to_datetime(flight_df['data_retrive_at'])
            all_flights.append(flight_df)
    
    if all_flights:
        return pd.concat(all_flights, ignore_index=True)
    else:
        return pd.DataFrame()