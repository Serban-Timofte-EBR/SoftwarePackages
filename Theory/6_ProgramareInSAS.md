# Programarea in SAS

- Putem crea noi seturi de date pe baza datelor existente

```sas
DATA set-de-date-SAS-de-iesire;
        SET set-de-date-SAS-de-intrare;
        WHERE expresie-conditionala;
    DROP listă-variabile;
    KEEP listă-variabile;
    LABEL var1=‘eticheta1’ var2=‘eticheta2’;
    FORMAT variabila(le) format.; 
    RUN;
```

- Intr-un astfel de bloc avem dreptul doar la o singura clauza WHERE

- Selectarea variabilelor din setul rezultat se realizează cu ajutorul instructiunilor DROP şi KEEP:
  - DROP listă-variabile; {cu spaţiu  între ele} indica variabilele care se exclud din setul rezultat.
  - KEEP listă-variabile; {cu spaţiu  între ele} indica variabilele care se păstrează în setul rezultat.

- LABEL schimbă modul în care apare numele variabilei în diverse proceduri. Spre exemplu, PROC PRINT poate afişa numele etichetei în loc de numele variabilei:

## Exemplu

- Consideram acest set de date

```sas
DATA produse;
LENGTH Categorie $9;
INFILE'/home/nume.prenume/produse.txt';
INPUT Cod Pret_achizitie Pret_vanzare Categorie $;
RUN;
PROC PRINT DATA=produse;
VAR  Cod Pret_achizitie Pret_vanzare Categorie;
```

- Pornind de la acest set de date, se definesc doua noi variabile
  - Profit_unitar: prin calcul
  - Grup: prin procesare conditionata

```sas
LIBNAME exemple '/home/nume.prenume/';
DATA exemple.produse;
    SET produse;

    Profit_unitar=Pret_vanzare-Pret_achizitie;

    if missing(Pret_vanzare) or Pret_vanzare lt 10 then Grup=1;
    else if Pret_vanzare le 20 then Grup=2;
    else Grup=3;

    DROP Pret_achizitie;
RUN;
```

- Similar funtioneaza si cu sintaxa SQL (cu WHERE IN sau IF ELSE)

## Instructiunea SELECT

```sas
DATA _NULL_; *nu se defineste un set de date;
    a=7; x=2;
    SELECT (a);
        WHEN (2,4,6,8) x=x*10;
        WHEN (1,3,5,7) x=x*100;
        OTHERWISE;
    END;
    put x= ; RUN; 
```

- DATA _NULL_; → nu se creează un set de date, doar se execută codul pentru testare/calcul.

- a = 7, x = 2 → inițializăm două variabile.

- SELECT (a); → evaluăm valoarea lui a, în cazul nostru 7.

- WHEN (2, 4, 6, 8) → nu se aplică (a = 7 nu e aici)

- WHEN (1, 3, 5, 7) → se aplică! ⇒ x = 2 * 100 = 200

- OTHERWISE → se execută doar dacă niciun WHEN nu e valid (nu e cazul aici).

- put x=; → afișează în log: x=200

```sas
DATA salariati;
    SET exemple.salarii;	length grup $ 20;
    SELECT(Pozitie); 
        WHEN ("FA1") grup ="Flight Attendant I";
        WHEN ("FA2") grup ="Flight Attendant II";
        WHEN ("FA3") grup ="Flight Attendant III";
        WHEN ("ME1", "ME2", "ME3") grup ="Mechanic";
        WHEN ("NA1", "NA2", "NA3") grup ="Navigator";
        WHEN ("PT1") grup ="Pilot I";
        WHEN ("PT2") grup ="Pilot II";
        WHEN ("PT3") grup ="Pilot III";
        WHEN ("TA1", "TA2", "TA3") grup ="Ticket Agents";
        OTHERWISE grup="Other"; END;
RUN;
```

- SET exemple.salarii; → ia datele rând cu rând din datasetul exemple.salarii.

- length grup $ 20; → definește coloana grup ca text de max 20 caractere.

- SELECT(Pozitie); → evaluează valoarea din coloana Pozitie.

- În funcție de codul poziției (FA1, PT2, NA3 etc.), se asociază o valoare descriptivă în grup.

- OTHERWISE → se folosește pentru orice cod care nu se regăsește în WHEN (default).

## Procesarea iterativa

- DO UNTIL execută bucla până când expresie devine adevărată. Expresia nu se evaluează până la finalul buclei, ceea ce însemnă că aceasta întotdeuna se execută cel puțin o dată.

- DO WHILE evaluează expresie înainte de intrarea în buclă, cu posibilitatea ca aceasta să nu se execute niciodată.

- Exemplu de combinare a celor două variante de  procesare iterativă:

```sas
 DATA investitie;
    DO an=1 to 10 UNTIL (Capital>=50000);
        Capital +4000;
        Capital+Capital*.10;
    END;
RUN;
```

## Afisarea

- `PUT` converteste valorile de tip numeric la valori de tip caracter

```sas
DATA _NULL_;
    c_data= "2/24/2019";
    c_num= "1234";
    Data_SAS= INPUT(c_data,mmddyy10.);
    Numar = INPUT(c_num,10.);
    PUT Data_SAS= Numar=;
RUN
```

## MISSING & CALL MISSING

- Funcția MISSING preia o valoare numerică sau de tip caracter și returnează “adevărat” dacă valoarea este lipsă și “fals” în caz contrar.

- CALL MISSING reprezintă o rutină care setează toate argumentele sale (numerice sau de tip caracter) cu valoarea nulă

## COMPRESS

- Funcția COMPRESS returnează un șir de caractere prin îndepărtarea anumitor caractere specificate din șirul pe care îl primește ca argument.

- COMPRESS (sir <,lista> <,modificatori>);

- Consideram variabilele

```txt
sir = “XY 01234ABC”
mobil = “(004)0788-51-43-23
```

| Funcție                            | Valoarea returnată   |
|-----------------------------------|-----------------------|
| `COMPRESS("X  Y ABCD")`           | `XYABCD`              |
| `COMPRESS(mobil, " (-)")`         | `0040788514323`       |
| `COMPRESS(sir, "0123456789")`     | `XY ABC`              |
| `COMPRESS(sir, "1234", "k")`      | `1234`                |
| `COMPRESS(mobil, , "kd")`         | `0040788514323`       |
