# Conectarea la baze de date Oracle

- In Python se utilieaza pachetul `oracledb`

- Pachetul cx_Oracle – premergator lui oracledb, conține metode pentru realizarea unei conexiuni cu o bază de date Oracle, pentru gestiunea interogărilor și a tranzacțiilor (comenzile SELECT/INSERT/UPDATE/DELETE/MERGE și COMMIT/ROLLBACK).

- Lista completă a metodelor pachetului oracledb este disponibilă [aici](https://python-oracledb.readthedocs.io/en/latest/user_guide/introduction.html)

- In cadrul conexiunii se precizează: userul, parola, serverul (host/ip) și denumirea bazei de date (service name/SID).

## Exemplu de conectare

Pentru realizarea conexiunii cu serverul oracle care rulează pe *IP-ul 193.226.34.57* cu *service_name orclpdb.docker.internal*, *nume utilizator ms_dba1* și *parola oracle* se inițializează conexiunea următoare:

```python
connection = oracledb.connect(user="MS_DBA1", password="oracle", dsn="193.226.34.57:1521/orclpdb.docker.internal")
```

## Cursorul

- Pentru gestiunea interogarilor / tranzactiilor se utilizeaza un cursor

```python
cursor = connection.cursor()
```

- Variabila de tip cursor dispune de toate metodele necesare gestiunii tranzacțiilor și procesării interogărilor.

| Metoda                       | Explicații                                                                                      |
|-----------------------------|--------------------------------------------------------------------------------------------------|
| `cursor.execute(comanda SQL, parametri)` | Execută comanda SQL specificată împreună cu lista de parametri. În cazul SELECT, cursorul este încărcat cu înregistrările returnate. |
| `cursor.close()`            | Închide cursorul și eliberează zona de memorie alocată.                                         |
| `cursor.fetchone()`         | Încarcă o singură înregistrare din cursor într-o variabilă locală Python.                       |
| `cursor.fetchmany(n)`       | Încarcă următoarele `n` înregistrări din cursor.                                                |
| `cursor.fetchall()`         | Încarcă toate înregistrările rămase din cursor într-o listă de tupluri.                        |
| `cursor.prepare(comanda SQL)` | Transmite comanda SQL către cursor fără a o executa.                                            |
| `cursor.rowcount`           | Returnează numărul de înregistrări parcurse din cursor. Inițial este 0 și crește la fetch.     |
| `cursor.bindarraysize`      | Precizează dimensiunea cursorului, utilă mai ales la comenzile de tip INSERT.                  |
| `cursor.setinputsizes()`    | Precizează tipul de date al parametrilor, folosit mai ales la comenzi INSERT.                  |

## Exemplu complet de utilizare a cursorului

```python
cursor.execute("""SELECT * FROM t_clienti_leasing""")

for rec in cursor:
    print("Values:", rec)

cursor.close()
connection.close()
```

- Cursorul este încărcat cu tuplurile returnate de interogare.

- Parcurgerea se face cu for rec in cursor.

- După utilizare, este recomandat să se închidă atât cursorul (cursor.close()), cât și conexiunea (connection.close()).

## Exemple interogari

- Să se returneze numele, profesia, venitul anual și suma solicitată în cazul clienților care au solicitat mai mult de 5000 lei credit.

```python
import oracledb
from pprint import pprint

# Realizarea conexiunii cu serverul Oracle
connection = oracledb.connect(user="MS_DBA1", password="oracle", dsn="193.226.34.57:1521/orclpdb.docker.internal")
cursor = connection.cursor()

cursor.execute("""SELECT nume_client, profesia, venit_anual  
                 FROM t_clienti_leasing 
                 WHERE suma_solicitata > 5000""")

lista_clienti = cursor.fetchall()

# Inchidere cursor si conexiune
cursor.close()
connection.close()

# Afisare lista clienti
print(lista_clienti)
```

## Exemplu cu parametri de interogare

- Să se returneze valoarea totală a daunelor înregistrate pentru o anumită marcă auto introdusă de utilizator de la tastatură.

```python
import oracledb
from pprint import pprint

# Realizarea conexiunii cu serverul Oracle
connection = oracledb.connect(user="MS_DBA1", password="oracle", dsn="193.226.34.57:1521/orclpdb.docker.internal")
cursor = connection.cursor()

v_marca = input("Introduceti marca: ")

cursor.execute("""
    SELECT marca, sum(valoare_dauna) Total_daune  
    FROM t_clienti_daune 
    WHERE lower(marca) LIKE :p_marca 
    GROUP BY marca
""", p_marca='%'+v_marca.lower()+'%')

lista_daune = cursor.fetchall()

# Inchidere cursor si conexiune
cursor.close()
connection.close()

# Afisare lista marci cu daune
print(lista_daune)
```

## Controlul tranzactiilor

- Operatiile de INSERT, UPDATE si DELETE sunt realizate tot prin intermediul unui cursor folosind metoda execute.

- În cazul INSERT, se pot transmite mai multe înregistrări prin metoda executemany(). În acest caz se recomandă să se precizeze numărul de înregistrări prin proprietatea bindarraysize și tipul parametrilor prin metoda setinputsizes.

- Tranzacțiile se pot finaliza sau anula prin precizarea opțiunilor COMMIT sau ROLLBACK ale conexiunii: connection.commit() sau connection.rollback()

- Se poate seta modul de gestiune a tranzacțiilor prin metoda connection.autocommit=True

## Exemplu insert

- Să se adauge o listă de tupluri în tabela CLIENTI_NOI care are următoarea structură: id_client number, nume_client varchar2(150), profesia varchar2(150), sex varchar2(3), varsta number, stare_civila varchar2(1), suma_solicitata number. Să se finalizeze tranzacția și apoi să se returneze înregistrările noi adăugate.

```python
import oracledb
from pprint import pprint

# Realizarea conexiunii cu serverul Oracle
connection = oracledb.connect(user="MS_DBA1", password="oracle", dsn="193.226.34.57:1521/orclpdb.docker.internal")

lista_clienti_noi = [
    (100, "Popa Marcel", "Inginer", "m", 34, "C", 230),
    (101, "Popa Vasilica", "Coafeza", "f", 32, "C", 200),
    (102, "Popa Ion", "Instalator", "m", 64, "C", 120)
]

cursor = connection.cursor()

# Adaugarea listei de clienti noi in tabela
cursor.bindarraysize = 3
cursor.setinputsizes(int, 150, 150, 3, int, 1, float)
cursor.executemany("INSERT INTO clienti_noi(id_client, nume_client, profesia, sex, varsta, stare_civila, suma_solicitata) VALUES (:1, :2, :3, :4, :5, :6, :7)", lista_clienti_noi)
cursor.close()

# Finalizarea tranzactiei
connection.commit()

# Interogarea bazei de date pentru vizualizarea inregistrarilor noi adaugate
cursor2 = connection.cursor()
cursor2.execute("""SELECT * FROM clienti_noi WHERE nume_client LIKE 'Popa%'""")
lista_clienti = cursor2.fetchall()
pprint(lista_clienti)
cursor2.close()

connection.close()
```

### Anularea tranzacției

Pentru a anula tranzacția, se poate înlocui `connection.commit()` cu `connection.rollback()`:

```python
# Anularea tranzactiei in loc de finalizare
connection.rollback()
```
