import os
import gradio as gr
import openai
import pandas as pd

# Load patient data from CSV
csv_file_path = '/home/cdsw/2_datasets/patient_data.csv'
patient_df = pd.read_csv(csv_file_path)

# Combine patient ID and name for the dropdown display
patient_options = [f"{row['patient_id']}, {row['name']}" for index, row in patient_df.iterrows()]

# Predefined questions for the user to select from
sample_questions = [
    "What are some medications to treat this condition?",
    "What is a preliminary diagnosis for this patient?",
    "What are suggestions to improve the patient's health?"
    # Add more predefined questions here
]

# Function to retrieve patient profile from the dataframe and get suggestions
def get_patient_info_and_suggestions(patient_info, question, predefined_question):
    patient_id, patient_name = patient_info.split(', ', 1)
    patient_profile = patient_df[patient_df['patient_id'] == patient_id].iloc[0].to_dict()
    profile_str = "\n".join([f"{key}: {value}" for key, value in patient_profile.items() if key != 'patient_id'])

    # Use predefined question if custom question is empty
    actual_question = predefined_question if not question else question
    
    suggestions = ""
    if actual_question:  # Only call OpenAI if there is a question
        open_ai_api_key = os.getenv('OPENAI_KEY')
        openai.api_key = open_ai_api_key

        # Construct the prompt for the OpenAI API call
        prompt = f"Patient profile for {patient_name} ({patient_id}):\n{profile_str}\n\nQuestion:\n{question}\n\nWhat suggestions would you have for this patient? Do not say anything about being an AI."

        # Call the OpenAI API using ChatCompletion
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Specify the correct GPT-4 chat model
            messages=[
                {"role": "system", "content": f"Patient profile for {patient_name} ({patient_id}): {patient_profile}"},
                {"role": "user", "content": actual_question}
            ]
        )
        suggestions = response['choices'][0]['message']['content']

    return profile_str, suggestions

# Custom CSS to further style the interface
custom_css = """
body { font-family: Arial, sans-serif; background-color: #f4f4f2; color: #333; }
h1 { color: #5f5f5f; }
.label, .output_label { font-weight: 600; color: #4a4a4a; }
.gradio-app { background-color: #ffffff; border-radius: 10px; box-shadow: 0 0 20px rgba(0,0,0,0.1); padding: 20px; }
.gradio-dropdown, .gradio-textbox { width: 100%; }
.gradio-textbox { min-height: 100px; }
"""

# Gradio interface setup with title and description
demo = gr.Interface(
    fn=get_patient_info_and_suggestions,
    inputs=[
        gr.Dropdown(choices=patient_options, label="Select Patient"),
        gr.Textbox(label="Enter your question for the phsycian AI to consider", optional=True),
        gr.Radio(choices=sample_questions, label="Or select a predefined question", optional=True),
    ],
    outputs=[
        gr.Textbox(label="Patient Profile"),
        gr.Textbox(label="AI Physician's Suggestion", optional=True),
    ],
    title="Physician Portal",
    description="This portal is designed for doctors to get AI-powered recommendations and ask questions to assist with patient care.",
    theme="huggingface",  # You can choose 'dark' or 'huggingface' which has a professional look
    allow_flagging="never",
    css=custom_css
)


# Launch Gradio app with custom CSS
def main():
    demo.launch(share=True,
            enable_queue=True,
            show_error=True,
            server_name='127.0.0.1',
            server_port=int(os.getenv('CDSW_APP_PORT')))
    
if __name__ == "__main__":
    main()