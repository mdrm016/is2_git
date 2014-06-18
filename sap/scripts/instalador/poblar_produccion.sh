#! /bin/bash
#Creacion y poblacion de BD de produccion
echo "############Creando Base de datos SAP############"
echo "ALTER USER postgres WITH PASSWORD 'postgres';" > comandos.sql
echo "\q" >> comandos.sql
sudo -u postgres psql -a -f comandos.sql
sudo -u postgres createuser -d -a sap
echo "ALTER USER sap WITH PASSWORD 'sap';" > comandos.sql
echo "\q" >> comandos.sql
sudo -u postgres psql -a -f comandos.sql
sudo -u postgres createdb -O sap sap_desarrollo
rm comandos.sql
python syncdb.py
echo "############Poblando BD SAP############"
cat poblacion_produccion.sql | psql sap_desarrollo
echo "############LANZANDO EL NAVEGADOR############"
firefox -new-tab sap.com
#google-chrome -new-tab sap.com
#chromium-browser -new-tab sap.com
