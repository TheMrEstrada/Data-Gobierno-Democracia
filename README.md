# Data-Gobierno-Democracia

Repositorio de **datos originales** de fuentes oficiales sobre los municipios de Antioquia. Cada archivo está tal como lo entregó su fuente, identificado por su huella MD5 y descrito en un registro. Aquí no se limpian ni se calculan datos: eso ocurre en los proyectos que leen este repositorio.

## Contenido

| Elemento | Qué es |
|---|---|
| `00_Documentacion/` | Anexo metodológico: criterios de admisión, protocolos y papel de personas y agentes de IA |
| `01_Datos/` | 176 archivos versionados en carpetas por entidad fuente, más 4 archivos que quedan solo en el disco: 3 originales pesados y la encuesta anonimizada |
| `registro_fuentes_variables.xlsx` | Registro de fuentes y variables: qué es cada archivo, su procedencia, las variables que contiene, brechas y pendientes |
| `verificar_integridad.py` | Script que comprueba el manifiesto: recalcula los MD5 y avisa de cambios, pérdidas e ingresos no registrados |
| `manifiesto_integridad.csv` | Ruta, peso y MD5 de cada archivo versionado de `01_Datos/`, para verificar que están todos y que ninguno cambió |

## Cómo usarlo

1. Busca el dato en el registro (hoja *Variables* o *Fuentes*): te dice en qué archivo, hoja y columna está.
2. Abre el archivo en `01_Datos/`, sin modificarlo. Si necesitas transformarlo, hazlo en tu propio proyecto.
3. Antes de citar una cifra, revisa en el registro la fecha de corte y el nivel de procedencia del archivo.

Para comprobar que tu copia está completa e intacta, ejecuta desde la raíz:

```
python verificar_integridad.py
```

## Reglas básicas

- Solo entran originales (categorías A y B). Nada limpiado, recortado ni calculado.
- Los originales de más de 100 MB no se versionan: quedan en el disco y el repositorio guarda su conversión a parquet (categoría D, anexo sección 10).
- Un original con identificadores directos de personas tampoco se versiona: el repositorio guarda su versión anonimizada (categoría E, anexo sección 10.4).
- Los archivos no se editan, no se renombran ni se sobrescriben.
- Todo archivo nuevo o actualizado pasa por el ciclo de ingreso del anexo y queda en el registro y el manifiesto.
- Los archivos `README.md` son solo documentación: no son datos, no están en el registro ni en el manifiesto.
- Un agente de IA puede preparar y verificar; aprobar y publicar corresponde a una persona.

## Estado

Borrador inicial (septiembre de 2026). La procedencia de los archivos está en investigación, hay 15 brechas abiertas, la tabla maestra territorial está por construir (90 municipios con esquema asociativo) y de los tres originales de más de 100 MB dos ya tienen su conversión a parquet en el repositorio. El detalle está en la sección "Estado actual y limitaciones" del anexo y en las hojas Brechas y Pendientes del registro. Su gestión corresponde al equipo.
