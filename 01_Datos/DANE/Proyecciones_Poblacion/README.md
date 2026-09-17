# Proyecciones de población municipal

**4 archivos versionados**, más 1 original pesado que está en esta carpeta pero no se versiona.

| Archivo | Cat. | Contenido |
|---|---|---|
| `POBLACION MUNICIPAL.xlsx` | B | Proyecciones DANE de población municipal 2025 (hojas base y Rangos_Quintenios). |
| `PPED-AreaSexoEdadMun-2018-2042_VP__PobMunicipalxAreaSexoEdad.parquet` | D | Proyecciones por área, sexo y edad simple 2018-2042: 84.229 filas × 312 columnas. Encabezado de dos niveles combinado como "GRUPO - subcolumna". |
| `PPED-AreaSexoEdadMun-2018-2042_VP__Indice.parquet` | D | Portada del archivo de proyecciones (texto). |
| `PPED-AreaSexoEdadMun-2018-2042_VP__PPED.parquet` | D | Notas metodológicas del archivo de proyecciones (texto). |

`PPED-AreaSexoEdadMun-2018-2042_VP.xlsx` (126 MiB) está en esta carpeta, pero no se versiona por su tamaño: no aparece en un clon del repositorio. Su MD5 está en el registro y el protocolo de conversión, en `00_Documentacion/`, sección 10.

**Serie de referencia (2026-09-17): PPED 2018-2042**, en sus tres parquet. `POBLACION MUNICIPAL.xlsx` (1985-2035) queda como no vigente: no es la misma serie en otro formato, porque 6.722 de las 6.750 combinaciones de municipio, año y área que comparten tienen un total distinto, con 6,3 % de diferencia media. El repositorio no tiene, por ahora, población de referencia anterior a 2018.

---
Categorías: **A** original tal como lo entregó la entidad · **B** original de captura o compilación · **D** conversión a parquet de un original pesado (ver nota en el registro). La procedencia de todos los archivos está **por confirmar**. Detalle completo en el registro de la raíz y reglas en `00_Documentacion/`.
