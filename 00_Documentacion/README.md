# Documentación

Documentos que explican cómo está organizado el repositorio y cómo se mantiene.

| Archivo | Contenido |
|---|---|
| `anexo_metodologico_Data-Gobierno-Democracia.md` | Anexo metodológico, versión editable (fuente) |
| `anexo_metodologico_Data-Gobierno-Democracia.docx` | La misma versión en Word, para lectura y circulación |

El anexo cubre: propósito y alcance, criterios de admisión de datos, registro de fuentes y variables, tabla maestra territorial, integridad (MD5 y manifiesto), personas y agentes de IA, y los protocolos de ingreso, investigación de procedencia, pendientes, datos nuevos y actualización.

El archivo `.md` es la versión de referencia: el `.docx` se regenera a partir de él y no se edita por separado.

## Cómo regenerar el `.docx`

Con [pandoc](https://pandoc.org) instalado, desde esta carpeta:

```
pandoc anexo_metodologico_Data-Gobierno-Democracia.md -o anexo_metodologico_Data-Gobierno-Democracia.docx
```

En Windows, pandoc se instala con `winget install --id JohnMacFarlane.Pandoc`. El `.docx` usa los estilos por defecto de pandoc; si se quiere la imagen institucional, se agrega `--reference-doc=plantilla.docx` con una plantilla de Word.

Cualquier cambio se escribe en el `.md`, se regenera el `.docx` y se anota la versión en la tabla de control del anexo.
