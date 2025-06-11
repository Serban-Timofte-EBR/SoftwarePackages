# Masivi (Arrays) în SAS

## Ce este un masiv în SAS?

Un masiv (array) este un grup de variabile numerice sau de caractere, denumite generic sub un singur identificator, accesibile printr-un index.

Se utilizează pentru:
- procesarea automată și eficientă a unui grup de variabile;
- evitarea codului repetitiv.

---

## Sintaxa generală

```sas
ARRAY nume_array [n] lista_variabile;
```

- n = numărul de variabile din array.
- lista_variabile = variabile existente sau noi.
- Dacă variabilele nu există, vor fi create automat.
- Poți specifica tipul cu num (numeric) sau $ (caractere).

---

## Exemple simple

1. Array numeric
```sas
ARRAY note [3] nota1 nota2 nota3;
```

Acces:
```sas
note[1] = 10;
note[2] = 9;
```

2. Array caracter
```sas
ARRAY luni [4] $ nume1 nume2 nume3 nume4;
```

## Procesare în buclă

Poți itera printr-un array cu DO:
```sas
DATA exemplu;
	SET studenti;
	ARRAY note [3] nota1-nota3;
	suma = 0;
	DO i = 1 TO 3;
		suma = suma + note[i];
	END;
	media = suma / 3;
RUN;
```

## Observații importante
- Variabilele din array trebuie să fie de același tip (toate numerice sau toate caractere).
- Poți crea array-uri doar în pasul DATA, nu în PROC.
- Array-ul nu este o structură permanentă – dispare după execuția pasului DATA.
- Dacă folosești variabile inexistente, SAS le va crea automat.

---

## Exemple utile

### Calcul automat pe coloane

```sas
DATA salarii;
	SET angajati;
	ARRAY luni [12] luna1-luna12;
	total = 0;
	DO i = 1 TO 12;
		total + luni[i];
	END;
RUN;
```

### Înlocuire condiționată în array

```sas
DATA curatare;
	SET chestionar;
	ARRAY rasp [5] r1-r5;
	DO i = 1 TO 5;
		IF rasp[i] = 9 THEN rasp[i] = .; * înlocuiește cu missing;
	END;
RUN;
```

## Funcții utile împreună cu masivi
- OF – referință scurtă la toți membrii unui array:

```sas
media = MEAN(OF nota1-nota3);
```

Aceștia sunt arrays temporari, nu devin coloane în dataset.

| Concept | Explicație |
|---------|------------|
| ARRAY | Definește un grup de variabile |
| [n] | Dimensiunea array-ului |
| DO i = 1 TO n | Permite iterarea prin variabile |
| note[i] | Acces la o variabilă din array |
| $ | Array de caractere |
| _TEMPORARY_ | Array temporar, doar pentru procesare |