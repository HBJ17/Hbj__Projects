c = int(input())
station_dct={}
for i in range(c):
    name=input()
    no_coupe=int(input())

    coupe_dct={}

    for j in range(no_coupe):
        data = input()
        coupe_name, passengers = data.split(",")
        coupe_name = coupe_name.strip()
        passengers = int(passengers.strip())
        coupe_dct[coupe_name]=passengers
        k = {k:coupe_dct[k] for k in sorted(coupe_dct)}


    station_dct[name]= k

print(station_dct,end="")


