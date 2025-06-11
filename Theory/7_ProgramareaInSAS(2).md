# Programarea in SAS (2)

- Combinarea seturilor de date se poate face in urmatoarele moduri:

1. `SET` = fuziune unu-la-unu / Concatenare / Interclasare

2. `APPEND` = Adaugare

3. `MERGE` = Fuziune pe baza unei corespondente

## Fuziune 1-la-1

```sas
DATA set-date-iesire
    SET set-date-1
    SET set-date-2
RUN
```

### Setul de date 1 (`set_date_1`)

| id  | nume  |
|-----|--------|
| 1   | Ana    |
| 2   | Vlad   |
| 3   | Irina  |

### Setul de date 2 (`set_date_2`)

| salariu |
|---------|
| 3000    |
| 3500    |
| 4000    |

---

### Fuziunea 1-la-1

| Rând nou | din set_date_1 | din set_date_2 | Rezultatul combinat |
|----------|----------------|----------------|---------------------|
| 1 | id=1, nume=Ana | salariu=3000 | id=1, nume=Ana, salariu=3000 |
| 2 | id=2, nume=Vlad | salariu=3500 | id=2, nume=Vlad, salariu=3500 |
| 3 | id=3, nume=Irina | salariu=4000 | id=3, nume=Irina, salariu=4000 |

- Liniile sunt combinate în ordine strictă, fără chei.

- Daca exista valori comune in cele 2 seturi de date, cele din setul 2 o sa le suprasrie mereu pe cele din setul 1

## Concatenarea

### Ce face?

Această instrucțiune **concatenează două seturi de date** vertical, adică:

- Adaugă rândurile din `set_date_2` **sub** rândurile din `set_date_1`.
- Este echivalent cu o **unire de tip "append"**.

---

### Cod SAS

```sas
DATA set_date_iesire;
    SET set_date_1 set_date_2;
RUN;
```

### Exemplu

#### set_date_1

| id  | nume  |
|-----|-------|
| 1   | Ana   |
| 2   | Vlad  |

#### set_date_2

| id  | nume  |
|-----|-------|
| 3   | Irina |
| 4   | Paul  |

#### Output

| id  | nume  |
|-----|-------|
| 1   | Ana   |
| 2   | Vlad  |
| 3   | Irina |
| 4   | Paul  |

### Observații importante:

- Toate variabilele din ambele seturi trebuie să aibă aceeași structură (aceleași nume și tipuri).

- Dacă set_date_2 conține variabile în plus față de set_date_1, acelea vor fi ignorate (sau create cu valori lipsă, dacă set_date_1 le are).

- Foarte util când faci unificarea mai multor fișiere cu aceeași structură (ex: date lunare, fișiere separate pe regiuni).

## Adăugarea

### Ce face?

Instrucțiunea `PROC APPEND` adaugă rândurile dintr-un set de date **direct la finalul** unui alt set de date existent, **fără a crea un nou set**.

- Este o metodă eficientă pentru a **actualiza un dataset** cu observații noi.
- Funcționează similar cu concatenarea, dar modifică **direct** datasetul de bază (`BASE=`).

---

### Cod SAS

```sas
PROC APPEND BASE=set_date
            DATA=set_date_nou;
RUN;
```

### Exemplu

#### set_date (setul de bază)

| id  | nume  |
|-----|-------|
| 1   | Ana   |
| 2   | Vlad  |

#### set_date_nou (setul de adăugat)

| id  | nume  |
|-----|-------|
| 3   | Irina |
| 4   | Paul  |

#### Output în set_date după PROC APPEND

| id  | nume  |
|-----|-------|
| 1   | Ana   |
| 2   | Vlad  |
| 3   | Irina |
| 4   | Paul  |

### Observații importante

- Variabilele din DATA= trebuie să corespundă exact cu cele din BASE= (nume și tip).
- Dacă BASE= nu există, SAS îl creează automat cu structura din DATA=.
- Dacă există diferențe între variabile și totuși vrei să forțezi adăugarea, folosește opțiunea FORCE:

```sas
PROC APPEND BASE=set_date
            DATA=set_date_nou
            FORCE;
RUN;
```

## Interclasarea

### Ce face?

Instrucțiunea `SET ... BY` realizează o **interclasare ordonată** a două sau mai multe seturi de date, combinând liniile **în ordinea valorilor unei variabile-cheie**.

- Este o formă specială de concatenare, unde SAS **presupune că seturile sunt deja sortate** după variabila specificată în `BY`.
- Permite procesarea datelor în mod secvențial și controlat, de exemplu în calcule cumulative sau analize grupate.

---

### Cod SAS

```sas
DATA set_date_iesire;
    SET set_date_1 set_date_2;
    BY id;
RUN;
```

## Interclasarea

### Ce face?

Instrucțiunea `SET ... BY` realizează o **interclasare ordonată** a două sau mai multe seturi de date, combinând liniile **în ordinea valorilor unei variabile-cheie**.

- Este o formă specială de concatenare, unde SAS **presupune că seturile sunt deja sortate** după variabila specificată în `BY`.
- Permite procesarea datelor în mod secvențial și controlat, de exemplu în calcule cumulative sau analize grupate.

---

### Cod SAS

```sas
DATA set_date_iesire;
    SET set_date_1 set_date_2;
    BY id;
RUN;
```

### Exemplu

#### set_date_1 (sortat după id)

| id  | nume  |
|-----|-------|
| 1   | Ana   |
| 3   | Irina |

#### set_date_2 (sortat după id)

| id  | nume  |
|-----|-------|
| 2   | Vlad  |
| 4   | Paul  |

#### Output

| id  | nume  |
|-----|-------|
| 1   | Ana   |
| 2   | Vlad  |
| 3   | Irina |
| 4   | Paul  |

### Observații importante

- TOATE seturile de date trebuie să fie sortate în prealabil după variabila din BY, altfel SAS va genera o eroare (BY variables are not properly sorted).
- Nu este o îmbinare (merge) — seturile nu sunt combinate pe baza valorii comune, ci doar puse cap la cap în ordine crescătoare.
- Poți folosi FIRST. și LAST. pentru a detecta începutul și sfârșitul fiecărui grup în BY.
