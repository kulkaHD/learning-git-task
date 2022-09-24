print("ZADANIE 1.")

zakupy= {
    "piekarnia": ['chleb', 'pączek', 'bułki'],
    "warzywniak": ['marchew', 'seler', 'rukola']
}
for sklep, rzeczy in zakupy.items():    
    print("Idę do",sklep.capitalize(),", kupuję tu następujące rzeczy: ", [rzecz.capitalize() for rzecz in rzeczy],".")

ilosc = 0
for sklep in zakupy.items():
    ilosc+=len(rzeczy)

print("W sumie kupuję ", ilosc, "produktów.")
#pierwszy commit
#drugi commit, jakże zaskakujący
# raz dwa trzy commita robisz ty

szyfr = (list(map(chr, range(97, 123))))
print(szyfr[3], szyfr[14],szyfr[1],szyfr[17],szyfr[4],szyfr[6],szyfr[14]," ",szyfr[3],szyfr[13],szyfr[8],szyfr[0])