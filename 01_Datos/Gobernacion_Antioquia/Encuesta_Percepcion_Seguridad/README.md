# Encuesta de percepción de seguridad

**2 archivos versionados**, más el archivo de microdatos con identificadores, que está en esta carpeta pero no se versiona.

| Archivo | Cat. | Contenido |
|---|---|---|
| `Diccionario de datos 033200250000 percepcion de seguridad_2025 (1).xlsx` | A | Diccionario de variables y valores de la encuesta de percepción de seguridad 2025. |
| `encuesta_percepcion_2018-2025_anonimizada.parquet` | E | Microdatos 2018-2025 sin identificadores directos ni barrio del encuestado: 23.216 registros × 1.356 columnas. |

`Data anonimizada encuesta percepcion 2018-2025.xlsx` (100 MiB, 23.216 registros × 1.363 columnas) se queda en esta carpeta, listado en `.gitignore`: no sale del computador de trabajo. Su MD5 está en el registro.

## Anonimización

Es el único archivo del repositorio con una intervención más profunda que un cambio de formato, y por eso se documenta aquí completa.

**Qué se suprimió:**

| Columna | Qué era | Registros con dato |
|---|---|---|
| `PD_NOMBREAUTORIZA` | Nombre del adulto que autoriza la entrevista | 726 |
| `PD_FIRMAAUTORIZA` | Identificador de la firma | 726 |
| `DIRECCION_1` | Dirección de la vivienda | 2.924 |
| `DIRECCION_1_1` | La misma dirección, geocodificada | 2.336 |
| `BARRIOENC` | Barrio o vereda declarado por el encuestado, en texto libre | 23.216 |
| `TELEFONO` | Teléfono | 0 (columna vacía) |
| `EMAIL` | Correo | 0 (columna vacía) |

`BARRIOENC` se suprimió porque estaba en todos los registros con 7.599 valores distintos: 6.291 combinaciones de municipio y barrio aparecían una sola vez, y el 43 % de los registros quedaba en un barrio con menos de cinco encuestas.

Además se buscaron correos, teléfonos y números de documento dentro de las respuestas abiertas, para enmascararlos. No se encontró ninguno (0 celdas enmascaradas).

**Qué se conserva, por decisión del equipo:** `BARRIO` y `COMUNA_LOCALIDAD` del marco muestral (4.588 y 4.059 registros), código de manzana (7.569 registros), zona de muestreo, ruta, código de entrevistador, municipio, estrato, sexo, edad exacta, fecha y hora de la entrevista y las 102 columnas de respuesta abierta.

**Riesgo residual.** Quitar el nombre, la dirección y el barrio declarado reduce el riesgo, no lo elimina. En los 7.569 registros con código de manzana, la manzana ubica la vivienda con más precisión que el barrio; y en los municipios pequeños, estrato, sexo y edad exacta siguen señalando a pocas personas. Las respuestas abiertas pueden mencionar lugares o situaciones reconocibles. Quien use este archivo no debe publicar resultados desagregados a un nivel que permita reconocer a un encuestado. Queda como pendiente **P-18** medir ese riesgo y decidir si el archivo se generaliza más.

**Verificación hecha:** ninguna de las columnas suprimidas sobrevive en el parquet, y ninguna respuesta abierta contiene correos ni teléfonos. El parquet conserva, en sus metadatos, el MD5 del archivo de origen, las columnas suprimidas y el alcance de la anonimización; cada columna guarda además el texto de su pregunta.

## Código que produjo el archivo

Es el código que se ejecutó, no una reconstrucción posterior.

```python
"""Anonimiza la encuesta de percepcion: retira identificadores directos y guarda parquet."""
import os, re, sys, json, hashlib, time
import python_calamine as pcm
import pyarrow as pa, pyarrow.parquet as pq

R = sys.argv[1]; os.chdir(R)
CARPETA = '01_Datos/Gobernacion_Antioquia/Encuesta_Percepcion_Seguridad/'
ORIGEN = CARPETA + 'Data anonimizada encuesta percepcion 2018-2025.xlsx'
DESTINO = CARPETA + 'encuesta_percepcion_2018-2025_anonimizada.parquet'
HOY = '2026-09-17'

# Columnas que identifican directamente a una persona o ubican su vivienda.
SUPRIMIR = ['PD_NOMBREAUTORIZA', 'PD_FIRMAAUTORIZA', 'TELEFONO', 'EMAIL', 'DIRECCION_1', 'DIRECCION_1_1', 'BARRIOENC']
# Patrones de identificador directo que pueden aparecer dentro de una respuesta abierta.
PATRONES = [
    (re.compile(r'[\w.+-]+@[\w-]+\.[\w.]+'), '[CORREO SUPRIMIDO]'),
    (re.compile(r'(?<!\d)(?:3\d{9}|\d{7})(?!\d)'), '[TELEFONO SUPRIMIDO]'),
    (re.compile(r'(?i)\b(?:c\.?c\.?|c[ée]dula)\s*:?\s*\d[\d.\s]{5,}'), '[DOCUMENTO SUPRIMIDO]'),
]

def md5(p):
    h = hashlib.md5()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 22), b''): h.update(b)
    return h.hexdigest()

t0 = time.time()
md5_origen = md5(ORIGEN)
hoja = pcm.CalamineWorkbook.from_path(ORIGEN)
d = hoja.get_sheet_by_name(hoja.sheet_names[0]).to_python()
etiquetas = [str(c).strip() for c in d[0]]
nombres = [str(c).strip() for c in d[1]]
filas = d[2:]
print('leido', len(filas), 'x', len(nombres), round(time.time() - t0), 's', flush=True)

columnas = list(zip(*[list(r) + [None] * (len(nombres) - len(r)) for r in filas]))
mascaras = 0
campos, arrays = [], []
for j, nombre in enumerate(nombres):
    if nombre in SUPRIMIR: continue
    vals = list(columnas[j])
    tipos = {type(v) for v in vals if v is not None and str(v).strip() != ''}
    if str in tipos:
        limpio = []
        for v in vals:
            if isinstance(v, str) and v.strip():
                orig = v
                for pat, rep in PATRONES: v = pat.sub(rep, v)
                if v != orig: mascaras += 1
                limpio.append(v)
            else:
                limpio.append(None if v is None or str(v).strip() == '' else str(v))
        arr = pa.array(limpio, type=pa.string())
    else:
        limpio = [None if (v is None or str(v).strip() == '') else v for v in vals]
        if tipos == {float} and all(float(v).is_integer() for v in limpio if v is not None):
            arr = pa.array([None if v is None else int(v) for v in limpio], type=pa.int64())
        else:
            arr = pa.array(limpio)
    campos.append(pa.field(nombre, arr.type, metadata={b'etiqueta': etiquetas[j].encode()}))
    arrays.append(arr)

esquema = pa.schema(campos, metadata={
    b'origen_archivo': os.path.basename(ORIGEN).encode(),
    b'origen_md5': md5_origen.encode(),
    b'origen_filas': str(len(filas)).encode(),
    b'origen_columnas': str(len(nombres)).encode(),
    b'anonimizacion_fecha': HOY.encode(),
    b'anonimizacion_columnas_suprimidas': ', '.join(SUPRIMIR).encode(),
    b'anonimizacion_enmascarado': 'correos, telefonos y documentos dentro de respuestas abiertas'.encode(),
    b'anonimizacion_alcance': ('Solo identificadores directos. Se conservan barrio, manzana, comuna, zona de muestreo, '
                               'estrato, sexo, edad exacta, fechas y respuestas abiertas: el riesgo de reidentificacion '
                               'por combinacion de esas variables no esta eliminado.').encode(),
    b'herramienta': f'pyarrow {pa.__version__}'.encode()})
tabla = pa.Table.from_arrays(arrays, schema=esquema)
pq.write_table(tabla, DESTINO, compression='zstd', compression_level=9)

resumen = {'filas': tabla.num_rows, 'columnas_origen': len(nombres), 'columnas_resultado': tabla.num_columns,
           'suprimidas': SUPRIMIR, 'celdas_enmascaradas': mascaras,
           'md5_origen': md5_origen, 'md5_parquet': md5(DESTINO),
           'peso_mb': round(os.path.getsize(DESTINO) / 1048576, 2), 'segundos': round(time.time() - t0)}
json.dump(resumen, open(os.path.expanduser('~/work/resumen_anon.json'), 'w'), ensure_ascii=False, indent=1)
print(json.dumps(resumen, ensure_ascii=False, indent=1))

# Verificacion: ninguna columna suprimida sobrevive y no quedan correos ni telefonos sueltos
t = pq.read_table(DESTINO)
assert not (set(SUPRIMIR) & set(t.column_names)), 'quedo una columna suprimida'
sospechosos = 0
for c in t.column_names:
    col = t[c]
    if pa.types.is_string(col.type):
        for v in col.to_pylist():
            if v and (PATRONES[0][0].search(v) or PATRONES[1][0].search(v)): sospechosos += 1
print('columnas suprimidas presentes: 0 | textos con correo o telefono restantes:', sospechosos)
```

Equivalente en R, si el archivo se vuelve a generar con otra versión del original:

```r
library(arrow)
enc <- readxl::read_excel("Data anonimizada encuesta percepcion 2018-2025.xlsx", skip = 1)   # la fila 2 trae los nombres cortos
directos <- c("PD_NOMBREAUTORIZA", "PD_FIRMAAUTORIZA", "TELEFONO", "EMAIL",
              "DIRECCION_1", "DIRECCION_1_1", "BARRIOENC")
enc <- enc[, setdiff(names(enc), directos)]
write_parquet(enc, "encuesta_percepcion_2018-2025_anonimizada.parquet",
              compression = "zstd", compression_level = 9)
```

## Cómo usarlo

```r
library(arrow)
enc <- read_parquet("encuesta_percepcion_2018-2025_anonimizada.parquet")

# Solo unas columnas, sin cargar las 1.356
read_parquet("encuesta_percepcion_2018-2025_anonimizada.parquet",
             col_select = c(COD_MUNICIPIO, ESTRATO, PC, P1A))

# Reconstruir el CSV anonimizado
readr::write_excel_csv(enc, "encuesta_percepcion_2018-2025_anonimizada.csv")

# Etiqueta completa de una pregunta y datos de la anonimización
esquema <- open_dataset("encuesta_percepcion_2018-2025_anonimizada.parquet")$schema
esquema$GetFieldByName("P1A")$metadata     # texto de la pregunta
esquema$metadata                           # origen, MD5, columnas suprimidas, alcance
```

El CSV reconstruido es el archivo anonimizado en otro formato, no el original de la entidad.

---
Categorías: **A** original tal como lo entregó la entidad · **D** conversión a parquet de un original pesado · **E** original anonimizado (ver `00_Documentacion/`, sección 10). La procedencia de todos los archivos está **por confirmar**. Detalle completo en el registro de la raíz.
