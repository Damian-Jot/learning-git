print("Lista zakupow. Version 2")
lista_zakupow = {
    "warzywniak": ["marchew", "seler", "rukola"],
    "piekarnia": ["chleb", "bułki", "pączki"]
}
print("lista_zakupow:")
for sklep, produkty in lista_zakupow.items():
    print(f"Ide do {sklep}, kupie: {produkty}") 
print("W sumie kupie " + str(len(lista_zakupow["warzywniak"]) + len(lista_zakupow["piekarnia"])) + " produktów.")