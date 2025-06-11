# Pachete Python pentru procesarea avansata a datelor

- Pipeline-ul (Fluxul) de procesarea a datelor este:

1. Tratarea valorilor lipsa - Procesare Avansata

2. Codificarea valorilor non-numerice
    - 2.1. Procesarea avansata a seturilor mari de date non-numerice

3. Tratarea valorilor extreme

4. Scalarea

`Importanta procesarii datelor`: Etape esentiale pentru pregatirea datelor -> pentru a aplica algoritmi de ML

## Tratarea valorilor lipsa - Valori numerice

- Efect negativ: Modelele esueaza in antrenare

### Elimanarea randurilor sau coloanelor cu valori lipsa

- Eliminam randurile cu cel putin o valoare lipsa

```python
df_dropped_rows = df.dropna()
```

- Eliminam coloanele cu valori lipsa

```python
df_dropped_rows = df.dropna(axis = 1)
```

### Inlocuirea cu media, mediana, valoarea cea mai frecventa sau interpolarea

- Inlocuirea cu valori fixe

```python
df_filled_constant = df.fillna(0)
```

- Inlocuirea cu media

```python
df['A'] = df['A'].fillna(df['A'].mean())
```

- Inlocuirea cu mediana

```python
df['A'] = df['A'].fillna(df['A'].median())
```

- Inlocuirea cu modulul

```python
df['A'] = df['A'].fillna(df['A'].mode()[0])
```

- Inlocuirea liniara

```python
df_interpolated1 = df.interpolate(method='linear')
```

```txt
Original:
0    2.0
1    NaN
2    6.0
```

- `Interpolare liniară:` 1 = 2.0 + (6.0 - 2.0) * (1 / 2) = 4.0

- Inlocuirea cu media

```python
df_interpolated2 = df.interpolate(method='polynomial', order=2)
```

- Forward Fill

```python
df_ffill = df.fillna(method='ffill') # Propaga valoarea anterioara
```

- Backward Fill

```python
df_bfill = df.fillna(method='bfill') # Propaga urmatoarea anterioara
```

### Impunerea avansata folosind metode predictive (MICE, KNN)

- Se utilizeaza modele de ML (scikit-learn) pentru a prezice valorile lipsa

- Implementeaza o regresie liniara pentru a estima valorile lipsa bazate pe alte coloane

```python
from sklearn.linear_model import LinearRegression

df_train = df.dropna()  # Datele fără valori lipsă pentru antrenare

model = LinearRegression()
model.fit(df_train[['A', 'B']], df_train['C'])  # Prezicem C pe baza A și B

# Prezicerea valorilor lipsă
missing_data = df[df['C'].isnull()]  # Extragem rândurile lipsă
df.loc[df['C'].isnull(), 'C'] = model.predict(missing_data[['A', 'B']])
```

- `KNN`: Completeaza valorile lipsa folosind metoda k-Nearest Neighbords

```python
from sklearn.impute import KNNImputer

imputer = KNNImputer(n_neighbors=3)
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
```

#### MICE

- `Concept`: Estimeaza valorile lipsa pe baza relatiilor dintre variabile

- `Proces Iterativ`: Algoritmul parcurge fiecare coloana cu valori lipsa si creeaza un model de regresie separat pentru a estima valorile lipsa in functie de celelalte variabile disponibile

#### LSTM

- `Autoencoders`: Pentru completarea valorilor lipsa

- Invata tipare temporale si pot prezice valorile lipsa pe baza contextului

#### Kalman Filtering

- Utilizeaza model probabilistic pentru a estima valorile lipsa

### Recomandari

- Dacă proporția valorilor lipsă este mică (<5%): metode simple precum media, mediana sau interpolarea.

- Pentru date complexe: MICE sau KNN Imputation.

- În cazul seriilor de timp: interpolarea și propagarea valorilor (bfill, ffill).

- Dacă valorile lipsă sunt multe: elimina coloane/rânduri doar dacă acestea nu sunt relevante pentru analiză.

## Tratarea valorilor lipsa - Valori Non-Numerice

- Necesita metode diferite fata de datele numerice

1. Eliminarea valorilor lipsa

2. Inlocuirea cu o valoarea fixa

3. Inlocuirea cu mode

4. Etichetarea valorilor lipsa

5. Inlocuirea pe baza unei reguli / logici
