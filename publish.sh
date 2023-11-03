#!/bin/bash

generateChanges() {
    carpeta=".versions"
    archivo_concatenado="CHANGES.md"
    if [ -e $archivo_concatenado ]; then
        rm $archivo_concatenado
    fi
    archivos=$(find "$carpeta" -type f -exec ls -t -p "{}" + | awk '{print $NF}')
    echo "## Historial de Cambios" > "$archivo_concatenado"
    for archivo in $archivos; do
        cat "$archivo" >> "$archivo_concatenado"
    done
}


if [ "$#" -eq 0 ]; then
    echo "Error: Se debe proporcionar el número de versión como argumento."
    exit 1
fi

file_version=".versions/$1.md"

if [ -e "$file_version" ]; then
    echo "Existe la info de la version $1."
else
    echo "Error: No existen los cambios para la version $1."
    exit 1
fi

generateChanges

PUBLISH_DATE=$(date '+%Y-%m-%d %H:%M:%S')

echo "$1" > RELEASE
echo "__version__ = '$1'" > tools/sdk/CPCReady/__init__.py

git add .
git commit -m "Change Release file"
git push

git tag $1 -m "Publish Release $1 ($PUBLISH_DATE)"
git push --tags
