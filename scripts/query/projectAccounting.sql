UPDATE
	{0}."JDT1" T1
SET
	--	Corregir el proyecto de los asiento basados en documentos
	T1."Project" = 
		CASE
			WHEN T1."TransType" = 13 THEN (SELECT TA."Project" FROM {0}."OINV" TA WHERE TA."TransId" = T1."TransId")
			WHEN T1."TransType" = 14 THEN (SELECT TA."Project" FROM {0}."ORIN" TA WHERE TA."TransId" = T1."TransId")
			WHEN T1."TransType" = 30 AND T1."Account" = '13050501' THEN (SELECT TA."ProjectCod" FROM {0}."OCRD" TA WHERE TA."CardCode" = T1."ShortName")
            WHEN T1."TransType" = 321 AND T1."Account" = '13050501' THEN (SELECT TA."ProjectCod" FROM {0}."OCRD" TA WHERE TA."CardCode" = T1."ShortName")
			ELSE T1."Project"
		END
WHERE
	--	Prueba con un asiento para evitar erorres masivos
	T1."TransId" = {1}
	--ifnull(T1."Project",'') = '' AND
	--	Si se quiere actualizar por rango de fechas
	--T1."RefDate" = '{1}'