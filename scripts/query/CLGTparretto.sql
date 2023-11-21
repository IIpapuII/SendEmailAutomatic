SELECT
	--	DOCUMENTO
              T2."Project" as "Proyecto",
	CASE 
	WHEN T2."WhsCode" IN (006,030) THEN 'CÚCUTA'
	WHEN T2."WhsCode" = '013' THEN 'ARAUCA'
    WHEN T2."WhsCode" = '011' THEN 'OCAÑA'
    WHEN T2."WhsCode" = '010' THEN 'CALI'
    WHEN T2."WhsCode" = '014' THEN 'GIRON'
    WHEN T2."WhsCode" = '019' THEN 'EJE CAFETERO'
	ELSE 'ERROR BODEGA'
	END AS "Sucursal",
	(IFNULL(T4."BeginStr", '') || substring(T1."DocNum", 4)) as "Número Factura",
	YEAR(T1."DocDate") AS "AnioDocumento",
	MONTH(T1."DocDate") AS "MesDocumento",
	TO_VARCHAR(T1."DocDate", 'YYYY-MM-DD') AS "FechaDocumento",
	T4."SeriesName" AS "SerieDocumento",
	T1."DocNum" AS "NumeroDocumento",
	'FV' AS "TipoDocumento",
	--	CLIENTE
	T1."CardCode" AS "CodigoCliente",
	T1."CardName" AS "NombreCliente",
	T5."U_GD_NombComercial" AS "Sigla Comercial",
	T5."LicTradNum" AS "NITCliente",
	T6."GroupName" AS "GrupoCliente",
	T3."StreetS" AS "Direccion",
	T3."BlockS" AS "Barrio",
	T3."U_HBT_MunMedS" AS "Codigo Municipio",
	T13."U_NomMunicipio" AS "Nombre Municipio", 
	--	PRODUCTO
	T2."ItemCode" AS "CodigoProducto",
	T2."Dscription" AS "NombreProducto",
	T7."SalPackUn" AS "Embalaje",
	T2."Quantity" AS "Cantidad",
	TO_INT(T2."Quantity" / T7."SalPackUn") AS "Cajas",
	MOD(T2."Quantity",T7."SalPackUn") AS "Unidades",
	(T2."Price" - (T2."Price" * T1."DiscPrcnt" / 100)) AS "PrecioUnitario",
	(T2."LineTotal" - (T2."LineTotal" * T1."DiscPrcnt" / 100)) AS "SubTotal",
	(T2."VatSum") AS "IVA",
	(T2."LineTotal" - (T2."LineTotal" * T1."DiscPrcnt" / 100) + T2."VatSum") AS "Total",
	--T7."ItmsGrpCod" AS "CodigoGrupoProducto",
	T8."ItmsGrpNam" AS "NombreGrupoProducto",
	--T7."U_GD_SubGrupo" AS "CodigoSubGrupoProducto",
	T9."Name" AS "NombreSubGrupoProducto",
	--T7."U_GD_FamProducto" AS "CodigoFamiliaProducto",
	T10."Name" AS "NombreFamiliaProducto",
	--	VENDEDOR
	T1."SlpCode" AS "CodigoVendedor",
	T11."SlpName" AS "NombreVendedor",
             T2."WhsCode" AS "Bodega",
    T12."WhsName" AS "Descripcion Bodega",
    0 AS "Cod Causal Devolucion",
    
    'NONE' AS "Descripcion Causal Devolucion",
    T1."U_GLV_UID" as "ID Pedido Easy",
   TO_VARCHAR(T1."DocNum") AS "FacturaOrigen",
    T2."DiscPrcnt" AS "% de Descuento",
     A1."PymntGroup" AS "Condición de Pago"
    
--	DOCUMENTO
FROM
	{0}."OINV" T1
INNER JOIN
	{0}."INV1" T2
		ON T1."DocEntry" = T2."DocEntry"
INNER JOIN
	{0}."INV12" T3
		ON T1."DocEntry" = T3."DocEntry"
INNER JOIN
	{0}."NNM1" T4
		ON T1."Series" = T4."Series"
--	CLIENTE
INNER JOIN
	{0}."OCRD" T5
		ON T1."CardCode" = T5."CardCode"
LEFT JOIN {0}."OCTG" A1 ON T5."GroupNum" = A1."GroupNum"
INNER JOIN
	{0}."OCRG" T6
		ON T5."GroupCode" = T6."GroupCode"
--	PRODUCTO
INNER JOIN
	{0}."OITM" T7
		ON T2."ItemCode" = T7."ItemCode"
INNER JOIN
	{0}."OITB" T8
		ON T7."ItmsGrpCod" = T8."ItmsGrpCod"
LEFT JOIN
	{0}."@GD_SUBGRUPO" T9
		ON T7."U_GD_SubGrupo" = T9."Code"
LEFT JOIN
	{0}."@GD_FAMPRODUCTOS" T10
		ON T7."U_GD_FamProducto" = T10."Code"
--	VENDEDOR
INNER JOIN
	{0}."OSLP" T11
		ON T1."SlpCode" = T11."SlpCode"
LEFT JOIN 
	{0}."OWHS" T12
		ON T2."WhsCode" = T12."WhsCode"
LEFT JOIN
	{0}."@HBT_MUNICIPIO" T13
	ON T3."U_HBT_MunMedS" = T13."Code"
WHERE
	T1."DocDate" BETWEEN ADD_DAYS(CURRENT_DATE,-EXTRACT(DAY FROM CURRENT_DATE) + 1) AND CURRENT_DATE
	AND T2."WhsCode" IN ({1})
	AND T8."ItmsGrpCod" IN ({2})
	--AND T1."DocNum" = '10078561'

UNION ALL

SELECT
	--	DOCUMENTO
T2."Project" as "Proyecto",
	CASE 
	WHEN T2."WhsCode" IN (006,030) THEN 'CÚCUTA'
	WHEN T2."WhsCode" = '013' THEN 'ARAUCA'
    WHEN T2."WhsCode" = '011' THEN 'OCAÑA'
    WHEN T2."WhsCode" = '010' THEN 'CALI'
    WHEN T2."WhsCode" = '014' THEN 'GIRON'
    WHEN T2."WhsCode" = '019' THEN 'EJE CAFETERO'
	ELSE 'ERROR BODEGA'
	END AS "Sucursal",
	(IFNULL(T4."BeginStr", '') || substring(T1."DocNum", 4)) as "Número Factura",
	YEAR(T1."DocDate") AS "AnioDocumento",
	MONTH(T1."DocDate") AS "MesDocumento",
	TO_VARCHAR(T1."DocDate", 'YYYY-MM-DD') AS "FechaDocumento",
	T4."SeriesName" AS "SerieDocumento",
	T1."DocNum" AS "NumeroDocumento",
	'NC' AS "TipoDocumento",
	--	CLIENTE
	T1."CardCode" AS "CodigoCliente",
	T1."CardName" AS "NombreCliente",
	T5."U_GD_NombComercial" AS "Sigla Comercial",
	T5."LicTradNum" AS "NITCliente",
	T6."GroupName" AS "GrupoCliente",
	T3."StreetS" AS "Direccion",
	T3."BlockS" AS "Barrio",
	T3."U_HBT_MunMedS" AS "Codigo Municipio",
	T13."U_NomMunicipio" AS "Nombre Municipio", 
	--	PRODUCTO
	T2."ItemCode" AS "CodigoProducto",
	T2."Dscription" AS "NombreProducto",
	T7."SalPackUn" AS "Embalaje",
	-T2."Quantity" AS "Cantidad",
	-TO_INT(T2."Quantity" / T7."SalPackUn") AS "Cajas",
	-MOD(T2."Quantity",T7."SalPackUn") AS "Unidades",
	-(T2."Price" - (T2."Price" * T1."DiscPrcnt" / 100)) AS "PrecioUnitario",
	-(T2."LineTotal" - (T2."LineTotal" * T1."DiscPrcnt" / 100)) AS "SubTotal",
	-(T2."VatSum") AS "IVA",
	-(T2."LineTotal" - (T2."LineTotal" * T1."DiscPrcnt" / 100) + T2."VatSum") AS "Total",
	--T7."ItmsGrpCod" AS "CodigoGrupoProducto",
	T8."ItmsGrpNam" AS "NombreGrupoProducto",
	--T7."U_GD_SubGrupo" AS "CodigoSubGrupoProducto",
	T9."Name" AS "NombreSubGrupoProducto",
	--T7."U_GD_FamProducto" AS "CodigoFamiliaProducto",
	T10."Name" AS "NombreFamiliaProducto",
	--	VENDEDOR
	T1."SlpCode" AS "CodigoVendedor",
	T11."SlpName" AS "NombreVendedor",
             T2."WhsCode" AS "Bodega",
    T12."WhsName" AS "Descripcion Bodega",
    IFNULL(T2."ReturnRsn",0)AS "Cod Causal Devolucion",
    IFNULL((Select t1."Reason" from {0}."ORER" t1 where t1."AbsEntry" = T2."ReturnRsn"),'N/N') AS "Descripcion Causal Devolucion",
    T1."U_GLV_UID" as "ID Pedido Easy",
   CASE T2."BaseType"
		WHEN '234000031' THEN (
			SELECT
				TA."DocNum"
			FROM
				{0}."OINV" TA
			WHERE
				TA."DocEntry" IN (
					SELECT
						TA."BaseEntry"
					FROM
						{0}."RRR1" TA
					WHERE
						TA."DocEntry" = T2."BaseEntry"
					)
			)
		WHEN '13' THEN (
			SELECT
				TA."DocNum"
			FROM
				{0}."OINV" TA
			WHERE
				TA."DocEntry" = T2."BaseEntry"
			)
		ELSE '0'
	END AS "FacturaOrigen",
T2."DiscPrcnt" AS "% de Descuento",
A1."PymntGroup" AS "Condición de Pago"
    
--	DOCUMENTO
FROM
	{0}."ORIN" T1
INNER JOIN
	{0}."RIN1" T2
		ON T1."DocEntry" = T2."DocEntry"
INNER JOIN
	{0}."RIN12" T3
		ON T1."DocEntry" = T3."DocEntry"
INNER JOIN
	{0}."NNM1" T4
		ON T1."Series" = T4."Series"
--	CLIENTE
INNER JOIN
	{0}."OCRD" T5
		ON T1."CardCode" = T5."CardCode"
LEFT JOIN {0}."OCTG" A1 ON T5."GroupNum" = A1."GroupNum"
INNER JOIN
	{0}."OCRG" T6
		ON T5."GroupCode" = T6."GroupCode"
--	PRODUCTO
INNER JOIN
	{0}."OITM" T7
		ON T2."ItemCode" = T7."ItemCode"
INNER JOIN
	{0}."OITB" T8
		ON T7."ItmsGrpCod" = T8."ItmsGrpCod"
LEFT JOIN
	{0}."@GD_SUBGRUPO" T9
		ON T7."U_GD_SubGrupo" = T9."Code"
LEFT JOIN
	{0}."@GD_FAMPRODUCTOS" T10
		ON T7."U_GD_FamProducto" = T10."Code"
--	VENDEDOR
INNER JOIN
	{0}."OSLP" T11
		ON T1."SlpCode" = T11."SlpCode"
LEFT JOIN 
	{0}."OWHS" T12
		ON T2."WhsCode" = T12."WhsCode"
LEFT JOIN
	{0}."@HBT_MUNICIPIO" T13
	on T3."U_HBT_MunMedS" = T13."Code"
WHERE
	T1."DocDate" BETWEEN ADD_DAYS(CURRENT_DATE,-EXTRACT(DAY FROM CURRENT_DATE) + 1) AND CURRENT_DATE
	AND T2."WhsCode" IN ({1})
	AND T8."ItmsGrpCod" IN ({2})
	--AND T1."DocNum" = '10078561'
/*ORDER BY
	"FechaDocumento"*/