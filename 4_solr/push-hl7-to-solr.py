import requests
from datetime import datetime, timedelta
import re
import json
import csv
import random
import os

def generate_past_date(days=30):
    """ Generate a random date within the past 'days' days """
    past_date = datetime.now() - timedelta(days=random.randint(1, days))
    return past_date.strftime("%Y-%m-%d %H:%M:%S")

def parse_hl7_field(segment, field_number):
    try:
        fields = segment.split('|')
        return fields[field_number].strip()
    except IndexError:
        return None
    
def get_random_doctors_note(condition):
    pre_statements = [
        "The patient complained of ",
        "Reason for visit was ",
        "Evaluated patient for ",
        "Visited me because of ",
        "Started treatment for "
    ]
    post_statements = [
        ". Performed tests. ",
        ". ",
        ". Prescribed medication. ",
        ". Drew blood. ",
        ". Discharged. ",
        ". Admitted to hospital. ",
        ". Recommended adjustments. ",
        ". Discussed changes. "
    ]
    return random.choice(pre_statements) + condition.replace('_', ' ').lower() + random.choice(post_statements)

def convert_hl7_to_json(hl7_segments):
    condition = ""
    for segment in hl7_segments:
        if segment.startswith('DG1|'):
            condition_field = parse_hl7_field(segment, 3)
            if condition_field:
                condition = condition_field
            break
            
    extracted_data = {
        "patient_s": "",
        "patient_id": "",
        "department": "",
        "condition": "",
        "visit_date_dt": generate_past_date(),  # Generate a random past date
        "note_txt": get_random_doctors_note(condition),
        "insert_date_dt": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    
    for segment in hl7_segments:
        if segment.startswith('PID|'):
            patient_field = parse_hl7_field(segment, 5)
            patient_id_field = parse_hl7_field(segment, 3)
            if patient_field:
                extracted_data["patient_s"] = re.sub(r'\^', ' ', patient_field)

            if patient_id_field:
                extracted_data["patient_id"] = patient_id_field.split('^')[0]

        elif segment.startswith('PV1|'):
            department_field = parse_hl7_field(segment, 3)
            if department_field:
                extracted_data["department"] = department_field.split('^')[0]

        elif segment.startswith('DG1|'):
            condition_field = parse_hl7_field(segment, 3)
            if condition_field:
                extracted_data["condition"] = condition_field

    return json.dumps(extracted_data, indent=4)

def post_to_solr(hl7_json, solr_endpoint, collection_name):
    url = f"{solr_endpoint}{collection_name}/update/json/docs"
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, headers=headers, data=hl7_json)

    if response.status_code == 200:
        print("HL7 message posted successfully.")
    else:
        print(f"Failed to post HL7 message. Status code: {response.status_code}, Response: {response.text}")
        
def commit_to_solr(solr_endpoint, collection_name):
    url = f"{solr_endpoint}{collection_name}/update?commit=true"
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, headers=headers)

    if response.status_code == 200:
        print("Solr commit successful.")
    else:
        print(f"Failed to commit to Solr. Status code: {response.status_code}, Response: {response.text}")

# Read HL7 messages from CSV
csv_file_path = "/home/cdsw/4_solr/HL7_Messages.csv"
solr_endpoint = os.getenv('SOLR_SERVER_URL')
collection_name = "hl7_messages"

with open(csv_file_path, mode='r', newline='') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
        hl7_json = convert_hl7_to_json(row)
        print(hl7_json)
        post_to_solr(hl7_json, solr_endpoint, collection_name)
        
commit_to_solr(solr_endpoint, collection_name)
