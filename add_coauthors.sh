#!/bin/bash

# Asegúrate de que estás en el directorio de un repositorio Git
if [ ! -d ".git" ]; then
  echo "Este script debe ejecutarse dentro de un repositorio Git."
  exit 1
fi

# Lista de coautores con sus correos electrónicos noreply de GitHub
coautores=("Franciscolrf <Franciscolrf@users.noreply.github.com>" "rsarayos <rsarayos@users.noreply.github.com>" "DavidAcostaF <DavidAcostaF@users.noreply.github.com>")

# Función para limpiar en caso de error
cleanup() {
    echo "Limpiando estado actual..."
    git cherry-pick --abort 2>/dev/null
    git checkout main
    git branch -D "$branch_name" 2>/dev/null
}

# Atrapar señales de interrupción
trap cleanup EXIT INT TERM

# Cambia a la rama principal (main)
echo "Cambiando a la rama 'main'..."
git checkout main
if [ $? -ne 0 ]; then
  echo "No se pudo cambiar a la rama 'main'. Verifica que exista."
  exit 1
fi

# Asegúrate de tener los últimos cambios de 'main'
echo "Obteniendo últimos cambios de main..."
git pull origin main

# Crear una nueva rama
branch_name="add-coauthors-$(date +%s)"
echo "Creando nueva rama: $branch_name"
git checkout -b "$branch_name"

# Procesar los últimos n commits
echo "¿Cuántos commits quieres modificar?"
read num_commits

# Verificar que el número de commits sea un número válido
if ! [[ "$num_commits" =~ ^[0-9]+$ ]]; then
  echo "Por favor ingresa un número válido de commits."
  exit 1
fi

# Preparar el mensaje de coautores
coauthor_msg="\n\n"
for coautor in "${coautores[@]}"; do
  if [ -n "$coautor" ]; then
    coauthor_msg+="Co-authored-by: $coautor\n"
  fi
done

# Obtener los últimos n commits en orden correcto
commits=($(git log --format="%H" -n "$num_commits" --reverse))

echo "Procesando ${#commits[@]} commits..."

# Por cada commit
for commit in "${commits[@]}"; do
    commit_msg=$(git log -1 --format=%B "$commit")
    commit_subject=$(git log -1 --format=%s "$commit")
    echo "Procesando commit: $commit_subject"

    if git cherry-pick "$commit" 2>/dev/null; then
        # Si el cherry-pick fue exitoso y no tiene coautores
        if ! echo "$commit_msg" | grep -q "Co-authored-by:"; then
            # Agregar coautores
            new_msg="${commit_msg}${coauthor_msg}"
            git commit --amend -m "$new_msg" --no-edit
        fi
    else
        # Si hay conflictos
        echo "⚠️ Conflicto detectado en el commit: $commit_subject"
        echo "Intentando resolver el conflicto automáticamente..."

        # Buscar archivos en conflicto y hacer git add
        conflicted_files=$(git diff --name-only --diff-filter=U)
        if [ -n "$conflicted_files" ]; then
            for file in $conflicted_files; do
                git add "$file"
            done
        fi
        
        # Continuar con el cherry-pick
        git cherry-pick --continue
    fi
done

echo "✅ Proceso completado."
echo "Los commits han sido modificados en la rama: $branch_name"
echo ""
echo "Para subir los cambios, ejecuta:"
echo "git push origin $branch_name"
echo ""
echo "Luego crea un Pull Request en:"
echo "https://github.com/DavidAcostaF/Krello/pull/new/$branch_name"
