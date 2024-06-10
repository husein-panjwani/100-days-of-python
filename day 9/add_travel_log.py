travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]


country_key = ["country","visits","cities"]
# contry_final = [country_dict]

def add (countries , visited , cities):
    country_dict = {}
    country_dict["country"] = countries
    country_dict["visites"] = visited
    country_dict["cities"] = cities
    travel_log.append(country_dict)  
    print(travel_log)
               
               
add("Russia", 2, ["Moscow", "Saint Petersburg"])