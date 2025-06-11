# Machine Learning în SAS – Analiza Retenției Clienților

## 1. Importanța retenției clienților

- În sectorul bancar competitiv, fidelizarea clienților este esențială.
- Retenția reduce costurile de achiziție și crește stabilitatea veniturilor.
- Clienții loiali tind să folosească mai multe produse financiare.

## 2. Ce este Churn-ul?

- **Customer churn** = plecarea unui client.
- Motive:
  - Decizii personale (migrare la altă bancă).
  - Probleme externe (neplata creditelor).
- Monitorizarea churn-ului ajută la intervenții prompte.

## 3. Rolul ML în anticiparea churn-ului

- Modelele ML identifică tipare invizibile pentru metodele tradiționale.
- Variabile analizate:
  - Date demografice
  - Istoric tranzacții
  - Frecvența utilizării serviciilor
  - Interacțiuni anterioare
- Se obține un scor de probabilitate de churn → intervenții personalizate.

## 4. Utilizări practice ale ML

- Notificări și recomandări personalizate
- Campanii către clienții inactivi
- Creșterea loialității
- Marketing direcționat

## 5. Avantajele ML față de metodele tradiționale

- Metodele clasice folosesc reguli fixe.
- ML analizează volume mari de date și relații complexe.
- Beneficii:
  - Predicții mai precise
  - Reducerea alertelor false
  - Strategii proactive

## 6. Structura setului de date

- Variabila țintă: `Exited = 1` (client plecat)
- 10 variabile independente (predictori)
- Sursă: [Kaggle dataset](https://www.kaggle.com/datasets/shubhammeshram579/bank-customer-churn-prediction/data)

## 7. Tipuri de ML

### Învățare Supervizată

- Seturi cu etichete (X, y)
- Scop: prezicerea clasei (ex: va pleca / nu va pleca)

### Învățare Nesupervizată

- Seturi fără etichete (X)
- Scop: identificare de grupuri, tipare

## 8. Pipeline-ul în SAS

### Importul datelor

```sas
proc import datafile="C:\cale\fisier.csv"
    out=dataset_sas
    dbms=csv
    replace;
    getnames=yes;
run;
```

### Tratarea valorilor lipsă

```sas
proc freq data=dataset; tables _all_ / missing; run;  /* categorice */
proc means data=dataset; run;                         /* numerice */

proc stdize data=intrare out=iesire method=mean reponly;
    var lista_variabile;
run;
```

### Exploratory Data Analysis (EDA)
- PROC SGPLOT – histograme, KDE
- PROC FREQ – distribuții categorice

### Crearea de variabile noi
- balance_to_salary = balance / estimated_salary
- balance_to_product_ratio = balance / num_of_products
- tenure_to_age = tenure / age

### Encodare variabile

```sas
/* Ex: Gender: 0 = Female, 1 = Male */
/* Geography: 0 = France, 1 = Spain, 2 = Germany */
```

## 9. Corelații

```sas
proc corr data=dataset spearman;
    var lista_variabile;
run;
```

- Coeficient Spearman → corelații monotone (nu neapărat liniare)

## 10. Oversampling
- Realizat în Python cu SMOTETomek:

```python
from imblearn.combine import SMOTETomek
smk = SMOTETomek(random_state=42)
X_resampled, y_resampled = smk.fit_resample(X, y)
```

## 11. Împărțirea datelor și scalare
- Seturi: train/test
- Parametrul SEED pentru reproductibilitate

## 12. Modele de ML

### a. Regresie Logistică
- Estimează probabilitatea de Exited = 1
- Aplică pragul de decizie (ex: 0.5)

Cod SAS:

```sas
proc logistic data=train_data;
    model Exited(event='1') = var1 var2 var3;
run;
```

- Evaluare: matrice de confuzie, ROC curve

### b. Random Forest
- Combate supraînvățarea (overfitting)
- Foarte robust la date zgomotoase

Cod SAS:

```sas
proc hpforest data=train_data;
    target Exited;
    input var1 var2 var3 / level=interval;
run;
```

- Evaluare: matrice de confuzie, ROC curve

## 13. Evaluare modele
- Matrice de confuzie
- Acuratețe, precizie, recall, F1-score
- Curba ROC + AUC
- Praguri ajustabile