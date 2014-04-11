#!/bin/bash 

Usuario=`whoami`

cd /home/"$Usuario"/is2_git/is2_git/sap/aplicaciones/autenticacion
mkdir /home/"$Usuario"/is2_git/is2_git/sap/Sap_documentacion
mkdir /home/"$Usuario"/is2_git/is2_git/sap/Sap_documentacion/Autenticacion
epydoc --html --o /home/mdrm016/is2_git/is2_git/sap/Sap_documentacion/Autenticacion --name "Sap_documentacion" *.py

cd /home/"$Usuario"/is2_git/is2_git/sap/aplicaciones/usuarios
mkdir /home/"$Usuario"/is2_git/is2_git/sap/Sap_documentacion/Usuarios
epydoc --html --o /home/mdrm016/is2_git/is2_git/sap/Sap_documentacion/Usuarios --name "Sap_documentacion" *.py

cd /home/"$Usuario"/is2_git/is2_git/sap
mkdir /home/"$Usuario"/is2_git/is2_git/sap/Sap_documentacion/Sap
epydoc --html --o /home/mdrm016/is2_git/is2_git/sap/Sap_documentacion/Sap --name "Sap_documentacion" *.py

cd /home/"$Usuario"/is2_git/is2_git/sap/Sap_documentacion/Sap 
sudo firefox index.html
cd /home/"$Usuario"/is2_git/is2_git/sap/Sap_documentacion/Usuarios
sudo firefox index.html
cd /home/"$Usuario"/is2_git/is2_git/sap/Sap_documentacion/Autenticacion
sudo firefox index.html
