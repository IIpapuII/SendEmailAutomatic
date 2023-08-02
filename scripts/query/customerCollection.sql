SELECT 
    T0."CardCode", 
    T0."CardName", 
    T0."LicTradNum", 
    T0."AliasName", 
    (TOTAL."TotalFacture" - PAYTODAY."PayedUntilNow") AS "Mora",
    TO_VARCHAR(T1."DocDueDate", 'DD/MM/YYYY') AS "Fecha", 
    T0."E_Mail"
FROM {0}.OCRD T0
INNER JOIN {0}.OINV T1 ON T0."CardCode" = T1."CardCode"
LEFT JOIN ( 
    SELECT T0."CardCode", SUM(T0."DocTotal") AS "TotalFacture"
    FROM {0}.OINV T0
    WHERE T0."CardCode" = {1}
    GROUP BY T0."CardCode"
) TOTAL ON T0."CardCode" = TOTAL."CardCode"
LEFT JOIN (
    SELECT T0."CardCode", SUM(T0."PaidToDate") AS "PayedUntilNow"
    FROM {0}.OINV T0
    WHERE T0."CardCode" = {1} 
    GROUP BY T0."CardCode"
) PAYTODAY ON T0."CardCode" = PAYTODAY."CardCode"
WHERE T0."CardCode" = {1} 
AND T1."DocDueDate" = (SELECT MAX(T1."DocDueDate") 
                       FROM {0}.OINV T1 
                       WHERE T1."CardCode" = {1}
                       )