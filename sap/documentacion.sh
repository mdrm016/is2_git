#!/bin/bash 

Usuario='ysapy'

cd /home/"$Usuario"/workspace/is2_git/sap/aplicaciones/autenticacion
mkdir /home/"$Usuario"/workspace/is2_git/sap/Sap_documentacion
mkdir /home/"$Usuario"/workspace/is2_git/sap/Sap_documentacion/Autenticacion
epydoc --html --o /home/ysapy/workspace/is2_git/sap/Sap_documentacion/Autenticacion --name "Sap_documentacion" *.py

cd /home/"$Usuario"/workspace/is2_git/sap/aplicaciones/usuarios
mkdir /home/"$Usuario"/workspace/is2_git/sap/Sap_documentacion/Usuarios
epydoc --html --o /home/ysapy/workspace/is2_git/sap/Sap_documentacion/Usuarios --name "Sap_documentacion" *.py

cd /home/"$Usuario"/workspace/is2_git/sap
mkdir /home/"$Usuario"/workspace/is2_git/sap/Sap_documentacion/Sap
epydoc --html --o /home/ysapy/workspace/is2_git/sap/Sap_documentacion/Sap --name "Sap_documentacion" *.py

cd /home/"$Usuario"/workspace/is2_git/sap/Sap_documentacion/Sap 
sudo firefox index.html
cd /home/"$Usuario"/workspace/is2_git/sap/Sap_documentacion/Usuarios
sudo firefox index.html
cd /home/"$Usuario"/workspace/is2_git/sap/Sap_documentacion/Autenticacion
sudo firefox index.html
