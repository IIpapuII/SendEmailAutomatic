SELECT DISTINCT 
	T0."Project",
	T0."TransId"
FROM
	{0}.JDT1 T0
WHERE
	T0."Project" IS NULL
	AND T0."Account" = '13050501'
	AND T0."TransType" IN (30, 14, 13, 321) 