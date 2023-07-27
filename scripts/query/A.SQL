SELECT T0."SlpCode" AS "Codigo", T0."SlpName" AS "Nombre de Asesor", T3."U_GLV_CodSup" AS "Area", T3."U_GLV_NameSup", T2."ItmsGrpNam"
FROM OSLP T0 
INNER JOIN "@GEL_GRUARTXEMPVNT" T1 ON T0."SlpCode" = T1."Name" 
INNER JOIN "OITB"  T2 ON T1."U_GLV_GrupoArt" = T2."ItmsGrpCod" 
INNER JOIN "@SIS_SUPERVISORES"  T3 ON T0."U_GLV_Supervisor" = T3."DocEntry"