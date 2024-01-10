# Use this to start Solr as an application in CML, or within a session.

import subprocess

print(subprocess.run(["bash ~/solr/scripts/stop-solr.sh"], cwd="solr", shell=True))

print("Stop solr command is finished.")
  