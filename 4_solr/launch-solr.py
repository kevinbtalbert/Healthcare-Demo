import subprocess
import os

print("Starting Solr/Banana Server...")

subprocess.run(["/home/cdsw/4_solr/solr-8.9.0/bin/solr start -f -p " + str(os.environ['CDSW_APP_PORT'])], shell=True)