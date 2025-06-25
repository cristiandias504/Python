# Primero
# Es necesario configurar el archivo .gitconfig para agregarle un nombre de usuario y un correo
# git config --global user.email "cristian@gmail.com"
# git config --global user.email "cristian@gmail.com"
# --global especifica que se aplicara a todo el equipo, no solo a un proyecto o un usuario en particular

# Para configurar un alias
# git config --global alias.tree "log --graph --decorate --all --oneline"
# Util para automatizar algun comando, tree es el nombre del alias y con el cual se ejecutara
# git tree, Se puede poner el nombre que quiera

# Para ignorar algun fichero o carpeta y no añadirlos a git
# crear un archivo llamado .gitignore
# dentro de el colocar el nombre del fichero a ignorar





# Creamos una carpeta donde se va a almacenar el proyecto y nos dirigimos a ella
# Para iniciar git el comando
# git init

# Para ver el estado actual de los archivos
# git status

# Para añadir un fichero a git
# git add "Nombre del fichero"

# Para crear un commit (Punto de restauración o respaldo del proyecto)
# git commit -m "Mensaje indicando que cambia o por que se hace el respaldo"
# -m es necesario, sin el no es posible hacer el commit, e indica el mensaje entre comillas

# Para ver los logs de los cambios hechos
# git log

# Para ver todos los logs, incluyendo los eliminados mediante git reset --hard
# git reflog

# Para ver los cambios hechos desde el ultimo conmmit
# git diff

# Para ver que ficheros han tenido cambios desde la ultima copia
# git reset





# Para restaurar un archivo a la ultima copia guardada
# git checkout "Nombre del archivo"

# Para llevar el head sin desplazar el main a una version anterior
# git checkout "ID de la version"

# Para que el head vuelva a donde esta el main
# git checkout main




# Para volver a una version atras y descartar todos los cambios de ahi en adelante
# git reset --hard "ID de la version a la que queremos volver"

# Para ir a una version mas adelante despues de haberla eliminado con reset --hard
# ejecutar git reflog para ver los logs eliminados y con reset --hard ir al ID deseado

# Para añadir un tag a una version
# git tag nombre 
# Puede servir para etiquetar algun punto para diferenciarlo de los demas

# Para ver los tags que tenemos
# git tag



# RAMAS - BRANCH

# Para crear una rama
# git branch "Nombre de la rama"

# Para cambiar entre ramas
# git switch "Nombre de la rama"

# Para traer los cambios de una rama a otra
# Ubicarse en la rama a la que se quieren llevar los cambios
# git merge "Nombre de la rama de la que se quieren traer los cambios"
# Para salir del menu que aparece  ESC - ":wq" - ENTER

# Elimiar una rama
# gut branch -d "Nombre de la rama"


# STASH
# Sirve para guardar cambios temporales sin que queden registrados como un commit
# El commit se debe usar para guardar codigo que funcione

# Para guardar un stash
# git stash

# Para ver los stash hechos
# git stash list

# Para volver al stash 
# git stash pop

# Para eliminar el stash
# git stash drop