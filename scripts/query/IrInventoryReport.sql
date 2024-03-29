SELECT
	D1."CodigoProducto",
	D1."EAN",
	D1."NombreProducto",
	D1."NombreSubGrupoProducto",
	D1."NombreFamiliaProducto",
	D1."Nombre de bodega",
	D1."Nombre de Proveedor",
	D1."Presentacion",
	D1."Embalaje",
	D1."Stock",
	TO_INT(D1."Stock" / D1."Embalaje") AS "Cajas",
	MOD(D1."Stock", D1."Embalaje") AS "Unidades",
	(D1."Stock" * D1."UltimoPrecioCompra") AS "TotalUltimoPrecioCompra",
	D1."UltimaFechaCompra",
	D1."UltimaFechaVenta",
	D1."UltimaFechaKardex",
	D1."Dias",
	CASE
		WHEN D1."Dias" >= 60 AND D1."Dias" <= 90 THEN (D1."Stock" * IFNULL(D1."UltimoPrecioCompra",D1."UltimoCostoGeneral"))
	END AS "60 - 90 Dias",
	CASE
		WHEN D1."Dias" > 90 AND D1."Dias" <= 180 THEN (D1."Stock" * IFNULL(D1."UltimoPrecioCompra",D1."UltimoCostoGeneral"))
	END AS "91 - 180 Dias",
	CASE
		WHEN D1."Dias" > 180 THEN (D1."Stock" * IFNULL(D1."UltimoPrecioCompra",D1."UltimoCostoGeneral"))
	END AS "> 180 Dias"

	
FROM (
	SELECT
		T1."ItemCode" AS "CodigoProducto",
		T1."CodeBars" AS "EAN",
		T1."SuppCatNum" AS "CodigoProveedor",
		T1."ItemName" AS "NombreProducto",
		T3."ItmsGrpNam" AS "NombreGrupoProducto",
		T4."Name" AS "NombreSubGrupoProducto",
		T5."Name" AS "NombreFamiliaProducto",
		T6."WhsCode" AS "Bodega",
		T6."WhsName" AS "Nombre de bodega",
		T3."ItmsGrpNam" AS "Nombre de Proveedor",
		T1."InvntryUom" AS "Presentacion",
		T1."SalPackUn" AS "Embalaje",
		(SELECT
			IFNULL(SUM(TA."InQty" - TA."OutQty"),0)
		FROM
			{0}."OINM" TA
		WHERE
			TA."ItemCode" = T1."ItemCode"
			AND TA."Warehouse" = T2."WhsCode"
			AND TA."DocDate" <= CURRENT_DATE
		) AS "Stock",
		T2."AvgPrice" AS "CostoPromedio",
		(SELECT
			MAX(TB."Price")
		FROM
			{0}."OPCH" TA
		INNER JOIN
			{0}."PCH1" TB
				ON TA."DocEntry" = TB."DocEntry"
		WHERE
			TB."ItemCode" = T1."ItemCode"
			AND TB."WhsCode" = T6."WhsCode"
			AND TA."DocDate" <= CURRENT_DATE
		) AS "UltimoPrecioCompra",
		TO_VARCHAR(
			(SELECT
				MAX(TA."DocDate")
			FROM
				{0}."OPCH" TA
			INNER JOIN
				{0}."PCH1" TB
					ON TA."DocEntry" = TB."DocEntry"
			WHERE
				TB."ItemCode" = T1."ItemCode"
				AND TB."WhsCode" = T6."WhsCode"
				AND TA."DocDate" <= CURRENT_DATE
			),
			'YYYY-MM-DD'
		) AS "UltimaFechaCompra",
		TO_VARCHAR(
			(SELECT
				MAX(TA."DocDate")
			FROM
				{0}."OINV" TA
			INNER JOIN
				{0}."INV1" TB
					ON TA."DocEntry" = TB."DocEntry"
			WHERE
				TB."ItemCode" = T1."ItemCode"
				AND TB."WhsCode" = T6."WhsCode"
				AND TA."DocDate" <= CURRENT_DATE
			),
			'YYYY-MM-DD'
		) AS "UltimaFechaVenta",
		TO_VARCHAR(
			(SELECT
				IFNULL(MAX(TA."DocDate"),'20220930')
			FROM
				{0}."OINM" TA
			WHERE
				TA."ItemCode" = T1."ItemCode"
				AND TA."Warehouse" = T2."WhsCode"
				AND TA."DocDate" <= CURRENT_DATE
			),
			'YYYY-MM-DD'
		) AS "UltimaFechaKardex",
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
		(SELECT
			STRING_AGG(TA."BcdCode",',' ORDER BY TA."BcdCode")
		FROM
			{0}."OBCD" TA
		WHERE
			TA."ItemCode" = T1."ItemCode"
			AND TA."BcdCode" <> T1."CodeBars"
		) AS "CodigosBarras",
		T1."LastPurPrc" AS "UltimoCostoGeneral",
		DAYS_BETWEEN(
			IFNULL(
				(SELECT
					MAX(TA."DocDate")
				FROM
					{0}."OPCH" TA
				INNER JOIN
					{0}."PCH1" TB
						ON TA."DocEntry" = TB."DocEntry"
				WHERE
					TB."ItemCode" = T1."ItemCode"
					AND TB."WhsCode" = T6."WhsCode"
					AND TA."DocDate" <= CURRENT_DATE
				),
				(SELECT
					IFNULL(MAX(TA."DocDate"),'20220930')
				FROM
					{0}."OINM" TA
				WHERE
					TA."ItemCode" = T1."ItemCode"
					AND TA."Warehouse" = T2."WhsCode"
					AND TA."DocDate" <= CURRENT_DATE
				)
			),
			CURRENT_DATE
		) AS "Dias"

	FROM
		{0}."OITM" T1
	INNER JOIN
		{0}."OITW" T2
			ON T1."ItemCode" = T2."ItemCode"
	INNER JOIN
		{0}."OITB" T3
			ON T1."ItmsGrpCod" = T3."ItmsGrpCod"
	LEFT JOIN
		{0}."@GD_SUBGRUPO" T4
			ON T1."U_GD_SubGrupo" = T4."Code"
	LEFT JOIN
		{0}."@GD_FAMPRODUCTOS" T5
			ON T1."U_GD_FamProducto" = T5."Code"
	INNER JOIN
		{0}."OWHS" T6
			ON T2."WhsCode" = T6."WhsCode"
	LEFT JOIN
		{0}."OSTC" T7
			ON T1."TaxCodeAP" = T7."Code"
	LEFT JOIN
		{0}."OSTC" T8
			ON T1."TaxCodeAR" = T8."Code"
	WHERE
		T3."ItmsGrpCod" IN ({2})
		AND T6."WhsCode" IN ({1})
) AS D1
WHERE
	D1."Stock" > 0 AND
	D1."Dias" >= 60
ORDER BY
	D1."CodigoProducto", D1."Bodega"