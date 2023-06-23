SELECT
--	DOCUMENTO
	YEAR(T1."DocDate") AS "AnioDocumento",
	MONTH(T1."DocDate") AS "MesDocumento",
	TO_VARCHAR(T1."DocDate", 'YYYY-MM-DD') AS "FechaDocumento",
	T4."SeriesName" AS "SerieDocumento",
	T1."DocNum" AS "NumeroDocumento",
	'FV' AS "TipoDocumento",
	--	CLIENTE
	T1."CardCode" AS "CodigoCliente",
	T1."CardName" AS "NombreCliente",
	T5."LicTradNum" AS "NITCliente",
	T6."GroupName" AS "GrupoCliente",
	T3."StreetS" AS "Direccion",
	T3."BlockS" AS "Barrio",
	T3."U_HBT_MunMedS" AS "Cod Municipio",
              --T12."Name" AS "Municipio",
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
             T2."WhsCode" AS "Bodega"
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
              {0}."@HBT_MUNICIPIO" T12
                            ON T3."U_HBT_MunMedS" = T12."Code"
WHERE
	T1."DocDate" BETWEEN ADD_DAYS(CURRENT_DATE,-EXTRACT(DAY FROM CURRENT_DATE) + 1) AND CURRENT_DATE
	--AND T1."DocNum" = '10078561'

UNION ALL

SELECT
	--	DOCUMENTO
	YEAR(T1."DocDate") AS "AnioDocumento",
	MONTH(T1."DocDate") AS "MesDocumento",
	TO_VARCHAR(T1."DocDate", 'YYYY-MM-DD') AS "FechaDocumento",
	T4."SeriesName" AS "SerieDocumento",
	T1."DocNum" AS "NumeroDocumento",
	'NC' AS "TipoDocumento",
	--	CLIENTE
	T1."CardCode" AS "CodigoCliente",
	T1."CardName" AS "NombreCliente",
	T5."LicTradNum" AS "NITCliente",
	T6."GroupName" AS "GrupoCliente",
	T3."StreetS" AS "Direccion",
	T3."BlockS" AS "Barrio",
	T3."U_HBT_MunMedS" AS "Cod Municipio",
             -- T12."Name" AS "Municipio",
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
             T2."WhsCode" AS "Bodega"
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
              {0}."@HBT_MUNICIPIO" T12
                            ON T3."U_HBT_MunMedS" = T12."Code"
WHERE
	T1."DocDate" BETWEEN ADD_DAYS(CURRENT_DATE,-EXTRACT(DAY FROM CURRENT_DATE) + 1) AND CURRENT_DATE
	--AND T1."DocNum" = '10078561'
/*ORDER BY
	"FechaDocumento"*/