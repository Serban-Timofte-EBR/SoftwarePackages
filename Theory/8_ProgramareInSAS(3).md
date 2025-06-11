
# Programarea în limbajul SAS – Lecția 4 explicată simplu

## 1. Crearea unui nou set de date în SAS

```sas
DATA nume_dataset;
    instrucțiuni;
RUN;
```

- `DATA` = începi să creezi un nou set de date.
- `RUN;` = finalizezi blocul.

**Exemplu:**

```sas
DATA studenti;
    input nume $ varsta;
    datalines;
Ana 20
Vlad 22
;
RUN;
```

---


## 2. Input: cum introduci date

```sas
INPUT nume_variabila1 tip1 variabila2 tip2 ... ;
```

- `$` se folosește pentru șiruri de caractere (text).
- Numeric = default (nu scrii nimic).

**Exemplu:**

```sas
INPUT varsta gen $ data mmddyy8.;
```

---


## 3. Date speciale (date calendaristice)

```sas
FORMAT nume_variabila format_data;
```

- `mmddyy8.` – așteaptă data în format 05/27/10 (MM/DD/YY).
- `yymmdds10.` – afișează data în format 2010-05-27.

**Exemplu:**

```sas
format data yymmdds10.;
```

---


## 4. Cum sortezi un set de date

```sas
PROC SORT data=nume_dataset;
    BY nume_variabila;
RUN;
```

**Sortare descrescătoare:**

```sas
proc sort data=comanda;
    by descending data;
```

---


## 5. Cum tipărești setul de date

```sas
PROC PRINT data=nume_dataset;
    VAR variabila1 variabila2;
RUN;
```

---


## 6. Mai multe observații pe aceeași linie

```sas
INPUT cod nota @@;
```

- `@@` = permite introducerea mai multor linii de date pe o singură linie.

**Exemplu:**

```sas
DATA studenti;
    INPUT cod nota @@;
    DATALINES;
1101 7 1102 9 1103 10
;
RUN;
```

---


## 7. Citirea fișierelor externe

```sas
LIBNAME libref 'calea/catre/fisier';
DATA libref.nume_dataset;
    INFILE 'fisier.txt';
    INPUT variabile;
RUN;
```

---


## 8. DATALINES vs. INFILE

| Comandă    | Folosită când...                   |
|------------|-------------------------------------|
| `DATALINES` | Datele sunt scrise direct în cod   |
| `INFILE`    | Datele sunt într-un fișier extern  |

---


## 9. LENGTH – setarea dimensiunii pentru variabile text

```sas
LENGTH nume_variabila $dimensiune;
```

**Exemplu:**

```sas
LENGTH categorie $9;
```

---


## 10. Exemplu complet

```sas
DATA produse;
    LENGTH Categorie $9;
    INFILE '/home/nume.prenume/produse.txt';
    INPUT Cod Pret_achizitie Pret_vanzare Categorie $;
RUN;

PROC PRINT data=produse;
    VAR Cod Pret_achizitie Pret_vanzare Categorie;
RUN;
```

---


## 11. Instrucțiunea SELECT (similar cu switch/case)

```sas
SELECT (valoare);
    WHEN (cond1, cond2) instrucțiuni;
    WHEN (altceva) instrucțiuni;
    OTHERWISE instrucțiune_daca_nimic_nu_se_potriveste;
END;
```

**Exemplu simplu:**

```sas
DATA _NULL_;
    a = 7; x = 2;
    SELECT (a);
        WHEN (1,3,5,7) x = x * 100;
        WHEN (2,4,6,8) x = x * 10;
        OTHERWISE;
    END;
    put x=;
RUN;
```

---


## 12. Select pe valori de text (exemplu complex)

```sas
SELECT (Pozitie); 
    WHEN ("FA1") grup ="Flight Attendant I";
    WHEN ("ME1", "ME2", "ME3") grup ="Mechanic";
    WHEN ("PT1") grup ="Pilot I";
    OTHERWISE grup="Other";
END;
```

---


## 13. Scurt despre concatenare, adăugare și interclasare

- `SET A B` → concatenează vertical două seturi.
- `PROC APPEND BASE=A DATA=B;` → adaugă datele din B în A.
- `SET A B; BY id;` → interclasează două seturi sortate după `id`.
