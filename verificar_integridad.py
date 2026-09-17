#!/usr/bin/env python3
"""Verifica que los archivos versionados de 01_Datos/ coincidan con manifiesto_integridad.csv.

Uso (desde la raíz del repositorio):

    python verificar_integridad.py

No necesita instalar nada: usa solo la biblioteca estándar de Python 3.
Devuelve 0 si todo coincide y 1 si encuentra algún problema.

Qué revisa, según el anexo metodológico (sección 9):
  - un archivo cuyo MD5 no coincide es un cambio no registrado;
  - un archivo sin fila en el manifiesto es un ingreso no registrado;
  - una fila sin archivo es una pérdida.

Los originales listados en .gitignore (los de más de 100 MB y el de la encuesta
con identificadores) no están en el manifiesto a propósito: no se versionan.
El script los informa aparte, sin tratarlos como error.
"""
import csv
import hashlib
import os
import sys

RAIZ = os.path.dirname(os.path.abspath(__file__))
MANIFIESTO = os.path.join(RAIZ, 'manifiesto_integridad.csv')
DATOS = '01_Datos'


def md5(ruta):
    h = hashlib.md5()
    with open(ruta, 'rb') as f:
        for bloque in iter(lambda: f.read(1 << 22), b''):
            h.update(bloque)
    return h.hexdigest()


def rutas_ignoradas():
    """Rutas de 01_Datos/ listadas en .gitignore (originales que no se versionan)."""
    ignoradas = set()
    gitignore = os.path.join(RAIZ, '.gitignore')
    if os.path.exists(gitignore):
        with open(gitignore, encoding='utf-8') as f:
            for linea in f:
                linea = linea.strip()
                if linea.startswith(DATOS + '/'):
                    ignoradas.add(linea)
    return ignoradas


def archivos_en_disco():
    encontrados = set()
    for carpeta, _, archivos in os.walk(os.path.join(RAIZ, DATOS)):
        for archivo in archivos:
            if archivo == 'README.md':
                continue
            ruta = os.path.relpath(os.path.join(carpeta, archivo), RAIZ)
            encontrados.add(ruta.replace(os.sep, '/'))
    return encontrados


def main():
    if not os.path.exists(MANIFIESTO):
        print('No se encontró manifiesto_integridad.csv en', RAIZ)
        return 1

    with open(MANIFIESTO, encoding='utf-8-sig', newline='') as f:
        filas = list(csv.DictReader(f))

    ignoradas = rutas_ignoradas()
    en_disco = archivos_en_disco()
    en_manifiesto = {f['ruta'] for f in filas}

    perdidos, cambiados, tamano = [], [], []
    for fila in filas:
        ruta = os.path.join(RAIZ, fila['ruta'])
        if not os.path.exists(ruta):
            perdidos.append(fila['ruta'])
            continue
        if os.path.getsize(ruta) != int(fila['bytes']):
            tamano.append(fila['ruta'])
        if md5(ruta) != fila['md5']:
            cambiados.append(fila['ruta'])

    sin_registrar = sorted(en_disco - en_manifiesto - ignoradas)
    presentes_ignorados = sorted(r for r in ignoradas if os.path.exists(os.path.join(RAIZ, r)))
    faltan_ignorados = sorted(r for r in ignoradas if not os.path.exists(os.path.join(RAIZ, r)))

    print(f'Manifiesto: {len(filas)} archivos versionados')
    print(f'Verificados con MD5: {len(filas) - len(perdidos)}')
    print()

    problemas = 0
    if cambiados:
        problemas += len(cambiados)
        print(f'CAMBIO NO REGISTRADO ({len(cambiados)}): el contenido no coincide con su MD5')
        for r in cambiados:
            print('   ', r)
    if tamano:
        print(f'AVISO ({len(tamano)}): el peso no coincide con el manifiesto')
        for r in tamano:
            print('   ', r)
    if perdidos:
        problemas += len(perdidos)
        print(f'PÉRDIDA ({len(perdidos)}): está en el manifiesto pero no en el disco')
        for r in perdidos:
            print('   ', r)
    if sin_registrar:
        problemas += len(sin_registrar)
        print(f'INGRESO NO REGISTRADO ({len(sin_registrar)}): está en el disco pero no en el manifiesto')
        for r in sin_registrar:
            print('   ', r)

    if ignoradas:
        print(f'Originales que no se versionan ({len(ignoradas)}):')
        for r in presentes_ignorados:
            print('    presente en el disco:', r)
        for r in faltan_ignorados:
            print('    no está en este computador:', r)
        print('    Su MD5 está en el registro, no en el manifiesto.')
        print()

    if problemas:
        print(f'Resultado: {problemas} problema(s). Revise el registro antes de publicar.')
        return 1
    print('Resultado: todo coincide.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
