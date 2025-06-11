# Pachete Python pentru procesarea avansata a datelor (2)

## Codificarea valorilor non-numerice

- Algoritmii de invatarea automata nu pot procesa sirurile de caractere

### Label Encoding

- Potrivit pentru categorii ordinale

```txt
A -> 0
B -> 1
C -> 2
```

- Exemplu:

```txt
    educatie  educatie_encoded
0      liceu                 1
1  facultate                 0
2     master                 2
3      liceu                 1
4     master                 2
```

### One-Hot Encoding

- Potrivit pentru categorii non-ordonate

- Prin crearea unor coloane binare

- Imaginează că ai un formular unde poți bifa doar un singur răspuns la: Ce culoare îți place?
  - Opțiuni: roșu, verde, albastru
  - Fiecare opțiune va deveni o coloană:

```txt
   culoare_albastru  culoare_rosu  culoare_verde
0                 0              1               0
1                 0              0               1
2                 1              0               0
3                 0              1               0
```

### Target Encoding

- Potrivit pentru modele predictive

- Inlocuirea categoriilor cu medii dintr-o variabila tinta

- Consideram urmatoarele data

```txt
Oraș        Preț (target)
Cluj            200
București       300
Cluj            220
Iași            250
București       280
```

- Calculam media prețurilor pentru fiecare oraș:
  - Cluj: (200 + 220)/2 = 210
  - București: (300 + 280)/2 = 290
  - Iași: 250

```txt
Oraș            Preț (target)       Oraș (encoded)
Cluj                200                 210
București           300                 290
Cluj                220                 210
Iași                250                 250
București           280                 290
```

## Tratarea valorilor extreme

- Valorile extreme pot afecta media, abaterea standard si performanta modelelor, in special pentru algoritmii sensisibili la aceste valori

### Eliminarea outlierilor folosind IQR / Z-Score

- Z-Score = Masoara cate valori ale abaterii medii sunt de la medie pana la valoarea analizata

### Transformari logaritmice

- Reduce impactul valorilor extreme

### Winsorizarea

- Trunchierea outlierilor la o anumita valoarea maxima sau minima

## Scalarea

- Modelele de ML care folosesc distantate (KNN, regresie logistica, retele neuronale) sunt afectate de amplitudinea diferita a variabilelor

### Min-Max Scaling

- Normalizarea valorilor intre 0 si 1

- Implementat prin `MinMaxScaler`

### Standardization (Z-Score)

- Centreaza valorile in jurul meidiei si le exprima in unitati de deviatie standard

- Implementat prin `StandardScaler`

### Robust Scaling

- Foloseste mediana si interquartile pentru a reduce efectul outlierilor

- Implementat prin `RobustScaler`

### Transformer

- `QuantileTransformer`: Transforma datele astfel incat sa urmeze o distributie uniforma sau normala (inlocuieste cu percentilelel acestora). Este utila cand NU sunt distribuite normal si dorim o distributie uniforma sau Gaussiana.

- `Normalizer`: Normalizeaza fiecare rand (vector) astfel incat norma sa fie 1. Foarte utilizat la date spatiale si in NLP (clasificare)
