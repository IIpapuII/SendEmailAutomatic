SELECT T1."U_SeriesName" AS "Nombre Series",
(T1."U_UltimoNumero"- MAX(T0."DocNum")) AS "Numeros Restantes",
DAYS_BETWEEN(CURRENT_DATE,T1."U_FechaFin") AS "Dias Restantes" 
FROM {0}.{1} T0 
INNER JOIN {0}."@HBT_FE_SERIE" T1 ON T0."Series" = T1."U_Series" 
GROUP BY T1."U_SeriesName", T1."U_UltimoNumero",T1."U_FechaFin" 
HAVING (T1."U_UltimoNumero"- MAX(T0."DocNum")) > 0