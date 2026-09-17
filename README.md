# Data-Gobierno-Democracia

Repositorio de **datos originales** que sustentaron el diagnóstico de los Planes Estratégicos Provinciales de Antioquia (Proyecto Provincias). Cada archivo está tal como lo entregó su fuente, identificado por su huella MD5 y descrito en un registro. Aquí no se limpian ni se calculan datos: eso ocurre en los proyectos que leen este repositorio.

## Contenido

| Elemento | Qué es |
|---|---|
| `00_Documentacion/` | Anexo metodológico: criterios de admisión, protocolos y papel de personas y agentes de IA |
| `01_Datos/` | 172 archivos originales en carpetas por entidad fuente |
| `Sistematización fuentes originales - Proyecto Provincias - v4.xlsx` | Registro de fuentes y variables: qué es cada archivo, su procedencia, las variables que contiene, brechas y pendientes |
| `manifiesto_integridad.csv` | Ruta, peso y MD5 de cada archivo de `01_Datos/`, para verificar que están todos y que ninguno cambió |

## Cómo usarlo

1. Busca el dato en el registro (hoja *Variables* o *Fuentes*): te dice en qué archivo, hoja y columna está.
2. Abre el archivo en `01_Datos/`, sin modificarlo. Si necesitas transformarlo, hazlo en tu propio proyecto.
3. Antes de citar una cifra, revisa en el registro la fecha de corte y el nivel de procedencia del archivo.

## Reglas básicas

- Solo entran originales (categorías A y B). Nada limpiado, recortado ni calculado.
- Los archivos no se editan, no se renombran ni se sobrescriben.
- Todo archivo nuevo o actualizado pasa por el ciclo de ingreso del anexo y queda en el registro y el manifiesto.
- Los archivos `README.md` son solo documentación: no son datos, no están en el registro ni en el manifiesto.
- Un agente de IA puede preparar y verificar; aprobar y publicar corresponde a una persona.

## Estado

Borrador inicial (septiembre de 2026). La procedencia de los archivos está en investigación, hay 15 brechas abiertas, la tabla maestra territorial está por construir y tres originales de más de 100 MB esperan decisión sobre su almacenamiento. El detalle está en la sección "Estado actual y limitaciones" del anexo.
