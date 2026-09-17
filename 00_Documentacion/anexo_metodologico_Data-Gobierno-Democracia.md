# Anexo metodológico — Repositorio de datos originales Data-Gobierno-Democracia

**Versión:** borrador 0.3 · **Fecha:** 2026-09-17 · **Estado:** en revisión

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
| **B. Original de captura o compilación** | No es la descarga directa, pero no transforma valores. Incluye: copia manual de tablas web, reconstrucción desde una captura de navegador, compilación de cuadros de varias fuentes o columnas añadidas por el equipo sin cambiar los datos. | Sí, con nota que explique qué lo hace B |
| **C. Tratado** | Tiene limpieza, filtro, recorte, cálculo, cruce, agregación o formato hechos por el equipo; o es un extracto o duplicado de un original que ya está. | No |

**Reglas que no admiten excepción:**

- No entran recortes hechos por el equipo a un subconjunto de municipios: se guarda el producto completo de la entidad.
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

- **Manifiesto** (`manifiesto_integridad.csv`, en la raíz): una fila por cada archivo de `01_Datos/`, con ruta, nombre, categoría, peso en bytes, MD5 y fecha de ingreso. Solo describe el contenido de este repositorio y se genera recorriendo `01_Datos/`. El registro dice qué es cada archivo; el manifiesto permite comprobar con un script que están todos y que no cambiaron.
- **Verificación:** se recalcula el MD5 de cada archivo y se compara con el manifiesto antes de cada publicación y después de cualquier movimiento de carpetas. Hay tres resultados posibles:
  - un archivo que no coincide es un cambio no registrado;
  - un archivo sin fila es un ingreso no registrado;
  - una fila sin archivo es una pérdida.
- **Procedencia:** se documenta en el registro con el protocolo de la sección 13.
- **Historial:** el control de versiones registra el cuándo; la bitácora registra el porqué y quién lo aprobó.

## 10. Archivos pesados, registros individuales y acceso

**Archivos pesados.** Tres originales superan los 100 MB por archivo que admite GitHub:

- líneas de internet fijo de MinTIC (753 MB);
- proyecciones de población DANE por edad simple (132 MB);
- encuesta de percepción de seguridad (105 MB).

**Decisión por tomar:** almacenamiento externo con referencia en el registro, Git LFS u otra opción. Mientras tanto están registrados, pero no copiados.

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

Mientras no se decida, **no se borra ni se sobrescribe ningún archivo**: el nuevo corte entra junto al anterior. Ya hay precedentes de convivencia de versiones:

- eventos de salud pública;
- valor agregado municipal;
- IRCA;
- mortalidad infantil.

## 17. Estado actual y limitaciones

- **Tres originales pesados** están registrados, pero no copiados (sección 10).
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
- **Versiones por confirmar:** el IRCA de Antioquia frente al histórico nacional, y dos ediciones de mortalidad infantil con las mismas hojas y valores distintos.
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

Este anexo se actualiza en tres casos:

- cuando cambia una regla;
- cuando se cierra una brecha de prioridad alta o cambia el nivel de procedencia de un grupo de archivos;
- cuando se toma una de las decisiones marcadas como "decisión por tomar".

Las cifras de las secciones 3, 5, 14 y 17 deben coincidir con el registro de fuentes y variables. Si no coinciden, manda el registro.
