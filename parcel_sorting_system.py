# P.S.) This System took me longer than 5 hours to find out the the correct System-architecture (flows) to make it work correctly


sorting_hall = {
    "amsterdam" : "hall-a",
    "rotterdam" : "hall-b",
    "brabant" : "hall-c"
}

def parcel_sorting_centra(city):
    
    # Searching (if) city is in the Database
    if city in sorting_hall:

        # Searching (if) the city holds "is linked to" a sorting-hall
        hall = sorting_hall[city]
        return f"{city} is linked to {hall}"
    else:
        return f"{city} yet not linked to any sorting hall"


# Continue looping headprogram for searching city names
while True:
    name_city = input("Type city name, (or type 'stop' to stop): ").lower()

    # Checking (if) person types "stop", (if) so, end the System by (break)
    if name_city == "stop":
        print("Okay, see you next time!")
        break

    # Give final result of asked city name
    result = parcel_sorting_centra(name_city)
    print(result)
