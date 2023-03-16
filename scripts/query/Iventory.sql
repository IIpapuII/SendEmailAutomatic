SELECT
	T1."ItemCode" AS "CodigoProducto",
	T1."CodeBars" AS "EAN",
	T1."SuppCatNum" AS "CodigoProveedor",
	T1."ItemName" AS "NombreProducto",
	T3."ItmsGrpNam" AS "NombreGrupoProducto",
	T4."Name" AS "NombreSubGrupoProducto",
	T5."Name" AS "NombreFamiliaProducto",
	T6."WhsCode" AS "Bodega",
	T6."WhsName" as "Nombre de bodega",
	T1."InvntryUom" AS "Presentacion",
	T1."SalPackUn" AS "Embalaje",
	SUM(T2A."InQty" - T2A."OutQty") AS "Stock",
	TO_INT(SUM(T2A."InQty" - T2A."OutQty") / T1."SalPackUn") AS "Cajas",
	MOD(SUM(T2A."InQty" - T2A."OutQty"),T1."SalPackUn") AS "Unidades",
	T2."AvgPrice" AS "CostoPromedio",
	--AVG(T2A."CalcPrice") AS "CostoPromedio",
	T1."LastPurPrc" AS "UltimoPrecioCompra",
	--(SUM(T2A."InQty" - T2A."OutQty") * AVG(T2A."CalcPrice")) AS "TotalCostoPromedio",
	(SUM(T2A."InQty" - T2A."OutQty") * T2."AvgPrice") AS "TotalCostoPromedio",
	(SUM(T2A."InQty" - T2A."OutQty") * T1."LastPurPrc") AS "TotalUltimoPrecioCompra",
	--TO_VARCHAR(T1."LastPurDat", 'YYYY-MM-DD') AS "UltimaFechaCompra",
	TO_VARCHAR((SELECT MAX(TA."DocDate") FROM HBTGELVEZ_CUCUTA."OPCH" TA INNER JOIN HBTGELVEZ_CUCUTA."PCH1" TB ON TA."DocEntry" = TB."DocEntry" WHERE TB."ItemCode" = T1."ItemCode" AND TB."WhsCode" = T6."WhsCode"), 'YYYY-MM-DD') AS "UltimaFechaCompra",
	--TO_VARCHAR(MAX(T2A."DocDate"), 'YYYY-MM-DD') AS "UltimaFechaVenta",
	TO_VARCHAR((SELECT MAX(TA."DocDate") FROM HBTGELVEZ_CUCUTA."OINV" TA INNER JOIN HBTGELVEZ_CUCUTA."INV1" TB ON TA."DocEntry" = TB."DocEntry" WHERE TB."ItemCode" = T1."ItemCode" AND TB."WhsCode" = T6."WhsCode"), 'YYYY-MM-DD') AS "UltimaFechaVenta",
	T1."TaxCodeAP" AS "IVACompra",
	T7."Name" AS "IVACompra Nombre",
	T1."TaxCodeAR" AS "IVAVenta",
	T8."Name" AS "IVAVenta Nombre",
	CASE
		WHEN T1."validFor" = 'Y' THEN 'Activo'
		ELSE 'Inactivo'
	END AS "EstadoGeneral",
	T1."FrozenComm" AS "Comentario",
	CASE
		WHEN T2."Locked" = 'Y' THEN 'Bloqueado'
		ElSE 'Desbloqueado'
	END AS "EstadoAlmacen",
	(SELECT STRING_AGG(TA."BcdCode",',' ORDER BY TA."BcdCode") FROM HBTGELVEZ_CUCUTA."OBCD" TA WHERE TA."ItemCode" = T1."ItemCode" AND TA."BcdCode" <> T1."CodeBars") AS "CodigosBarras"
FROM
	"HBTGELVEZ_CUCUTA"."OITM" T1
INNER JOIN
	"HBTGELVEZ_CUCUTA"."OITW" T2
		ON T1."ItemCode" = T2."ItemCode"
INNER JOIN
	"HBTGELVEZ_CUCUTA"."OINM" T2A
		ON T1."ItemCode" = T2A."ItemCode"
		AND T2."WhsCode" = T2A."Warehouse"
INNER JOIN
	"HBTGELVEZ_CUCUTA"."OITB" T3
		ON T1."ItmsGrpCod" = T3."ItmsGrpCod"
LEFT JOIN
	"HBTGELVEZ_CUCUTA"."@GD_SUBGRUPO" T4
		ON T1."U_GD_SubGrupo" = T4."Code"
LEFT JOIN
	"HBTGELVEZ_CUCUTA"."@GD_FAMPRODUCTOS" T5
		ON T1."U_GD_FamProducto" = T5."Code"
INNER JOIN
	"HBTGELVEZ_CUCUTA"."OWHS" T6
		ON T2A."Warehouse" = T6."WhsCode"
LEFT JOIN
	"HBTGELVEZ_CUCUTA"."OSTC" T7
		ON T1."TaxCodeAP" = T7."Code"
LEFT JOIN
	"HBTGELVEZ_CUCUTA"."OSTC" T8
		ON T1."TaxCodeAR" = T8."Code"
WHERE
	T3."ItmsGrpCod" = {0}
	AND T6."WhsCode"  in ({1})
	AND T2A."DocDate" <= TO_VARCHAR(CURRENT_DATE,'YYYYMMDD')
GROUP BY
	T1."ItemCode",
	T1."CodeBars",
	T1."SuppCatNum",
	T1."ItemName",
	T3."ItmsGrpNam",
	T4."Name",
	T5."Name",
	T6."WhsCode",
	T6."WhsName",
	T1."InvntryUom",
	T1."SalPackUn",
	T1."SalPackUn",
	T2."AvgPrice",
	T1."LastPurPrc",
	T1."LastPurDat",
	T1."TaxCodeAP",
	T7."Name",
	T1."TaxCodeAR",
	T8."Name",
	T2A."Warehouse",
	T1."validFor",
	T1."FrozenComm",
	T2."Locked"
HAVING
	SUM(T2A."InQty" - T2A."OutQty") >= 0
ORDER BY
	T1."ItemCode", T2A."Warehouse"