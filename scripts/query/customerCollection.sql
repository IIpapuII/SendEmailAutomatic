SELECT T0."CardCode", T0."CardName", T0."LicTradNum", T0."AliasName", T0."Balance", TO_VARCHAR(T1."DocDueDate",'DD/MM/YYYY') AS "Fecha", T0."E_Mail"
FROM {0}.OCRD T0
INNER JOIN {0}.ORIN T1 ON T0."CardCode" = T1."CardCode"
WHERE T0."CardCode" = 'CN1092016542'
ORDER BY T1."DocDueDate"
