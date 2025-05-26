/* (1) Crearea unui set de date SAS din fișiere externe */
/* === Clients_Dataset.csv === */
filename clients '/home/u64222853/Clients_Dataset.csv';

proc import datafile=clients
    out=clients_data
    dbms=csv
    replace;
    getnames=yes;
run;

/* === Employees_Dataset.csv === */
proc import datafile='/home/u64222853/Employees_Dataset.csv'
    out=employees_data
    dbms=csv
    replace;
    getnames=yes;
run;

/* === Sales_Dataset.csv === */
filename sales '/home/u64222853/Sales_Dataset.csv';

proc import datafile=sales
    out=sales_data
    dbms=csv
    replace;
    getnames=yes;
run;

/* === Current_Projects_Dataset.csv === */
filename projects '/home/u64222853/Current_Projects_Dataset.csv';

proc import datafile=projects
    out=projects_data
    dbms=csv
    replace;
    getnames=yes;
run;

proc print data=clients_data (obs=5); run;
proc print data=employees_data (obs=5); run;
proc print data=sales_data (obs=5); run;
proc print data=projects_data (obs=5); run;

/* (2) Crearea și folosirea de formate definite de utilizator */
proc format;
  value sal_range low-50000='Mic' 50001-100000='Mediu' 100001-high='Mare';
run;

proc print data=employees_data;
  format Salary sal_range.;
run;

/* (3) Procesarea iterativă și condițională a datelor */
data seniori;
  set employees_data;
  if ExperienceYears > 10 then Tip = 'Senior';
  else Tip = 'Junior';
run;

/* (4) Crearea de subseturi de date */
data retail_clients;
  set clients_data;
  where Industry = 'Retail';
run;

/* (5) Utilizarea de funcții SAS */
data salarii_modificate;
  set employees_data;
  Bonus = round(Salary * 0.1);
  NumeSimplu = scan(Name, 1); /* prenumele */
run;

/* (6) Combinarea seturilor de date (+SQL) */
/* Merge */
proc sort data=clients_data; by ClientID; run;
proc sort data=projects_data; by ClientID; run;

data merged;
  merge clients_data projects_data;
  by ClientID;
run;

/* proc sql */
proc sql;
  create table joined as
  select a.*, b.ProjectName
  from clients_data as a
  left join projects_data as b
  on a.ClientID = b.ClientID;
quit;

/* (7) Utilizarea de masive (arrays) */
data scoruri_normalizate;
  set employees_data;
  array scoruri{3} ExperienceYears ProjectsWorked PerformanceScore;
  do i = 1 to 3;
    scoruri{i} = scoruri{i} * 10;
  end;
run;

/* (8) Proceduri pentru raportare */
proc report data=employees_data;
  column Name Department Salary;
  define Salary / analysis mean;
run;

/* (9) Proceduri statistice */
proc means data=employees_data mean median min max;
  var Salary ExperienceYears;
run;

proc freq data=projects_data;
  tables Status;
run;

/* (10) Generarea de grafice */
proc sgplot data=sales_data;
  series x=Month y=Revenue;
  title "Evoluția veniturilor";
run;

proc sgplot data=employees_data;
  vbar Department / response=Salary stat=mean;
run;