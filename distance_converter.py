
name = input ("What is your name?: ")
# Converting to float immediately helps catch errors easily
distance_km = float(input("Enter distance in km: "))

# Calculation
distance_miles = float(distance_km) / 1.609344

print(f'Hi {name.title()}! {distance_km}km is equivalent to {round(distance_miles,1)} miles.')