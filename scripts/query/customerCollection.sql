SELECT T0."CardCode", T0."CardName", T0."LicTradNum", T0."AliasName", T0."Balance", TO_VARCHAR(T1."DocDueDate",'DD/MM/YYYY') AS "Fecha", 
T0."E_Mail", T0."GroupNum",
CASE T0."GroupNum"
WHEN -1 THEN -1
WHEN 1 THEN 30
WHEN 2 THEN 60
WHEN 3 THEN 90
WHEN 5 THEN 10
WHEN 6 THEN 45
WHEN 7 THEN 5
WHEN 8 THEN 8
WHEN 9 THEN 15
WHEN 10 THEN 40
WHEN 11 THEN 3
WHEN 12 THEN 1
WHEN 13 THEN 2
WHEN 14 THEN 25
ELSE -1
END AS "Condicion de pago"
FROM {0}.OCRD T0
INNER JOIN {0}.ORIN T1 ON T0."CardCode" = T1."CardCode"
WHERE T0."CardCode" = {1} --El WHERE no funciona con este codigo
ORDER BY T1."DocDueDate" 
