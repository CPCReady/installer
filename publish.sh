#!/bin/bash

generateChanges() {
    carpeta="docs/versions"
    archivo_concatenado="docs/CHANGES.md"
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

file_version="docs/versions/$1.md"

if [ -e "$file_version" ]; then
    echo "Exite la info de la version $1."
else
    echo "Error: No existen los cambios para la version $1."
    exit 1
fi

generateChanges

PUBLISH_DATE=$(date '+%Y-%m-%d %H:%M:%S')

echo $1 > RELEASE

git add .
git commit -m "Release $1 ($PUBLISH_DATE)"
git push

git tag $1 -m "$2"
git push --tags