# Anexo metodológico — Repositorio de datos originales Data-Gobierno-Democracia

**Versión:** borrador 0.10 · **Fecha:** 2026-09-17 · **Estado:** en revisión

---

## 1. Propósito y alcance

Este repositorio reúne, en un solo lugar y con registro verificable, **datos originales** de fuentes oficiales sobre los municipios de Antioquia. Cada archivo está como lo entregó su fuente, identificado por su huella digital y documentado con su origen.

El documento está escrito para tres lectores:

- quien necesita **encontrar y usar** un dato;
- quien va a **agregar o actualizar** datos;
- quien tiene que **auditar** el repositorio sin conocer su historia.

**Dentro del alcance:** archivos originales, sus metadatos, la tabla maestra territorial y las reglas para mantener todo eso.

**Fuera del alcance:** limpieza, homogeneización, cálculo de indicadores, reglas de agregación, tablas, figuras y documentos de diagnóstico. Todo eso ocurre en proyectos que **leen** este repositorio y nunca escriben en él.

## 2. Principios

1. **Solo originales.** Ningún archivo limpiado, recortado, calculado o combinado por el equipo entra como dato. Si existe una versión tratada, lo que se guarda es su original.
2. **Los archivos no se tocan.** Un original no se edita, no se renombra y no se sobrescribe. Toda corrección se hace fuera del repositorio.
3. **Todo archivo tiene registro.** Un archivo sin fila en el registro de fuentes no existe para el repositorio. Una fila sin archivo es un pendiente.
4. **La huella manda.** La integridad se comprueba con el MD5 del archivo, no con su nombre ni con su fecha.
5. **Lo que no se sabe se declara.** Un metadato desconocido queda como "por confirmar"; nunca se infiere sin evidencia.
6. **Las decisiones son humanas.** Un agente de IA puede preparar, verificar y proponer. Aprobar, decidir y publicar corresponde a una persona (sección 11).

## 3. Origen del repositorio

Los archivos se incorporaron el 2026-09-16 desde un archivo de trabajo previo del equipo. Cada uno se revisó por contenido (cobertura municipal detectada, hojas, columnas agregadas por el equipo y comparación entre archivos parecidos) y se clasificó con los criterios de la sección 6.

**Resultado:** entraron 172 originales (A y B). Tres originales de más de 100 MB quedaron registrados sin copiar (sección 10) y la tabla maestra territorial quedó por construir (sección 8). Los archivos tratados no se incorporaron.

El repositorio no depende de ese archivo de trabajo para operar. La procedencia de cada archivo se establece con el protocolo de la sección 13, no con la ubicación que tuvo antes.

## 4. Convenciones

- **Nombres de archivo:** se conservan exactamente como llegaron, con espacios, tildes y erratas. El nombre es parte de la identidad del original.
- **Carpetas:** una por entidad fuente, con subcarpetas cuando la entidad publica varios productos. Los nombres de carpeta no llevan espacios ni tildes.
- **Fechas:** AAAA-MM-DD en documentos y registros.
- **Llave territorial:** código DIVIPOLA del municipio (`ind_mpio`, entero de 5001 a 5895 para Antioquia). Los cruces se hacen por código, nunca por nombre.
- **Codificación:** UTF-8 para todo texto que produzca el equipo.
- **Estados:** "por confirmar" para lo que falta verificar y "decisión por tomar" para lo que requiere aprobación humana.

## 5. Organización

```
Data-Gobierno-Democracia/
├── registro_fuentes_variables.xlsx   (registro)
├── manifiesto_integridad.csv         (manifiesto)
├── verificar_integridad.py           (verificación del manifiesto)
├── 00_Documentacion/  (este anexo)
└── 01_Datos/
    ├── DANE/
    │   ├── CNPV_2018/  Cuentas_Nacionales/  Deficit_Habitacional/
    │   └── Estadisticas_Vitales/  Marco_Geoestadistico/  Proyecciones_Poblacion/
    ├── DNP/
    │   ├── Desempeno_Fiscal_IDF/  Desempeno_Municipal_MDM/
    │   └── Mapa_Inversiones/  Riesgo_Desastres_IMRC/
    ├── Gobernacion_Antioquia/
    │   ├── Catastro/  DAGRAN/  DAP_Planeacion/  Datalake/
    │   ├── Encuesta_Calidad_de_Vida/  Encuesta_Percepcion_Seguridad/
    │   ├── POTA/Tablas_municipales_octubre/GRUPO_1 ... GRUPO_8/
    │   └── SSSA_Secretaria_Seccional_Salud/  Secretaria_Turismo/
    ├── INS/
    │   └── SIVICAP_IRCA/  SIVIGILA/
    ├── ANM/  Contraloria/  Funcion_Publica_FURAG/  Global_Forest_Watch/
    ├── IDEAM/  MEN/  Migracion_Colombia_SITA/  MinTIC/  Parques_Nacionales_RUNAP/
    ├── Policia_Nacional/  Superintendencia_Subsidio_Familiar/  UARIV/
    ├── UBPD/  UNGRD/  UNODC_SIMCI/  URT/  XM/
    ├── _Compilaciones_equipo/     (compilaciones de varias fuentes, B)
    └── _Entidad_por_confirmar/    (entidad no verificada)
```

En la raíz solo están los archivos de control: el registro de fuentes y variables, el manifiesto y el script que lo verifica (sección 9). Los datos viven únicamente en `01_Datos/` y la documentación en `00_Documentacion/`.

Las carpetas que empiezan por guion bajo son transitorias. Un archivo sale de ellas cuando se confirma su entidad o se consigue el original de cada parte.

Los originales de más de 100 MB también viven en la carpeta de su entidad, pero no se versionan: están listados en `.gitignore` y lo que viaja al repositorio remoto es su conversión (sección 10).

**Contenido al inicio:**

| Entidad | Archivos | Entidad | Archivos |
|---|---|---|---|
| Gobernación de Antioquia | 120 | Migración Colombia (SITA) | 2 |
| DANE | 16 | Función Pública (FURAG) | 2 |
| INS | 7 | MEN | 2 |
| DNP | 6 | 12 entidades con 1 archivo cada una | 12 |
| UARIV | 4 | Carpetas transitorias | 2 |
| UNGRD | 3 | **Total versionado** | **176** |

De los 120 archivos de la Gobernación, 91 son las tablas municipales POTA. Los 16 del DANE incluyen las tres hojas de las proyecciones por edad simple convertidas a parquet.

Además hay **3 originales pesados** en el disco que no se versionan (sección 10).

## 6. Criterios de admisión

| Categoría | Definición | ¿Entra? |
|---|---|---|
| **A. Original** | Archivo tal como lo entregó o publicó la entidad. | Sí |
| **B. Original de captura o compilación** | No es la descarga directa, pero no transforma valores. Incluye: copia manual de tablas web, reconstrucción desde una captura de navegador, compilación de cuadros de varias fuentes o columnas añadidas por el equipo sin cambiar los datos. | Sí, con nota que explique qué lo hace B |
| **C. Tratado** | Tiene limpieza, filtro, recorte, cálculo, cruce, agregación o formato hechos por el equipo; o es un extracto o duplicado de un original que ya está. | No |
| **D. Conversión de formato** | Excepción única para un original de más de 100 MB, que no cabe en el repositorio remoto: el mismo contenido en parquet, sin cambiar valores, con el MD5 del original y la referencia de la conversión. | Sí, bajo el protocolo de la sección 10 |
| **E. Original anonimizado** | Excepción para un original que contiene identificadores directos de personas: el mismo archivo sin esos campos. Solo se admite cuando el original no puede circular tal como está. | Sí, bajo el protocolo de la sección 10.5 |

**Reglas que no admiten excepción:**

- No entran recortes hechos por el equipo a un subconjunto de municipios: se guarda el producto completo de la entidad.
- Si existen a la vez un extracto y su original completo, entra solo el original.
- Un archivo C solo reemplaza a un original ausente como excepción aprobada por una persona, y queda registrado como brecha abierta.
- Los archivos B se revisan periódicamente para sustituirlos por la descarga directa cuando esté disponible.
- La categoría D solo se usa por peso. Si un original cabe en el repositorio, entra tal cual: no se convierte "para que pese menos".
- La categoría E solo se usa por protección de datos, y cada uso lo aprueba una persona. El original con identificadores nunca se versiona ni se publica.

**Casos B al inicio (22):**

- copia manual del indicador Ley 617 (Contraloría);
- consulta IDF con hojas de trabajo;
- sujetos de reparación colectiva, reconstruidos desde una captura `.har`, y las cuatro capturas `.har`;
- compilaciones de salud, de seguridad y DDHH, del RUV, de la UBPD y de turismo;
- títulos mineros y plantas de energía con limpieza inicial;
- el cruce espacial de áreas protegidas;
- el área municipal sin fuente documentada;
- la base de extranjeros con una hoja agregada;
- proyecciones de población con hojas de rangos;
- tres documentos de observaciones POTA.

## 7. Registro de fuentes y variables

El registro es el archivo `registro_fuentes_variables.xlsx`, en la raíz. Sus hojas cumplen las funciones que se describen abajo.

**Fuentes.** Una fila por archivo del repositorio, más los originales registrados que no están copiados y la tabla maestra por construir. Campos mínimos obligatorios:

| Campo | Contenido |
|---|---|
| Archivo, ruta y estado en el repositorio | Identificación exacta en el repositorio |
| Categoría y nota | A o B; en B, qué lo hace B |
| Entidad fuente | Quién produce el dato |
| Acceso | URL con fecha de consulta, solicitud oficial o forma de obtención |
| Fecha de corte y de consulta | Cuándo mide el dato y cuándo se obtuvo |
| Cobertura | Territorial (nacional, Antioquia, parcial con número de municipios) y temporal |
| Versión | Vigente, no vigente o por confirmar, cuando hay varias del mismo producto |
| Formato, peso, MD5 | Para verificar integridad |
| Procedencia | Nivel (verificada, documentada, por confirmar, desconocida), evidencia y condiciones de uso (sección 13) |
| Registros individuales | Sí/No: personas, casos, titulares o predios |
| Responsable | Persona que responde por el archivo |

**Variables.** Una fila por variable de nivel municipal, con: identificador, definición, tipo y unidad de medida, disponibilidad temporal, archivo original y su ruta, **hoja y campo dentro del original**, y estado de anclaje. Los agregados por esquema asociativo, subregión o departamento no se registran: se calculan en los proyectos que leen el repositorio. Los estados de anclaje son:

- **Archivo y campo identificados.**
- **Archivo identificado: campo por confirmar.**
- **Brecha parcial:** el original disponible no cubre toda la variable.
- **Brecha:** no hay original.
- **Sin archivo:** la variable no tiene fuente asignada.

**Brechas y Pendientes.** Lo que falta resolver, con prioridad y acción requerida.

**Leyenda.** Significado de cada columna y de sus valores.

**Control (bitácora).** Un registro por cambio: fecha, qué cambió, motivo, evidencia y quién aprobó.

## 8. Tabla maestra territorial

Es la única base que el repositorio construye, y se trata como un original porque ninguna fuente disponible la ofrece completa.

**Contenido:** una fila por cada uno de los 125 municipios de Antioquia, con estas columnas:

- código DIVIPOLA;
- nombre normalizado (mayúsculas, sin tildes, para cruces);
- nombre de presentación;
- subregión DANE;
- esquema asociativo (vacío si el municipio no pertenece a uno);
- identificador del esquema asociativo.

**Conformación definida:** 90 de los 125 municipios pertenecen a un esquema asociativo. La conformación incluye Amalfi en Minero Agroecológica y Santa Fe de Antioquia en Turística y Agroecológica; los listados que asignaban 88 municipios no se usan.

**Estado: por construir.** Falta citar el acto o la fuente oficial de cada esquema asociativo.

El nombre del esquema 5 aparece en varias fuentes como «POVINCIA DEL AGUA, BOSQUES Y TURISMO», con la errata. La tabla maestra usa la forma correcta y deja registrada la variante.

**Reglas:**

- Solo una persona puede aprobar un cambio en la conformación de los esquemas asociativos.
- Cada cambio queda en la bitácora con su acto o fuente oficial.

## 9. Integridad y trazabilidad

- **Manifiesto** (`manifiesto_integridad.csv`, en la raíz): una fila por cada archivo versionado de `01_Datos/` (los originales pesados no versionados quedan fuera, con su MD5 en el registro), con ruta, nombre, categoría, peso en bytes, MD5 y fecha de ingreso. Solo describe el contenido de este repositorio y se genera recorriendo `01_Datos/`. El registro dice qué es cada archivo; el manifiesto permite comprobar con un script que están todos y que no cambiaron.
- **Verificación:** se ejecuta `python verificar_integridad.py` desde la raíz del repositorio, antes de cada publicación y después de cualquier movimiento de carpetas. El script recalcula el MD5 de cada archivo, lo compara con el manifiesto y termina con código 1 si algo no cuadra. Hay tres resultados posibles:
  - un archivo que no coincide es un cambio no registrado;
  - un archivo sin fila es un ingreso no registrado;
  - una fila sin archivo es una pérdida.
- **Procedencia:** se documenta en el registro con el protocolo de la sección 13.
- **Historial:** el control de versiones registra el cuándo; la bitácora registra el porqué y quién lo aprobó.

## 10. Archivos pesados, registros individuales y acceso

### 10.1 Regla

El repositorio remoto no admite archivos de más de 100 MB. Para ellos rige esta excepción:

- el **original se queda en la carpeta de su entidad**, en el disco, y se lista en `.gitignore`: nunca se sube ni se borra;
- el repositorio versiona su **conversión a parquet**, registrada como categoría D;
- el registro conserva las dos filas: la del original (con su MD5, su peso y la marca de no versionado) y la del parquet;
- el **manifiesto solo cubre los archivos versionados**, porque sirve para comprobar que un clon está completo. La integridad del original se comprueba con el MD5 que guarda el registro;
- el equipo mantiene además una **copia de respaldo del original** fuera del computador de trabajo.

**Lo que la conversión no es.** Un parquet no reproduce el archivo original byte a byte: al convertir se decide dónde empieza el encabezado, cómo se nombran las columnas y qué tipo tiene cada una. Revertirlo devuelve una tabla equivalente, no el archivo de la entidad. Por eso el original nunca se borra y el MD5 que vale como huella del dato original es el suyo.

**Qué se documenta en cada conversión:** archivo de origen y su MD5, hoja convertida, filas y columnas resultantes, qué se omitió (portadas, filas vacías), herramienta y fecha. Los parquet de este repositorio llevan esos datos dentro del propio archivo, en sus metadatos.

**Verificación antes de aceptar una conversión:** mismo número de filas útiles y de columnas, y coincidencia de una suma de control (por ejemplo, el total de una columna numérica) entre el original y el parquet.

### 10.2 Cómo convertir y revertir en R

```r
# install.packages(c("arrow", "readr", "readxl", "writexl", "dplyr"))
library(arrow)

# --- CSV grande a parquet -------------------------------------------------
datos <- readr::read_delim("EMPAQUETAMIENTO_FIJO_3.csv", delim = ";",
                           locale = readr::locale(encoding = "UTF-8"))
write_parquet(datos, "EMPAQUETAMIENTO_FIJO_3.parquet",
              compression = "zstd", compression_level = 9)

# --- Hoja de Excel a parquet (skip salta la portada del cuadro) -----------
hoja <- readxl::read_excel("PPED-AreaSexoEdadMun-2018-2042_VP.xlsx",
                           sheet = "PobMunicipalxÁreaSexoEdad", skip = 6)
write_parquet(hoja, "PPED-AreaSexoEdadMun-2018-2042_VP__PobMunicipalxAreaSexoEdad.parquet",
              compression = "zstd", compression_level = 9)

# --- Leer -----------------------------------------------------------------
datos <- read_parquet("EMPAQUETAMIENTO_FIJO_3.parquet")            # todo a memoria
read_parquet("EMPAQUETAMIENTO_FIJO_3.parquet",                     # solo unas columnas
             col_select = c(ANNO, MUNICIPIO, CANTIDAD_LINEAS_ACCESOS))

open_dataset("EMPAQUETAMIENTO_FIJO_3.parquet") |>                  # filtrar sin cargarlo entero
  dplyr::filter(ID_DEPARTAMENTO == 5) |>
  dplyr::collect()

# --- Volver al formato de origen ------------------------------------------
readr::write_delim(datos, "EMPAQUETAMIENTO_FIJO_3.csv", delim = ";", na = "")
writexl::write_xlsx(hoja, "PPED-AreaSexoEdadMun-2018-2042_VP.xlsx")

# --- Ver de qué original salió un parquet ---------------------------------
open_dataset("EMPAQUETAMIENTO_FIJO_3.parquet")$schema$metadata
```

**Dos advertencias sobre este código:**

- `skip = 6` deja solo el segundo nivel del encabezado. El parquet que está en el repositorio combinó los dos niveles como `"GRUPO - subcolumna"`, así que sus nombres de columna no son los que devuelve esa línea.
- `write_delim` y `write_xlsx` escriben un archivo nuevo: no sobrescriba con ellos el original. Compruebe siempre contra el MD5 del registro.

### 10.3 Estado actual

| Original | Peso | Qué se versiona |
|---|---|---|
| `EMPAQUETAMIENTO_FIJO_3.csv` (MinTIC) | 718 MiB | 1 parquet, 39,7 MiB (3.572.367 filas × 22 columnas) |
| `PPED-AreaSexoEdadMun-2018-2042_VP.xlsx` (DANE) | 126 MiB | 3 parquet, 30,1 MiB (hoja de datos: 84.229 filas × 312 columnas; portada y notas) |
| `Data anonimizada encuesta percepcion 2018-2025.xlsx` (Gobernación) | 100 MiB | 1 parquet anonimizado, 5,59 MiB (23.216 filas × 1.356 columnas), categoría E. **Fuera del repositorio desde el 2026-09-17** mientras se decide P-18. |

### 10.4 Anonimización (categoría E)

Cuando un original trae identificadores directos de personas, el repositorio versiona una versión anonimizada y el original se queda en el disco, listado en `.gitignore`.

**Reglas:**

- se suprimen los **identificadores directos**: nombre, firma, documento, teléfono, correo y dirección, tanto en columnas propias como dentro de respuestas abiertas;
- se suprime también la **geografía que ubica la vivienda** cuando es tan fina que señala a pocas personas, como el barrio o la vereda escritos en texto libre;
- el alcance de la anonimización lo decide una persona y queda escrito: qué se suprimió, qué se conservó y por qué;
- el **código que produjo el archivo** se publica completo en el README de la carpeta, tal como se ejecutó;
- el parquet guarda en sus metadatos el archivo de origen, su MD5, las columnas suprimidas y el alcance;
- se verifica que ninguna columna suprimida sobreviva y que no queden correos, teléfonos ni documentos en el texto libre;
- **anonimizar no es garantizar el anonimato.** Si se conservan geografía fina, edad exacta u otras variables que combinadas identifican a alguien, el riesgo residual se declara en el README y queda como pendiente con responsable.

Hoy la categoría E se usa en un solo archivo: la encuesta de percepción de seguridad 2018-2025 (ver el README de su carpeta).

### 10.5 Registros individuales

Algunos archivos contienen un registro por persona, caso, titular o predio:

- encuesta de percepción;
- casos SIVIGILA de intento de suicidio;
- títulos mineros, que traen el nombre del titular;
- tablas POTA por predio.

Por decisión institucional todo el repositorio es accesible al equipo. La marca en el registro existe para que quien use esos archivos no publique resultados que permitan identificar a alguien, y para revisar esa decisión si el acceso se amplía.

**Caso resuelto a medias (pendiente P-18).** El archivo de la encuesta de percepción se llamaba "anonimizada", pero conservaba 726 nombres de persona, 5.260 direcciones y el barrio del encuestado en los 23.216 registros. El repositorio versiona ahora una versión sin esos campos (categoría E) y el original se queda en el disco. Sigue abierto evaluar el riesgo residual: el código de manzana del marco muestral, el estrato, el sexo y la edad exacta se conservaron por decisión del equipo.

## 11. Personas y agentes de IA

Un agente de IA puede hacer buena parte del trabajo operativo con rapidez y sin errores de transcripción, pero no tiene autoridad ni responsabilidad institucional. La regla es simple: **el agente prepara y verifica; la persona decide y responde.**

| El agente de IA puede | Solo una persona puede |
|---|---|
| Inventariar archivos y calcular pesos y MD5 | Aprobar la categoría de cualquier archivo B y de los casos dudosos |
| Leer hojas y encabezados; detectar cobertura, recortes y duplicados | Decidir exclusiones y excepciones a los criterios de admisión |
| Proponer la categoría con su evidencia | Obtener originales: solicitudes a entidades, descargas con credenciales, acuerdos de uso |
| Redactar descripciones y completar el registro con metadatos que estén en el archivo | Confirmar entidad, URL y fecha de corte cuando no constan en el archivo |
| Investigar la procedencia: buscar la publicación oficial y contrastarla con el archivo | Aportar el conocimiento del equipo y asignar el nivel de procedencia |
| Anclar variables a hoja y campo, citando la evidencia | Declarar qué versión es la vigente |
| Generar y verificar el manifiesto; detectar inconsistencias | Aprobar cambios en la tabla maestra territorial |
| Preparar la propuesta de cambio y la entrada de bitácora | Decidir sobre archivos pesados y registros individuales |
| Redactar borradores de documentación | Aprobar el ingreso y publicarlo en el repositorio compartido |
| | Cerrar pendientes y brechas |

**Límites para cualquier agente:**

- No modifica, renombra ni borra originales.
- No publica en el repositorio compartido sin aprobación.
- No completa metadatos por inferencia.
- Toda salida del agente llega como propuesta revisable, con la evidencia que la sustenta.

## 12. Ciclo común de ingreso

Agregar un dato nuevo, actualizar uno existente, establecer la procedencia de un archivo y cerrar un pendiente siguen el mismo ciclo. Las secciones 13 a 16 describen solo lo que cambia en cada caso.

| Paso | Qué se hace | Quién |
|---|---|---|
| 1. Obtención | Conseguir el archivo de la entidad y anotar acceso y fecha de descarga | Persona (descargas públicas: agente, con aprobación) |
| 2. Revisión | Leer contenido: hojas, cobertura, columnas agregadas, relación con archivos existentes | Agente o persona |
| 3. Clasificación | Proponer A, B o C con evidencia | Agente o persona |
| 4. Aprobación | Aceptar la clasificación; en B, validar la nota | Persona |
| 5. Ubicación | Carpeta de la entidad, sin renombrar el archivo | Agente o persona |
| 6. Registro | Fila en Fuentes con su nivel de procedencia, variables afectadas, fila en el manifiesto | Agente o persona |
| 7. Verificación | Recalcular MD5 y comprobar que el registro y el repositorio coinciden | Agente o persona |
| 8. Bitácora y publicación | Entrada con motivo y aprobador; publicación del cambio | Persona aprueba y publica |

Un ingreso no está terminado hasta que pasa la verificación del paso 7.

## 13. Protocolo de investigación de procedencia

Saber de dónde viene cada archivo es el requisito más importante del repositorio: sin procedencia, un dato no se puede citar, actualizar ni defender. La procedencia no se hereda de la ubicación que tuvo un archivo en otro proyecto; se **investiga y documenta** en el registro. Es un trabajo conjunto: el agente de IA rastrea y contrasta, y la persona aporta lo que solo sabe el equipo y aprueba el resultado.

**Qué se documenta por archivo:** entidad y producto (nombre oficial de la publicación o sistema), acceso (URL exacta con fecha de consulta, o solicitud oficial con su radicado), fecha de corte y fecha de obtención, cobertura, condiciones de uso y la evidencia que sustenta cada dato.

**Niveles de procedencia:**

| Nivel | Significa | Quién lo asigna |
|---|---|---|
| **Verificada** | La publicación oficial se localizó y se contrastó con el archivo: coinciden la estructura, el periodo y una muestra de valores, o la huella de la descarga es idéntica | Persona, con el contraste documentado |
| **Documentada** | La fuente está identificada con evidencia (enlace oficial, radicado, correo de entrega), pero no se contrastaron los valores | Persona |
| **Por confirmar** | Hay una hipótesis de fuente sin evidencia suficiente | Agente o persona |
| **Desconocida** | Se investigó y no fue posible establecerla | Persona |

**Pasos:**

| Paso | Qué se hace | Quién |
|---|---|---|
| 1. Pistas internas | Leer lo que el propio archivo dice: hojas de índice o notas de "Fuente", encabezados institucionales, propiedades del documento, fechas y nombres de productos | Agente |
| 2. Búsqueda | Localizar la publicación oficial candidata: portal, nombre del producto, URL, versión y fecha de publicación | Agente |
| 3. Contraste | Si hay descarga pública, obtenerla fuera del repositorio y compararla con el archivo: estructura, periodo, muestra de valores, huella | Agente |
| 4. Conocimiento del equipo | Aportar lo que no está en internet: quién consiguió el archivo, por qué canal, solicitudes, correos, acuerdos de uso | Persona |
| 5. Decisión | Confirmar o descartar la hipótesis y asignar el nivel | Persona |
| 6. Registro | Completar los campos de procedencia y la bitácora con la evidencia | Agente o persona |

**Reglas:**

- El agente no asigna el nivel "verificada" ni "documentada": los propone con su evidencia.
- No se registra una URL que no se haya consultado; toda URL lleva su fecha de consulta.
- Si la descarga oficial actual difiere del archivo del repositorio, **no lo reemplaza**: se registra como otra versión y se sigue el protocolo de actualización (sección 16).
- Las fuentes que exigen credenciales, solicitudes formales o contacto con la entidad las gestiona una persona.
- Un archivo con procedencia desconocida se conserva, con esa marca visible, hasta que se decida si se reemplaza, se mantiene como B o se retira.

**Orden de trabajo:** primero los archivos que sostienen variables, luego los de carpetas transitorias y los de categoría B, y al final el resto.

## 14. Protocolo de pendientes y brechas

Un **pendiente** es una decisión o dato faltante sobre algo que ya está en el repositorio. Una **brecha** es un original que no está.

**Priorización:**

- **Alta:** afecta variables publicadas o la tabla maestra.
- **Media:** afecta metadatos o la calidad del registro.
- **Baja:** informativo.

**Salidas posibles para una brecha:**

1. **Recuperar el original.** Se obtiene de la entidad o del equipo, pasa el ciclo de ingreso y la brecha se cierra. Si el corte no coincide con el que se usó antes, se declara en la nota de versión.
2. **Aceptar un B.** Si solo existe una captura o compilación, entra como B con su nota. La brecha queda como parcial.
3. **Descartar.** La variable deja de sostenerse con datos del repositorio. Se registra el motivo y las variables quedan marcadas como no disponibles.

**Cierre:** exige evidencia (archivo ingresado, MD5 y entrada de bitácora) y la aprobación de una persona. Un agente puede proponer el cierre, pero no ejecutarlo.

Un pendiente cerrado **se elimina de la hoja Pendientes**, para que la hoja muestre solo lo que falta. Su rastro no se pierde: el cierre queda en la bitácora (hoja Control) con la fecha y la evidencia, y el resultado queda en la columna que se completó. Las brechas cerradas siguen la misma regla.

**Brechas abiertas al inicio:**

| Id | Tema | Prioridad |
|---|---|---|
| B-01 | Inventario pecuario municipal | Alta |
| B-02 | Evaluaciones agropecuarias (cultivos) | Alta |
| B-03 | Explotación de oro de aluvión (EVOA) | Alta |
| B-04 | Índice de Ciudades Modernas (ICM) | Alta |
| B-08 | Red vial primaria, secundaria y terciaria (shapefiles) | Alta |
| B-10 | Indicadores de seguridad, salud y vivienda: fuente de cada uno de los 33 | Alta |
| B-13 | Tabla maestra territorial (sección 8) | Alta |
| B-05 | Hechos victimizantes (RUV) | Media |
| B-06 | Índice de Desempeño Fiscal | Media |
| B-07 | Estado de actualización catastral | Media |
| B-09 | Presupuesto de inversión (API Mapa de Inversiones, sin archivo) | Media |
| B-12 | Índice de Competitividad IMCA 2022 | Media |
| B-11 | Suicidio e intento 2021 | Baja |
| B-14 | Capa RUNAP de áreas protegidas | Baja |
| B-15 | Marco Geoestadístico nacional | Baja |

## 15. Protocolo para agregar datos nuevos

Además del ciclo común:

1. **Antes de obtener el archivo,** comprobar en el registro que no exista ya el mismo producto. Si existe, es una actualización (sección 16), no un ingreso nuevo.
2. **Preferir la fuente primaria.** Si hay descarga oficial, no se acepta una compilación.
3. **Pedir el producto completo** que publica la entidad, no un filtro a Antioquia ni a un grupo de municipios. Si la entidad solo entrega el filtro, se registra como cobertura parcial.
4. **Documentar las variables** que motivaron el ingreso, con hoja y campo en el original.
5. **Entidad nueva:** se crea su carpeta. Si la entidad no está verificada, el archivo va a `_Entidad_por_confirmar/` y se abre un pendiente.

## 16. Protocolo para actualizar datos existentes

Una actualización es un nuevo corte o una revisión de un producto que ya está en el repositorio.

**Pasos, además del ciclo común:**

1. Confirmar que es el mismo producto: misma entidad, misma estructura o equivalente, periodo nuevo o datos revisados.
2. Comparar con la versión anterior y registrar qué cambió: periodos agregados, cambios de estructura, valores revisados.
3. Declarar la versión vigente en el registro.
4. Revisar las variables ancladas al archivo anterior y actualizar su hoja y campo si la estructura cambió.
5. Anotar en la bitácora que el corte cambió. **Actualizar es cambiar de corte**, y los usuarios de las cifras deben poder saberlo.

**Política de conservación: decisión por tomar.**

- **Conservar** el archivo anterior, marcado como no vigente: el corte que sustentó cifras ya publicadas sigue disponible y verificable, pero el repositorio crece.
- **Reemplazar** el archivo y dejar el historial en el control de versiones: el repositorio queda más limpio, pero los archivos binarios y pesados se recuperan con dificultad.

Mientras no se decida, **no se borra ni se sobrescribe ningún archivo**: el nuevo corte entra junto al anterior. Cuando conviven varias versiones, la columna `version` del registro dice cuál es la vigente y la nota explica por qué. Casos ya resueltos: IRCA, mortalidad infantil y población. Otros casos de convivencia:

- eventos de salud pública;
- valor agregado municipal;

## 17. Estado actual y limitaciones

- **Tres originales pesados** están en el disco pero no se versionan. Dos ya tienen su conversión a parquet en el repositorio; el de la encuesta de percepción no se convirtió (sección 10).
- **La encuesta de percepción** está fuera del repositorio, incluso en su versión anonimizada: la medición de riesgo (sección 10.4) mostró que casi la mitad de los registros son únicos. Vuelve a entrar cuando se decida P-18.
- **La tabla maestra territorial está por construir**, con la conformación ya definida (sección 8).
- **Hay 15 brechas abiertas**, siete de prioridad alta (sección 14).
- **Registro de variables (320, nivel municipal):**
  - en 24 están identificados la hoja y el campo en el original;
  - en 219 el campo está por confirmar;
  - 75 dependen de brechas: 45 sin original y 30 con un original parcial;
  - 2 no tienen fuente;
  - 4 filas no tienen identificador.
- **Procedencia sin investigar:** los 172 archivos están en nivel "por confirmar". Su entidad se asignó por nombre y contenido al incorporarlos, sin contraste con las publicaciones oficiales.
- **Metadatos incompletos:**
  - la URL y la fecha de corte no están registradas;
  - 5 entidades están por confirmar;
  - 163 filas no tienen responsable.
- **Versiones declaradas el 2026-09-17:** IRCA (vigente el histórico nacional), mortalidad infantil (vigente la edición 2005-2025) y población (vigente PPED 2018-2042, con lo que el repositorio queda sin serie de referencia para 1985-2017).
- **Un original no se puede leer:** defunciones no fetales 2022 está protegido con contraseña.
- **Vocabulario sin unificar:**
  - unidades con criterios distintos: porcentaje, fracción 0-1 y escala 0-100;
  - tipos de medida que se solapan: total, cantidad, conteo, numérico.
- **Validación externa:** los originales se verificaron por integridad y contenido, no contra las entidades.

La gestión de estos pendientes corresponde al equipo; el detalle está en las hojas Brechas y Pendientes del registro.

## 18. Control del documento

| Versión | Fecha | Cambio | Aprobó |
|---|---|---|---|
| 0.1 | 2026-09-16 | Borrador inicial | Pendiente |
| 0.2 | 2026-09-17 | Estructura 00_Documentacion/01_Datos; manifiesto de integridad propio del repositorio; protocolo de investigación de procedencia | Pendiente |
| 0.3 | 2026-09-17 | Desvinculación del archivo de trabajo de origen; registro renombrado a `registro_fuentes_variables.xlsx`; tabla maestra con conformación definida (90 municipios con esquema asociativo); variables restringidas al nivel municipal | Pendiente |
| 0.4 | 2026-09-17 | Categoría D y protocolo de archivos pesados (conversión a parquet, con código en R); hallazgo de identificadores en la encuesta de percepción | Pendiente |
| 0.5 | 2026-09-17 | Categoría E y protocolo de anonimización; encuesta de percepción anonimizada y versionada en parquet | Pendiente |
| 0.6 | 2026-09-17 | La anonimización suprime también la geografía fina en texto libre: se retiró `BARRIOENC` de la encuesta de percepción | Pendiente |
| 0.7 | 2026-09-17 | Script `verificar_integridad.py` para comprobar el manifiesto; el `.docx` y su procedimiento de generación quedan descritos en `00_Documentacion/README.md` | Pendiente |
| 0.8 | 2026-09-17 | La encuesta anonimizada sale del repositorio mientras se decide P-18; se documenta que la versión ya publicada permanece en el historial de git | Pendiente |
| 0.9 | 2026-09-17 | Versiones vigentes declaradas para IRCA, mortalidad infantil y población (P-08 y P-09 cerrados) | Pendiente |
| 0.10 | 2026-09-17 | Los pendientes y brechas resueltos se eliminan de sus hojas; su cierre queda en la bitácora | Pendiente |

Este anexo se actualiza en tres casos:

- cuando cambia una regla;
- cuando se cierra una brecha de prioridad alta o cambia el nivel de procedencia de un grupo de archivos;
- cuando se toma una de las decisiones marcadas como "decisión por tomar".

Las cifras de las secciones 3, 5, 14 y 17 deben coincidir con el registro de fuentes y variables. Si no coinciden, manda el registro.
