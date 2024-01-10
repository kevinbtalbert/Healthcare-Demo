import subprocess

print(subprocess.run(["bash /home/cdsw/solr/scripts/install-java_and_solr.sh"], shell=True))

print("Install-java11 & Solr is finished")
