print("ZADANIE 1.")

zakupy= {
    "piekarnia": ['chleb', 'pączek', 'bułki'],
    "warzywniak": ['marchew', 'seler', 'rukola']
}
for sklep, rzeczy in zakupy.items():    
    print("Idę do",sklep.capitalize(),", kupuję tu następujące rzeczy: ", [rzecz.capitalize() for rzecz in rzeczy],".")

