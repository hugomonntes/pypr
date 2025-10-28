# PRÁCTICA GUIADA GIT (HUGO MONTES FERNÁNDEZ)
## 1. Creación del directorio

```bash
34674@DESKTOP-TBJ305V MINGW64 ~/Desktop
$ mkdir prueba_git
```

## 2. Crear dos archivos mediante nano dentro del directorio

```bash
34674@DESKTOP-TBJ305V MINGW64 ~/Desktop/prueba_git
$ nano

34674@DESKTOP-TBJ305V MINGW64 ~/Desktop/prueba_git
$ nano

34674@DESKTOP-TBJ305V MINGW64 ~/Desktop/prueba_git
$ ls
script.sh  texto.txt
```

## 3. Inicialización (init y status)

```bash
34674@DESKTOP-TBJ305V MINGW64 ~/Desktop/prueba_git
$ git init
Initialized empty Git repository in C:/Users/34674/Desktop/prueba_git/.git/

34674@DESKTOP-TBJ305V MINGW64 ~/Desktop/prueba_git (master)
```

## 4. Utilizar git status
**Muestra el estado actual del repositorio mostando los archivos que se han modificado, añadido o aún no se han añadido.**

```bash
34674@DESKTOP-TBJ305V MINGW64 ~/Desktop/prueba_git (master)
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        script.sh
        texto.txt

nothing added to commit but untracked files present (use "git add" to track)
```
## 5. Cambiar rama a main mediante git branch

```bash
34674@DESKTOP-TBJ305V MINGW64 ~/Desktop/prueba_git (master)
git branch -m main

34674@DESKTOP-TBJ305V MINGW64 ~/Desktop/prueba_git (main)
```

## 6. Añadir un archivo y visualizar si se añadió correctamente

```bash
34674@DESKTOP-TBJ305V MINGW64 ~/Desktop/prueba_git (main)
$ git add script.sh
warning: in the working copy of 'script.sh', LF will be replaced by CRLF the nex
t time Git touches it

34674@DESKTOP-TBJ305V MINGW64 ~/Desktop/prueba_git (main)
$ git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   script.sh

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        texto.txt
```

## 7. Confirmar los cambios hecho anteriormente (Añadir el archivo script)

```bash
34674@DESKTOP-TBJ305V MINGW64 ~/Desktop/prueba_git (main)
$ git commit -m "Confirmacion Inicial"
[main (root-commit) 6b4d7b5] Confirmacion Inicial
 1 file changed, 2 insertions(+)
 create mode 100644 script.sh

34674@DESKTOP-TBJ305V MINGW64 ~/Desktop/prueba_git (main)
$ git status
On branch main
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        texto.txt

nothing added to commit but untracked files present (use "git add" to track)
```

## 8. Modificar el archivo texto.txt y visualizar estado del repositorio

```bash
34674@DESKTOP-TBJ305V MINGW64 ~/Desktop/prueba_git (main)
$nano texto.txt

34674@DESKTOP-TBJ305V MINGW64 ~/Desktop/prueba_git (main)
$ git status
On branch main
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        texto.txt

nothing added to commit but untracked files present (use "git add" to track)
```

## 9. Añadir el artchivo modificado y ver el estado del repositorio

```bash
34674@DESKTOP-TBJ305V MINGW64 ~/Desktop/prueba_git (main)
$ git add texto.txt
warning: in the working copy of 'texto.txt', LF will be replaced by CRLF the nex
t time Git touches it

34674@DESKTOP-TBJ305V MINGW64 ~/Desktop/prueba_git (main)
$ git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   texto.txt

34674@DESKTOP-TBJ305V MINGW64 ~/Desktop/prueba_git (main)
$ git commit -m "Ampliar explicaion del texto"
[main e547cdd] Ampliar explicaion del texto
 1 file changed, 4 insertions(+)
 create mode 100644 texto.txt

34674@DESKTOP-TBJ305V MINGW64 ~/Desktop/prueba_git (main)
$ git status
On branch main
nothing to commit, working tree clean
```

## 10. Información sobre el repositorio y todos los movimientos realizados sobre el (git show y git log)
```bash
34674@DESKTOP-TBJ305V MINGW64 ~/Desktop/prueba_git (main)
$ git show
commit e547cdd615264972f01242501f21acadb723c884 (HEAD -> main)
Author: hugomonntes <huugomontees@gmail.com>
Date:   Tue Oct 28 10:41:13 2025 +0100

    Ampliar explicaion del texto

diff --git a/texto.txt b/texto.txt
new file mode 100644
index 0000000..8c85792
--- /dev/null
+++ b/texto.txt
@@ -0,0 +1,4 @@
+uno
+dos
+tres
+cuatro

34674@DESKTOP-TBJ305V MINGW64 ~/Desktop/prueba_git (main)
$ git log
commit e547cdd615264972f01242501f21acadb723c884 (HEAD -> main)
Author: hugomonntes <huugomontees@gmail.com>
Date:   Tue Oct 28 10:41:13 2025 +0100

    Ampliar explicaion del texto

commit 6b4d7b5bad6e5fbe1fb2027e6dacbbaf8de4e57d
Author: hugomonntes <huugomontees@gmail.com>
Date:   Tue Oct 28 10:29:35 2025 +0100

    Confirmacion Inicial
```
## 11. Diferencias, muestra la diferencia entre el archivo modificado y el commiteado (git diff)

```bash
34674@DESKTOP-TBJ305V MINGW64 ~/Desktop/prueba_git (main)
$ git diff
warning: in the working copy of 'texto.txt', LF will be replaced by CRLF the nex
t time Git touches it
diff --git a/texto.txt b/texto.txt
index 8c85792..70dc1e3 100644
--- a/texto.txt
+++ b/texto.txt
@@ -1,4 +1,3 @@
 uno
 dos
-tres
-cuatro
+mil

34674@DESKTOP-TBJ305V MINGW64 ~/Desktop/prueba_git (main)
$ git commit -a -m "Probando diff"
warning: in the working copy of 'texto.txt', LF will be replaced by CRLF the nex
t time Git touches it
[main 4c24d50] Probando diff
 1 file changed, 1 insertion(+), 2 deletions(-)

34674@DESKTOP-TBJ305V MINGW64 ~/Desktop/prueba_git (main)
$ nano texto.txt

34674@DESKTOP-TBJ305V MINGW64 ~/Desktop/prueba_git (main)
$ git diff
warning: in the working copy of 'texto.txt', LF will be replaced by CRLF the nex
t time Git touches it
diff --git a/texto.txt b/texto.txt
index 70dc1e3..0b4868c 100644
--- a/texto.txt
+++ b/texto.txt
@@ -1,3 +1,4 @@
 uno
 dos
 mil
+siete añadido
```

## 12. Ignorar archivos (.gitignore)
**Evitamos quen X archivos se gestionen a nivel de versiones, crear archivo .gitignore y añadir la extension de los archivos que te interesa ignorar**

```bash
34674@DESKTOP-TBJ305V MINGW64 ~/Desktop/prueba_git (main)
$ ls -a
./   .git/       hola.java    script.sh  texto.txt
../  .gitignore  importante~  temporal~
```

## 13. Tags y gestión de versiones (git tag y git checkout)

```bash
34674@DESKTOP-TBJ305V MINGW64 ~/Desktop/prueba_git (main)
$ git show 6b4d7b5bad6e5fbe1fb2027e6dacbbaf8de4e57d
commit 6b4d7b5bad6e5fbe1fb2027e6dacbbaf8de4e57d
Author: hugomonntes <huugomontees@gmail.com>
Date:   Tue Oct 28 10:29:35 2025 +0100

    Confirmacion Inicial

diff --git a/script.sh b/script.sh
new file mode 100644
index 0000000..4245b96
--- /dev/null
+++ b/script.sh
@@ -0,0 +1,2 @@
+echo Lsitado completo
+ls -l

34674@DESKTOP-TBJ305V MINGW64 ~/Desktop/prueba_git (main)
$ git tag v0.7

34674@DESKTOP-TBJ305V MINGW64 ~/Desktop/prueba_git (main)
$ git log --oneline
e937b7a (HEAD -> main, tag: v0.7) Añadir todo
4c24d50 Probando diff
e547cdd Ampliar explicaion del texto
6b4d7b5 Confirmacion Inicial

34674@DESKTOP-TBJ305V MINGW64 ~/Desktop/prueba_git (main)
$ git show v0.7
commit e937b7a493324d432878cde4543c347e649d55fa (HEAD -> main, tag: v0.7)
Author: hugomonntes <huugomontees@gmail.com>
Date:   Tue Oct 28 11:03:32 2025 +0100

    Añadir todo

diff --git a/.gitignore b/.gitignore
new file mode 100644
index 0000000..9aba907
--- /dev/null
+++ b/.gitignore
@@ -0,0 +1,3 @@
+*.class
+*~
+!importante~
diff --git a/hola.java b/hola.java
new file mode 100644
index 0000000..38b5180
--- /dev/null
+++ b/hola.java
@@ -0,0 +1,5 @@
+class Hola {
+       public static void main(String args[]){
:
```

## 14. Ramas
**Archivos paralelos a los principales con el objetivo de hacer
pruebas o poner en práctica ideas**

```bash
34674@DESKTOP-TBJ305V MINGW64 ~/Desktop/prueba_git (main)
$ git branch Prueba

34674@DESKTOP-TBJ305V MINGW64 ~/Desktop/prueba_git (main)
$ git log --oneline
e937b7a (HEAD -> main, tag: v0.7, Prueba) Añadir todo
4c24d50 Probando diff
e547cdd Ampliar explicaion del texto
6b4d7b5 Confirmacion Inicial

34674@DESKTOP-TBJ305V MINGW64 ~/Desktop/prueba_git (main)
$ git branch
  Prueba
* main
```

**Para cambiar de rama: git switch nombre_rama**
```bash
34674@DESKTOP-TBJ305V MINGW64 ~/Desktop/prueba_git (main)
$ git switch Prueba
Switched to branch 'Prueba'

34674@DESKTOP-TBJ305V MINGW64 ~/Desktop/prueba_git (Prueba)
$

34674@DESKTOP-TBJ305V MINGW64 ~/Desktop/prueba_git (Prueba)
$ git merge Prueba
Already up to date.
```

## 15. Eliminar y quitar de seguimiento

```bash
34674@DESKTOP-TBJ305V MINGW64 ~/Desktop/prueba_git (Prueba)
$ git rm importante~
rm 'importante~'
```

## 16. Repositorios remotos: GitHub
```bash
git clone https://github.com/hugomonntes/pypr
git push -u origin main 
git push
```