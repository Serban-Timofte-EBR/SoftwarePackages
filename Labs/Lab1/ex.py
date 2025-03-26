# 1. Să se citească un număr n < 10, să se creeze o listă de numere întregi de dimensiune n și să se adauge elementele citite de la tastatură. Să se ordoneze crescător elementele listei și să se afișeze lista.

n = input("Introdu un numar mai mic ca 10: ")
n = int(n)
lista1 = []

if n > 9:
    print("Numarul trebuie sa fie mai mic deacat 10")
    
for i in range(0,n):
    lista1.append(input(f"Alege numarul pentru pozitia {i+1}: "))

lista1.sort()

print("Lista finala este: ", lista1)

# 2. Să se creeze o lista de 5 elemente cu denumirile unor orașe.
# Să se realizeze o funcție care returnează lungimea fiecărui element (oraș) și să se afișeze lista ordonată descrescător, utilizând opțiunile metodei sort(), în funcție de această lungime.

orase = ["Cluj", "Bucuresti", "Iasi", "Timisoara", "Brasov"]

def getLungimeOras(oras):
    return len(oras)

orase.sort(key=getLungimeOras, reverse=True)

print("Lista de orase: ", orase)

# 3. Să se creeze o listă de liste cu denumiri de echipamente IT (telefon, laptop, tableta, smart_tv), prețul și cantitatea acestora. Calculați valoarea fiecărui echipament, adăugați-o în listă și sortați în funcție de valoare, utilizand functia lamda.

echipamente = [
    ["telefon", 3000, 10],
    ["laptop", 4500, 5],
    ["tableta", 2000, 7],
    ["smart_tv", 4000, 3]
]

for echipament in echipamente:
    valoare = echipament[1] * echipament[2]
    echipament.append(valoare)

echipamente.sort(key=lambda x: x[3], reverse=True)

print("Echipamente sortate după valoare totală (descrescător):")
for e in echipamente:
    print(f"{e[0]} - Pret: {e[1]}, Cantitate: {e[2]}, Valoare: {e[3]}")

# Să se afișeze numele angajatului care este și client.

lista_angajati=['Popescu Vasile','Ionescu Gigel', 'Pop Maria']
lista_clienti=['Ionescu Gigel', 'Costache Ioana', 'Anton Eugenia']

angajati_clienti = [persoana for persoana in lista_angajati if persoana in lista_clienti]

print("Angajati care sunt si clienti: ", angajati_clienti)

# 5. Să se creeze o listă de dicționare cu următoarele chei: id, nume și salariul pentru următorii angajați: Popescu, Ionescu, Vasilescu.
# lista = [{"id":1, "nume":"Popescu", "salariul":5000}, {"id":2, "nume":"Ionescu", "salariul":4000}, {"id":3, "nume":"Vasilescu", "salariul":6000}]
# Dacă angajații au salariul mai mic decât 5000, să se majoreze salariul cu 10%.

lista = [
    {"id": 1, "nume": "Popescu", "salariul": 5000},
    {"id": 2, "nume": "Ionescu", "salariul": 4000},
    {"id": 3, "nume": "Vasilescu", "salariul": 6000}
]

for angajat in lista:
    if angajat["salariul"] < 5000:
        angajat["salariul"] = int(angajat["salariul"] * 1.10)

print("Lista actualizată a angajaților:")
for angajat in lista:
    print(f"ID: {angajat['id']}, Nume: {angajat['nume']}, Salariu: {angajat['salariul']}")
    
# 6. Să se creeze o funcție și să se determine dacă numărul primit ca parametru este sau nu prim.

def este_prim(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numar = int(input("Introdu un nr: "))
if este_prim(numar):
    print(f"{numar} este număr prim.")
else:
    print(f"{numar} nu este număr prim.")
    
numar = int(input("Introdu un nr: "))
if este_prim(numar):
    print(f"{numar} este număr prim.")
else:
    print(f"{numar} nu este număr prim.")
    
    
# 7. Să se creeze o listă li1, formată din primele m numere naturale, apoi să se realizeze o funcție prin care să se creeze o listă li2 formată din numerele prime ale listei li1.

def filtreaza_prime(lista):
    return [numar for numar in lista if este_prim(numar)]

m = int(input("Introdu numărul m: "))

li1 = list(range(m))

li2 = filtreaza_prime(li1)

print("Lista li1:", li1)
print("Lista li2 (numere prime):", li2)