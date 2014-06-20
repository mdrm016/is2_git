#!/bin/bash
dropdb sap_produccion
createdb -O sap sap_produccion
sed -i 's/''sap_desarrollo''/''sap_produccion''/g' /home/ysapy/workspace/is2_git/sap/sap/settings.py
sudo rm -rf poblacion_desarrollo.sql
pg_dump -c sap_desarrollo > poblacion_desarrollo.sql
cat poblacion_produccion.sql | psql sap_produccion
sudo /etc/init.d/apache2 restart
