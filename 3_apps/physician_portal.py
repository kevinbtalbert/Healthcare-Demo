import os
import gradio as gr
import openai
import pandas as pd

# Load patient data from CSV
csv_file_path = '/home/cdsw/2_datasets/patient_data.csv'
patient_df = pd.read_csv(csv_file_path)

# Combine patient ID and name for the dropdown display
patient_options = [f"{row['patient_id']}, {row['name']}" for index, row in patient_df.iterrows()]

# Function to retrieve patient profile from the dataframe and get suggestions
def get_patient_info_and_suggestions(patient_info, question):
    patient_id, patient_name = patient_info.split(', ', 1)
    patient_profile = patient_df[patient_df['patient_id'] == patient_id].iloc[0].to_dict()
    profile_str = "\n".join([f"{key}: {value}" for key, value in patient_profile.items() if key != 'patient_id'])

    suggestions = ""
    if question:  # Only call OpenAI if there is a question
        open_ai_api_key = os.getenv('OPENAI_KEY')
        openai.api_key = open_ai_api_key

        # Construct the prompt for the OpenAI API call
        prompt = f"Patient profile for {patient_name} ({patient_id}):\n{profile_str}\n\nQuestion:\n{question}\n\nWhat suggestions would you have for this patient?"

        # Call the OpenAI API using ChatCompletion
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Specify the correct GPT-4 chat model
            messages=[
                {"role": "system", "content": f"Patient profile for {patient_name} ({patient_id}): {patient_profile}"},
                {"role": "user", "content": question}
            ]
        )
        suggestions = response['choices'][0]['message']['content']

    return profile_str, suggestions

# Custom CSS to further style the interface
custom_css = """
body { background-color: #f4f4f2; }
label { font-weight: 600; }
.gradio-app { background-color: #ffffff; border-radius: 10px; box-shadow: 0 0 20px rgba(0,0,0,0.1); }
"""

# Gradio interface setup with title and description
iface = gr.Interface(
    fn=get_patient_info_and_suggestions,
    inputs=[
        gr.Dropdown(choices=patient_options, label="Select Patient"),
        gr.Textbox(label="Enter your question for the doctor to propose", optional=True),
    ],
    outputs=[
        gr.Textbox(label="Patient Profile"),
        gr.Textbox(label="Doctor's Suggestion", optional=True),
    ],
    title="Physician Portal",
    description="This portal is designed for doctors to get AI-powered recommendations and ask questions to assist with patient care.",
    theme="huggingface",  # You can choose 'dark' or 'huggingface' which has a professional look
    allow_flagging="never",
    css=custom_css
)


# Launch Gradio app with custom CSS
iface.launch(share=True, enable_queue=True)
