# Anexo metodológico — Repositorio de datos originales Data-Gobierno-Democracia

**Versión:** borrador 0.1 · **Fecha:** 2026-09-16 · **Estado:** en revisión

---

## 1. Propósito y alcance

Este repositorio reúne, en un solo lugar y con registro verificable, **los datos originales** que sustentaron el diagnóstico del Proyecto Provincias (Planes Estratégicos Provinciales de Antioquia). Cada archivo está como lo entregó su fuente, identificado por su huella digital y documentado con su origen.

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

El repositorio nació el 2026-09-16 de una migración desde la carpeta local `Proyecto-Provincias v2`, que era la versión más completa del proyecto. La carpeta de origen no se modificó.

**Qué se hizo:** se inventariaron los 249 archivos de datos de `01_Data` (sin contar los README). Cada uno se revisó por contenido:

- cobertura municipal detectada;
- hojas;
- columnas agregadas por el equipo;
- comparación celda a celda entre archivos parecidos.

Con esa revisión cada archivo quedó en una de tres categorías (sección 6).

**Resultado:**

| Concepto | Archivos |
|---|---|
| Revisados | 249 |
| Originales que migran (A: 153 · B: 22) | 175 |
| Copiados, con MD5 verificado | 172 |
| Pendientes por peso (más de 100 MB) | 3 |
| Excluidos por ser tratados (C) | 74 |
| Base nueva por construir: tabla maestra territorial | 1 |

**Por qué se excluyó cada grupo:**

| Tipo de archivo excluido | Archivos | Qué los reemplaza |
|---|---|---|
| Recortes con "PROVINCIAS" en el nombre | 16 | Su original, cuando existe; si no, una brecha |
| Derivados del procesamiento (Parquet) | 23 | Los originales que leía cada script |
| Tableros curados a mano | 10 | Su original, cuando existe; si no, una brecha |
| Listados territoriales parciales | 6 | La tabla maestra territorial |
| Cartografía adaptada | 8 | Marco Geoestadístico DANE (solo Antioquia) |
| Extractos o compilados de un original presente | 7 | El original completo, que sí migra |
| Duplicados exactos | 2 | La copia que migra |
| Documentos de trabajo del equipo | 2 | El registro de fuentes y variables |

Tres referencias que no son datos del repositorio siguen siendo útiles:

- `INVENTARIO_VARIABLES_v_2.xlsx` trae fuente, periodo y periodicidad por indicador, y sirve para completar metadatos.
- Los scripts de homogeneización del proyecto anterior muestran de qué hoja y columna salía cada variable.
- El manifiesto de migración permite ubicar cualquier archivo entre la ruta anterior y la nueva.

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
├── Sistematización fuentes originales - Proyecto Provincias - v4.xlsx   (registro)
├── manifiesto_migracion_originales_v4.csv                               (manifiesto)
├── 00_Documentacion/        (este anexo y la bitácora)
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
    ├── IDEAM/  MEN/  Migracion_Colombia_SITA/  Parques_Nacionales_RUNAP/
    ├── Policia_Nacional/  Superintendencia_Subsidio_Familiar/  UARIV/
    ├── UBPD/  UNGRD/  UNODC_SIMCI/  URT/  XM/
    ├── _Compilaciones_equipo/     (compilaciones de varias fuentes, B)
    └── _Entidad_por_confirmar/    (entidad no verificada)
```

En la raíz solo están los dos archivos de control: el registro de fuentes y variables, y el manifiesto (sección 9). Los datos viven únicamente en `01_Datos/` y la documentación en `00_Documentacion/`.

Las carpetas que empiezan por guion bajo son transitorias. Un archivo sale de ellas cuando se confirma su entidad o se consigue el original de cada parte.

**Contenido al inicio:**

| Entidad | Archivos | Entidad | Archivos |
|---|---|---|---|
| Gobernación de Antioquia | 120 | Migración Colombia (SITA) | 2 |
| DANE | 13 | Función Pública (FURAG) | 2 |
| INS | 7 | MEN | 2 |
| DNP | 6 | 11 entidades con 1 archivo cada una | 11 |
| UARIV | 4 | Carpetas transitorias | 2 |
| UNGRD | 3 | **Total** | **172** |

De los 120 archivos de la Gobernación, 91 son las tablas municipales POTA.

## 6. Criterios de admisión

| Categoría | Definición | ¿Entra? |
|---|---|---|
| **A. Original** | Archivo tal como lo entregó o publicó la entidad. | Sí |
| **B. Original de captura o compilación** | No es la descarga directa, pero no transforma valores. Incluye: copia manual de tablas web, reconstrucción desde una captura de navegador, compilación de cuadros de varias fuentes o columnas del proyecto añadidas sin cambiar los datos. | Sí, con nota que explique qué lo hace B |
| **C. Tratado** | Tiene limpieza, filtro, recorte, cálculo, cruce, agregación o formato del proyecto; o es un extracto o duplicado de un original que ya está. | No |

**Reglas que no admiten excepción:**

- Ningún archivo con "PROVINCIAS" en el nombre entra: son recortes hechos para el proyecto anterior.
- Si existen a la vez un extracto y su original completo, entra solo el original.
- Un archivo C solo reemplaza a un original ausente como excepción aprobada por una persona, y queda registrado como brecha abierta.
- Los archivos B se revisan periódicamente para sustituirlos por la descarga directa cuando esté disponible.

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

El registro es el libro de sistematización. Sus hojas cumplen las funciones que se describen abajo.

**Fuentes.** Una fila por archivo del repositorio. Campos mínimos obligatorios:

| Campo | Contenido |
|---|---|
| Nombre archivo, ruta | Identificación exacta en el repositorio |
| Categoría y nota | A o B; en B, qué lo hace B |
| Entidad fuente | Quién produce el dato |
| Acceso | URL, solicitud oficial o forma de obtención |
| Fecha de corte y de descarga | Cuándo mide el dato y cuándo se obtuvo |
| Cobertura | Territorial (nacional, Antioquia, parcial con número de municipios) y temporal |
| Versión | Vigente, no vigente o por confirmar, cuando hay varias del mismo producto |
| Formato, peso, MD5 | Para verificar integridad |
| Registros individuales | Sí/No: personas, casos, titulares o predios |
| Responsable | Persona que responde por el archivo |

**Variables.** Una fila por variable, con: identificador, definición, tipo y unidad de medida, disponibilidad temporal, archivo original, **hoja y campo dentro del original**, y estado de anclaje. Los estados posibles son:

- **Directo:** el campo está identificado.
- **Por confirmar:** se sabe el archivo, falta la hoja o la columna.
- **Brecha parcial:** el original disponible no cubre toda la variable.
- **Brecha:** no hay original.

**Excluidos.** Archivos que no entran, con su tipo de tratamiento y el original que los reemplaza.

**Brechas y Pendientes.** Lo que falta resolver, con prioridad y decisión requerida.

**Bitácora.** Un registro por cambio: fecha, qué cambió, valor anterior, valor nuevo, motivo, evidencia y quién aprobó.

## 8. Tabla maestra territorial

Es la única base que el repositorio construye, y se trata como un original porque ninguna fuente disponible la ofrece completa.

**Contenido:** una fila por cada uno de los 125 municipios de Antioquia, con estas columnas:

- código DIVIPOLA;
- nombre normalizado (mayúsculas, sin tildes, para cruces);
- nombre de presentación;
- subregión DANE;
- esquema asociativo;
- identificador de provincia.

**Estado: decisión por tomar.** Las fuentes que la componían no coinciden:

- Dos listados asignan provincia a 88 municipios.
- Otro listado, y el derivado usado en el procesamiento, asignan 90: agregan Amalfi a la provincia Minero Agroecológica y Santa Fe de Antioquia a la Turística y Agroecológica.
- Un tercer listado cubre solo 4 de las 11 provincias.

Además, el nombre de la provincia 5 aparece en varias fuentes como «POVINCIA DEL AGUA, BOSQUES Y TURISMO», con la errata. La tabla maestra usa la forma correcta y deja registrada la variante.

**Reglas:**

- Solo una persona puede aprobar un cambio en la conformación de provincias.
- Cada cambio queda en la bitácora con su acto o fuente oficial.

## 9. Integridad y trazabilidad

- **Manifiesto** (`manifiesto_migracion_originales_v4.csv`, en la raíz): una fila por archivo original, con ruta en el proyecto anterior, nombre, categoría, peso en bytes, MD5, marca de pesado, versión, ruta en el repositorio y estado de migración. Es la referencia contra la que se verifica el repositorio. El registro de fuentes describe los archivos; el manifiesto permite comprobar con un script que están todos y que no cambiaron.
- **Verificación:** se recalcula el MD5 de cada archivo y se compara con el manifiesto antes de cada publicación y después de cualquier movimiento de carpetas. Hay tres resultados posibles:
  - un archivo que no coincide es un cambio no registrado;
  - un archivo sin fila es un ingreso no registrado;
  - una fila sin archivo es una pérdida.
- **Trazabilidad hacia el proyecto anterior:** para los 172 archivos migrados, el manifiesto conserva la ruta en `Proyecto-Provincias v2`.
- **Historial:** el control de versiones registra el cuándo; la bitácora registra el porqué y quién lo aprobó.

## 10. Archivos pesados, registros individuales y acceso

**Archivos pesados.** Tres originales superan los 100 MB por archivo que admite GitHub:

- líneas de internet fijo de MinTIC (753 MB);
- proyecciones de población DANE por edad simple (132 MB);
- encuesta de percepción de seguridad (105 MB).

**Decisión por tomar:** almacenamiento externo con referencia en el manifiesto, Git LFS u otra opción. Mientras tanto están registrados, pero no copiados.

**Registros individuales.** Algunos archivos contienen un registro por persona, caso, titular o predio, aunque estén anonimizados:

- encuesta de percepción;
- casos SIVIGILA de intento de suicidio;
- títulos mineros, que traen el nombre del titular;
- tablas POTA por predio.

Por decisión institucional todo el repositorio es accesible al equipo. La marca en el registro existe para que quien use esos archivos no publique resultados que permitan identificar a alguien, y para revisar esa decisión si el acceso se amplía.

## 11. Personas y agentes de IA

Un agente de IA puede hacer buena parte del trabajo operativo con rapidez y sin errores de transcripción, pero no tiene autoridad ni responsabilidad institucional. La regla es simple: **el agente prepara y verifica; la persona decide y responde.**

| El agente de IA puede | Solo una persona puede |
|---|---|
| Inventariar archivos y calcular pesos y MD5 | Aprobar la categoría de cualquier archivo B y de los casos dudosos |
| Leer hojas y encabezados; detectar cobertura, recortes y duplicados | Decidir exclusiones y excepciones a los criterios de admisión |
| Proponer la categoría con su evidencia | Obtener originales: solicitudes a entidades, descargas con credenciales, acuerdos de uso |
| Redactar descripciones y completar el registro con metadatos que estén en el archivo | Confirmar entidad, URL y fecha de corte cuando no constan en el archivo |
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

Agregar un dato nuevo, actualizar uno existente y cerrar un pendiente siguen el mismo ciclo. Las secciones 13 a 15 describen solo lo que cambia en cada caso.

| Paso | Qué se hace | Quién |
|---|---|---|
| 1. Obtención | Conseguir el archivo de la entidad y anotar acceso y fecha de descarga | Persona |
| 2. Revisión | Leer contenido: hojas, cobertura, columnas agregadas, relación con archivos existentes | Agente o persona |
| 3. Clasificación | Proponer A, B o C con evidencia | Agente o persona |
| 4. Aprobación | Aceptar la clasificación; en B, validar la nota | Persona |
| 5. Ubicación | Carpeta de la entidad, sin renombrar el archivo | Agente o persona |
| 6. Registro | Fila en Fuentes, variables afectadas, MD5 en el manifiesto | Agente o persona |
| 7. Verificación | Recalcular MD5 y comprobar que el registro y el repositorio coinciden | Agente o persona |
| 8. Bitácora y publicación | Entrada con motivo y aprobador; publicación del cambio | Persona aprueba y publica |

Un ingreso no está terminado hasta que pasa la verificación del paso 7.

## 13. Protocolo de pendientes y brechas

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

**Brechas abiertas al inicio:**

| Id | Tema | Prioridad |
|---|---|---|
| B-01 | Inventario pecuario municipal | Alta |
| B-02 | Evaluaciones agropecuarias (cultivos) | Alta |
| B-03 | Explotación de oro de aluvión (EVOA) | Alta |
| B-04 | Índice de Ciudades Modernas (ICM) | Alta |
| B-08 | Red vial primaria, secundaria y terciaria (shapefiles) | Alta |
| B-10 | Tablero de seguridad, salud y vivienda: fuente de cada uno de sus 33 indicadores | Alta |
| B-13 | Tabla maestra territorial (sección 8) | Alta |
| B-05 | Hechos victimizantes (RUV) | Media |
| B-06 | Índice de Desempeño Fiscal | Media |
| B-07 | Estado de actualización catastral | Media |
| B-09 | Presupuesto de inversión (API Mapa de Inversiones, sin archivo) | Media |
| B-12 | Índice de Competitividad IMCA 2022 | Media |
| B-11 | Suicidio e intento 2021 | Baja |
| B-14 | Capa RUNAP de áreas protegidas | Baja |
| B-15 | Marco Geoestadístico nacional | Baja |

## 14. Protocolo para agregar datos nuevos

Además del ciclo común:

1. **Antes de obtener el archivo,** comprobar en el registro que no exista ya el mismo producto. Si existe, es una actualización (sección 15), no un ingreso nuevo.
2. **Preferir la fuente primaria.** Si hay descarga oficial, no se acepta una compilación.
3. **Pedir el producto completo** que publica la entidad, no un filtro a Antioquia ni a un grupo de municipios. Si la entidad solo entrega el filtro, se registra como cobertura parcial.
4. **Documentar las variables** que motivaron el ingreso, con hoja y campo en el original.
5. **Entidad nueva:** se crea su carpeta. Si la entidad no está verificada, el archivo va a `_Entidad_por_confirmar/` y se abre un pendiente.

## 15. Protocolo para actualizar datos existentes

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

Mientras no se decida, **no se borra ni se sobrescribe ningún archivo**: el nuevo corte entra junto al anterior. Ya hay precedentes de convivencia de versiones:

- eventos de salud pública;
- valor agregado municipal;
- IRCA;
- mortalidad infantil.

## 16. Estado actual y limitaciones

- **Tres originales pesados** están registrados, pero no copiados (sección 10).
- **La tabla maestra territorial está por construir** (sección 8).
- **Hay 15 brechas abiertas**, siete de prioridad alta (sección 13).
- **Registro de variables:**
  - 335 variables heredadas del proyecto anterior.
  - En 24 están identificados la hoja y el campo en el original.
  - En 229 el campo está por confirmar.
  - 79 dependen de brechas: 48 sin original y 31 con un original parcial.
  - 3 no tienen fuente.
  - 5 filas no tienen identificador.
- **Metadatos incompletos:**
  - la URL y la fecha de corte no están registradas para la mayoría de los archivos;
  - 5 entidades están por confirmar;
  - 163 filas no tienen responsable.
- **Versiones por confirmar:** el IRCA de Antioquia frente al histórico nacional, y dos ediciones de mortalidad infantil con las mismas hojas y valores distintos.
- **Un original no se puede leer:** defunciones no fetales 2022 está protegido con contraseña.
- **Vocabulario sin unificar:**
  - unidades con criterios distintos: porcentaje, fracción 0-1 y escala 0-100;
  - tipos de medida que se solapan: total, cantidad, conteo, numérico.
- **Validación externa:** la única contrastada es la del proyecto anterior, que comparó una sola provincia contra su informe publicado. Los originales se verificaron por integridad y contenido, no contra las entidades.

## 17. Control del documento

| Versión | Fecha | Cambio | Aprobó |
|---|---|---|---|
| 0.1 | 2026-09-16 | Borrador inicial tras la migración | Pendiente |

Este anexo se actualiza en tres casos:

- cuando cambia una regla;
- cuando se cierra una brecha de prioridad alta;
- cuando se toma una de las decisiones marcadas como "decisión por tomar".

Las cifras de las secciones 3, 5, 13 y 16 deben coincidir con el registro de fuentes y variables. Si no coinciden, manda el registro.
