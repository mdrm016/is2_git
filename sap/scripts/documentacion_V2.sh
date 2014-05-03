#!/bin/bash 

Usuario='ysapy'

cd /home/"$Usuario"/workspace/is2_git/sap/aplicaciones/autenticacion
mkdir /home/"$Usuario"/workspace/is2_git/sap/Sap_documentacion
mkdir /home/"$Usuario"/workspace/is2_git/sap/Sap_documentacion/Autenticacion
epydoc --html --o /home/"$Usuario"/workspace/is2_git/sap/Sap_documentacion/Autenticacion --name "Sap_documentacion" *.py

cd ..
cd usuarios
mkdir /home/"$Usuario"/workspace/is2_git/sap/Sap_documentacion/Usuarios
epydoc --html --o /home/"$Usuario"/workspace/is2_git/sap/Sap_documentacion/Usuarios --name "Sap_documentacion" *.py

cd ..
cd proyectos
mkdir /home/"$Usuario"/workspace/is2_git/sap/Sap_documentacion/Proyectos
epydoc --html --o /home/"$Usuario"/workspace/is2_git/sap/Sap_documentacion/Proyectos --name "Sap_documentacion" *.py

cd ..
cd roles
mkdir /home/"$Usuario"/workspace/is2_git/sap/Sap_documentacion/Roles
epydoc --html --o /home/"$Usuario"/workspace/is2_git/sap/Sap_documentacion/Roles --name "Sap_documentacion" *.py

cd ..
cd fases
mkdir /home/"$Usuario"/workspace/is2_git/sap/Sap_documentacion/Fases
epydoc --html --o /home/"$Usuario"/workspace/is2_git/sap/Sap_documentacion/Fases --name "Sap_documentacion" *.py

cd .. 
cd tipoitem
mkdir /home/"$Usuario"/workspace/is2_git/sap/Sap_documentacion/TipoItem
epydoc --html --o /home/"$Usuario"/workspace/is2_git/sap/Sap_documentacion/TipoItem --name "Sap_documentacion" *.py

cd ..
cd tipoatributo
mkdir /home/"$Usuario"/workspace/is2_git/sap/Sap_documentacion/TipoAtributo
epydoc --html --o /home/"$Usuario"/workspace/is2_git/sap/Sap_documentacion/TipoAtributo --name "Sap_documentacion" *.py

cd /home/"$Usuario"/workspace/is2_git/sap
mkdir /home/"$Usuario"/workspace/is2_git/sap/Sap_documentacion/Sap
epydoc --html --o /home/"$Usuario"/workspace/is2_git/sap/Sap_documentacion/Sap --name "Sap_documentacion" *.py

<<<<<<< HEAD
cd ..
cd items
mkdir /home/"$Usuario"/workspace/is2_git/sap/Sap_documentacion/Items
epydoc --html --o /home/"$Usuario"/workspace/is2_git/sap/Sap_documentacion/Items --name "Sap_documentacion" *.py

cd ..
cd relaciones
mkdir /home/"$Usuario"/workspace/is2_git/sap/Sap_documentacion/Relaciones
epydoc --html --o /home/"$Usuario"/workspace/is2_git/sap/Sap_documentacion/Relaciones --name "Sap_documentacion" *.py

cd /home/"$Usuario"/workspace/is2_git/sap/Sap_documentacion/Sap 
sudo firefox -new-tab index.html
cd /home/"$Usuario"/workspace/is2_git/sap/Sap_documentacion/Usuarios
sudo firefox -new-tab index.html
cd /home/"$Usuario"/workspace/is2_git/sap/Sap_documentacion/Autenticacion
sudo firefox -new-tab index.html
cd /home/"$Usuario"/workspace/is2_git/sap/Sap_documentacion/Proyectos
sudo firefox -new-tab index.html
cd /home/"$Usuario"/workspace/is2_git/sap/Sap_documentacion/Roles
sudo firefox -new-tab index.html
cd /home/"$Usuario"/workspace/is2_git/sap/Sap_documentacion/Fases
sudo firefox -new-tab index.html
=======
>>>>>>> branch 'master' of git@github.com:mdrm016/is2_git.git

