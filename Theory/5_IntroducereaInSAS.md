# Introducerea in SAS

- Categorii de software pentru prelucrări analitice
  - Instrumente bazate pe foi de calcul: Microsoft Excel
  - Instrumente OLAP: Oracle BI, Power BI, Tableau Software (pivot-table, roll-up, drill-down)
  - Software pentru analize statistice – SAS STAT, SAS EG, SPSS, SYSTAT, STATISTICA
  - Limbaje pentru prelucrări analitice: R, Python
  - Software pentru optimizări: Matlab, CPLEX
  - Instrumente de data mining, text mining

## Sistemul integrat SAS

- SAS este un sistem modular integrat pentru prelucrări analitice.

- SAS consta dintr-un numar mare de module pe care organizatiile le pot achizitiona si instala separat

- BASE SAS este centrul solutiilor SAS, avand facilitati pentru accesul la date, analiza datelor, crearea de rapoarte, etc.

## Programul SAS

- Un program SAS consta dintr-o succesiune de sectiuni (steps) distince trimise catre executie motorului SAS.

- Avem 2 tipuri de sectiuni: `de date` si `de proceduri`

```txt
Fisier TXT ---- |
                |
                | ---- Sectiuni de date ---- Tabela SAS noua ---- Seciune de proceduri ---- Raport
                |
Tabele SAS ---- |
```

- `DATA Step` = Sectiunea de date -> sunt folosite pentru a crea si modifica tabele SAS

- `PROC Step` = Seciunile de proceduri -> sunt folosite pentru a efectua prelucrari si interogari

## Reguli de sintaxa

- Incep cu un cuvant cheie

- Intotdeauna se termina cu punct si virgula

## Exemplu de cod SAS

Un program SAS tipic conține atât secțiuni DATA cât și PROC:

```sas
libname ad_data '/home/nume.prenume';
data ad_data.comenzi;
infile '/home/nume.prenume/comenzi.txt';
    input Nr_Comanda 1-5 ID_Produs $ 2-10
            Cantitate 13-15 PretVanzare 17-22 Valoare 25-32;
run;
proc print data=ad_data.comenzi;
run;
proc means data=ad_data.comenzi;
title 'Analiza comenzilor';
var PretVanzare;
run;
```

- Unul sau mai multe caractere de spaţiere pot fi folosite pentru a separa cuvintele.

- Nu necesita indentare, nu este case-sensitive.

- O singură instructiune se poate scrie pe mai multe rânduri.

- Mai multe instructiuni pot fi scrise pe aceeaşi linie.

## Sectiunile in SAS

- SAS compileaza si executa fiecare sectiune in mod independent

- Limitele unei sectiuni sunt:
  - RUN si QUIT -> exectua sectiunea anterioara -> Limite explicite
  - DATA si PROC -> indica inceputul unei sectiuni -> Limite implicite

- O secţiune de date sau de proceduri se termină atunci când se întâlneşte o altă secţiune, ceea ce înseamnă că prezenţa declaraţiilor RUN şi QUIT nu este obligatorie.

## Crearea seturilor de date din fișiere externe si DATALINES (sau CARDS)

- Dacă datele nu se regăsesc în formatul specific SAS, atunci există următoarele alternative de lucru:
  - Crearea de seturi  de date prin introducerea datelor în codul sursă prin care se crează setul de date (cu DATALINES).
  - Citirea datelor disponibile în fișiere flat. Acestea nu sunt fișiere proprietare, iar înregistrările conțin valori care sunt organizate în câmpuri.
  - Accesarea datelor create prin intermediul altor aplicații, spre exemplu MS Excel, Oracle, SPSS.

```sas
data comanda;
input varsta gen  $ id_prod cantitate data mmddyy8.;
format data yymmdds10.;

datalines;
25 f 02344 2 05/27/10
37 m 08798 4 04/29/10
45 f 09876 1 05/27/10
19 m 07897 3 05/30/10
;

proc sort data=comanda; by descending data;
proc print data=comanda;
title  'Comenzi onorate';
```

- `Default type` este `Numeric`. Folosim `$` pentru caractere (sau siruri de caractere) si `format` pentru date.

## PROC CONTENTS si PROC PRINT

- `Zona de descriere` = conține informații care caracterizează setul de date per ansamblu, cum ar fi numele setului de date, data creării, descrierea fiecărei variabile (nume, tip, lungime) etc. Aceste informații poartă denumirea de metadate. Și pot fi vizualizate cu procedura CONTENTS.

```sas
PROC CONTENTS DATA = set_date;
```

- Zona de date = conține datele propriu-zise ale setului de date, care pot fi vizualizate cu o multitudine de proceduri, printre care cea mai utillizată este PRINT.

```sas
PROC PRINT DATA = set_date;
```

## Tipuri de date

- SAS are 2 tipuri de date: `numeric` si `caracter`

- **Valorile Numerice:** pot memora valori si in format stiintific si sunt implicit stocate pe 8 octeti. Pot memora pana la 32.767 caractere

- - **Valorile Data / Timp:** Sunt stocate ca valori numerice. Valoarea unei date calendaristice in SAS este stocata intern sub forma numarului de zile trecut de la 1 ianuarie 1960 si data specificata, putand fi un numar pozitiv sau negativ

## Biblioteci SAS

- Bibliotaca SAS = colectie care include unul sau mai multe fisiere SAS

```sas
LIBNAME libref 'Biblioteca-SAS'
```

- `LIBNAME` NU are nevoie de RUN pentru a rula

- `Libref` trebuie sa refere un director existent, deoarece prin acesta declaratie nu se creeaza un nou director

### Vizualizarea continutului unei biblioteci

- Se face prin procedura CONTENTS

```sas
PROC CONTENTS DATA = libref.__ALL_NODS;
RUN;
```

## Crearea seturilor de date din fisiere

- Considerând că avem un fişier numit exemplu1.txt care conţine numele, preţul şi categoria a șase tipuri de copaci, fiecare având valoarea separată printr-un spaţiu, acesta ar avea următoarea formă:

```txt
brad 40 conifer
molid 25 conifer
fag 42 foios
stejar 27 foios
liliac 33 arbust
alun 38 arbust 
```

- Citirea in SAS

```sas
data exemplu1;
infile '/home/nume.prenume/exemplu1.txt';
    input Nume $ Pret Categorie $;
run;
```

- **IMPORTANT:** Functioneaza la fel si pentru delimitarea cu virgula, doar ca dupa file path se adauga si `dsd`. Pentru alti delimiatori se adauga `delimiter ='/' (sau alt delimitator)`

## Fisiere cu coloane cu latime fixa

- Cel de-al doilea tip de fişiere flat pe care SAS poate să le citească sunt cele care conţin date în coloane cu lăţime fixă. Pentru acestea există două modalităţi de citire:
  - Column Input
  - Formatted Input

- Avantajul folosirii datelor în coloane cu lăţime fixă consta in:
  - datele pot fi citite în orice ordine
  - valorile lipsă pot fi specificate prin tot atâtea spaţii libere cât are şi lăţimea coloanei.  

- Consideram urmatorul fisier

```txt
brad   40 conifer
molid  25 conifer
fag    42 foioase
stejar 27 foioase
liliac 33 arbusti
alun   38 arbusti
```

```sas
*citire fisier text cu latime fixa: metoda coloane de intrare;
data exemplu3;
    infile "/home/nume.prenume/exemplu3.txt";
    input Nume $ 1-6
          Pret 8-9
          Categorie $ 10-17;
run;
```

- Metoda 2: Intrări formatate poate citi diferite tipuri de formate, cum ar fi monedă (numere având semnul dolar sau euro), numere cu zecimale, date în diferite formate.

- Instructiunea INPUT are umătoarele opţiuni:
  - semnul @ urmat de poziţia de început a variabilei;
  - numele variabilei, formatul variabilei, dacă este necesar;
  - precum şi lăţimea coloanei asociată variabilei.

```sas
*citire fisier text cu latime fixa, metoda intrari formatate;
data exemplu4;
    infile '/home/nume.prenume/exemplu4.txt';
    input @1 Nume $6. 
          @8 Pret dollar3.
          @12 Categorie $7.;
format Pret dollar6.0;
/* 
datalines;
brad   $40 conifer
molid  $25 conifer
fag    $42 foioase
stejar $27 foioase
liliac $33 arbusti
alun   $38 arbusti  */
run;
```

## Atribuirea de etichete

- LABEL atribuie etichete variabilelor din setul de iesire

```sas
LABEL variabila = “Eticheta…”;
```

```sas
***Definire etichete in sectiunea de date;
DATA agenti;
INPUT Cod Oras$ Vanzari;
LABEL Cod = "Cod agent"
      Vanzari = "Vanzari trim I";	
DATALINES;
1101 BZ 100000
1102 CJ 250000
1103 BU 400000
1104 CJ 270000
1105 BU 150000
1106 BZ 80000
;
RUN;
***Utilizare etichete in sectiunea de proceduri;
PROC PRINT DATA =agenti LABEL;
RUN;
***Definire si utilizare etichete in sectiunea de proceduri;
PROC PRINT DATA =agenti LABEL;
LABEL  Oras = "Filiala" Cod = "Cod agent vanzari";
RUN;
```

## Formate de afisare

- `Formate de citire` = ofera instructiuni despre modul cum se citesc datele din fisiere externe

- `Formate de afisare` = ofera instructiuni despre modul cum se vor afisa datele din setul de date

- Definirea de formate

```sas
 PROC FORMAT;
    VALUE <$>nume_format 
                   listă_valori_iniţiale1 = val_afis1 
                           listă_valori_iniţiale2 = val_afis2
                   other = val_afis3;
```

- Se pot defini mai multe formate de afişare în aceeaşi procedură.

- Utilizarea formatului în alte proceduri

```sas
FORMAT variabila <$> nume_format. ;
```

### Utilizarea formatelor de afisare

```sas
***Definire formate definite de utilizator;
PROC FORMAT;
VALUE $oras 'BU'='Bucuresti'
        'BZ'='Buzau'
        'CJ'= 'Cluj'
        other='Gresit';

VALUE nivel low-<100000='Nivel1'
            100000-200000='Nivel2'
            200000<-high='Nivel3';
RUN;

***Aplicare formate definite de utilizator;
PROC PRINT DATA =agenti LABEL;
FORMAT oras $oras. Vanzari nivel.;
RUN;
```

- Folosind simbolul `@@` transmitem ca valorile trebuie sa fie citite de pe aceeasi linie
