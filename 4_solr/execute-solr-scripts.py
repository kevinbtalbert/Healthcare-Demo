import subprocess

subprocess.run("python /home/cdsw/4_solr/create_collection.py", shell=True)
subprocess.run("python /home/cdsw/4_solr/generate-hl7-data.py", shell=True)
subprocess.run("python /home/cdsw/4_solr/push-hl7-to-solr.py", shell=True)
subprocess.run(["sh /home/cdsw/4_solr/add-stopwords.sh"], shell=True)