import random
import csv
from datetime import datetime
from faker import Faker
# Initialize Faker
fake = Faker()

# Complete list of conditions
conditions = [
    "Abnormal_gait", "Abnormal_muscle_enlargement", "Binge_drinking", "Binge_eating", "Body_aches",
    "Body_pains", "Broken_bones", "Bruising", "Skin_discoloration", "Coarse_hair", "Craving_to_eat_ice",
    "Craving_to_eat_dirt", "Craving_to_eat_paper", "Decreased_appetite", "Decreased_sweating",
    "Developmental_delays", "Difficulty_breathing", "Difficulty_climbing_stairs", "Difficulty_getting_up_from_a_chair",
    "Difficulty_relaxing_muscles_after_contracting_them", "Difficulty_standing", "Difficulty_swallowing",
    "Difficulty_walking", "Change_in_daily_routine", "Distorted_body_image", "Drinking_excessive_fluids",
    "Dry_skin", "Easy_bleeding", "Easy_bruising", "Excessive_body_hair_growth", "Excessive_crying",
    "Excessive_exercising", "Excessively_salty_sweat", "Excessive_sweating", "Feeling_faint",
    "Flaking_skin", "Flushed_skin", "Food_cravings", "Frequent_falls", "Frequent_infections",
    "Frequent_laxative_use", "High_blood_pressure", "Hot_and_dry_skin", "Hot_flashes", "Hyperactive_behavior",
    "Impaired_judgement", "Impaired_social_skills", "Inability_to_care_for_self", "Increased_sensitivity_to_cold",
    "Increased_sensitivity_to_heat", "Increased_thirst", "Involuntary_movements", "Itching_sensation", "burning_sensation",
    "Joint_aches", "Jumpiness", "being_easily_startled", "Loss_of_balance", "Loss_of_coordination", "Low_blood_pressure",
    "Low_self_esteem", "Morning_alcohol_drinking", "Painful_Muscle_cramps", "Painful_Muscle_spasms", "Muscle_stiffness",
    "Muscle_weakness", "Night_sweats", "General_Pain", "Pale_skin", "Palpitations", "Poor_personal_hygiene",
    "Prolonged_bleeding", "Reduced_productivity_at_work", "Restless", "irritability", "Restrictive_dieting", "Seizures",
    "Shaking_chills", "Short_attention_span", "Short_stature", "Skin_peeling", "Skin_cracking", "Skin_scaling",
    "Slow_skeletal_growth", "Socially_withdrawn", "Stiffness", "decreased_movement", "Tires_quickly", "Unusual_behavior",
    "Weakness", "Weight_gain", "Weight_loss"
]

# Complete list of departments
departments = [
    "Acute assessment unit", "Burn center", "Central sterile services department", "Coronary care unit",
    "Emergency department", "Geriatric intensive-care unit", "Intensive care unit", "Medical records department",
    "Neonatal intensive care unit", "On-call room", "Operating room", "Pediatric intensive care unit", 
    "Physical therapy", "Post-anesthesia care unit", "Psychiatric hospital"
]

# Function to generate a random HL7 message
def generate_hl7_message(message_id):
    # Random patient details
    patient_id = random.randint(100000, 999999)
    patient_name = fake.name().replace(" ", "^")
    patient_dob = f"{random.randint(1950, 2010)}0101"
    patient_gender = random.choice(["M", "F"])
    patient_address = fake.address().replace("\n", "^^").replace(" ", "^")
    patient_phone = fake.phone_number()

    # Random department and condition
    department = random.choice(departments)
    condition = random.choice(conditions)

    # Current date and time for message
    current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")

    # Constructing the HL7 message
    hl7_message = [
        f"MSH|^~\\&|SendingApplication|SendingFacility|ReceivingApplication|ReceivingFacility|{current_datetime}||ADT^A01|{message_id}|P|2.3",
        f"EVN|A01|{current_datetime}",
        f"PID|1||{patient_id}^^^Hospital^MR||{patient_name}^^^||{patient_dob}|{patient_gender}||Caucasian|{patient_address}||{patient_phone}|||M||{patient_id}|987-65-4320",
        f"PV1|1|I|{department}^^^Hospital||||1234^Doe^John^A^^^||{patient_phone}|||||||||||{patient_id}|Self|||||||||||||||||||||||||{current_datetime}",
        f"DG1|1||{condition}||{current_datetime[:8]}"
    ]

    return hl7_message

# Generate a few HL7 messages
sample_messages = [generate_hl7_message(i) for i in range(1, 51)]

# Export to CSV
csv_file = "/home/cdsw/4_solr/HL7_Messages.csv"
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['MSH', 'EVN', 'PID', 'PV1', 'DG1'])  # Header
    for message in sample_messages:
        writer.writerow(message)