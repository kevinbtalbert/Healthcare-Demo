# Use this to start Solr as an application in CML, or within a session.

import subprocess

print(subprocess.run(["bash /home/cdsw/solr/scripts/start-solr.sh"], shell=True))

print("Start solr command is finished.")
  