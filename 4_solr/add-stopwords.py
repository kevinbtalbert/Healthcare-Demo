import subprocess

print(subprocess.run(["sh /home/cdsw/4_solr/add-stopwords.sh"], shell=True))