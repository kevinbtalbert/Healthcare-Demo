import requests
import json
import os

def create_solr_collection(solr_endpoint, collection_name):
    url = f"{solr_endpoint}/admin/collections?action=CREATE&name={collection_name}&numShards=1&replicationFactor=1&wt=xml"

    response = requests.get(url)

    if response.status_code == 200:
        content_type = response.headers.get('Content-Type')
        if 'application/json' in content_type and response.text:
            return response.json()  # Parse JSON if the response is JSON
        elif 'application/xml' in content_type:
            # Handle XML response here, if necessary
            return response.text
        else:
            # Handle other content types or empty response
            return response.text
    else:
        raise Exception(f"Failed to query Solr collection. Status code: {response.status_code}")


# Solr endpoint and collection name
solr_endpoint = os.getenv('SOLR_SERVER_URL')  # Replace with your Solr server URL
collection_name = "hl7_messages"  # Replace with your collection name

# Query the collection for patient names
try:
    results = create_solr_collection(solr_endpoint, collection_name)
    print(json.dumps(results, indent=4))
except Exception as e:
    print(str(e))
