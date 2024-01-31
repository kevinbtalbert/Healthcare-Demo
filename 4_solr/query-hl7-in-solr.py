import requests
import json
import os

def query_solr_collection_for_patient_names(solr_endpoint, collection_name):
    url = f"{solr_endpoint}/{collection_name}/select"
    query_params = {
        "q": "*:*",        # Query all documents
        "fl": "patient_s", # Filter to only show the patient_s field
        "rows": 100,       # Adjust the number of rows as needed
        "wt": "json"       # Response format
    }

    response = requests.get(url, params=query_params)

    if response.status_code == 200:
        return response.json()  # Returns the response in JSON format
    else:
        raise Exception(f"Failed to query Solr collection. Status code: {response.status_code}")


# Solr endpoint and collection name
solr_endpoint = os.getenv('SOLR_SERVER_URL')
collection_name = "hl7_messages"  # Replace with your collection name

# Query the collection for patient names
try:
    results = query_solr_collection_for_patient_names(solr_endpoint, collection_name)
    print(json.dumps(results, indent=4))
except Exception as e:
    print(str(e))