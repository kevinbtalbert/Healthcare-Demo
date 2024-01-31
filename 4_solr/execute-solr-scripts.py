import subprocess
import cmlapi
import os
import json

client = cmlapi.default_client(url=os.getenv("CDSW_API_URL").replace("/api/v1", ""), cml_api_key=os.getenv("CDSW_APIV2_KEY"))
if os.getenv("PROJECT_NAME") == "Healthcare Demo":
    projects = client.list_projects(search_filter=json.dumps({"name": "Healthcare Demo"}))
else:
    projects = client.list_projects(search_filter=json.dumps({"name": os.getenv("PROJECT_NAME")}))
    
project = projects.projects[0]

applications = client.list_applications(project_id=project.id, search_filter=json.dumps({"subdomain": "solr-app-"}))
solr_application = applications.applications[0]

building_url = os.getenv("CDSW_API_URL")
building_url = building_url.replace('/api/v1', '')

# Check if the URL starts with 'https://' or 'http://'
if building_url.startswith('https://'):
    # Add the subdomain after 'https://'
    building_url = 'https://' + solr_application.subdomain + "." + building_url[8:] + "/solr/"
elif building_url.startswith('http://'):
    # Add the subdomain after 'http://'
    building_url = 'http://' + solr_application.subdomain + "." + building_url[7:] + "/solr/"
    
    
os.environ['SOLR_SERVER_URL'] = building_url

subprocess.run("python /home/cdsw/4_solr/create_collection.py", shell=True)
subprocess.run("python /home/cdsw/4_solr/generate-hl7-data.py", shell=True)
subprocess.run("python /home/cdsw/4_solr/push-hl7-to-solr.py", shell=True)
subprocess.run(["sh /home/cdsw/4_solr/add-stopwords.sh"], shell=True)