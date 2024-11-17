import gradio as gr
import os
import json
import random
from groq import Groq

def load_random_task(folder_name):
    # Check if the folder exists
    if not os.path.exists(folder_name):
        return "Podany folder nie istnieje.", "", "", ""
    
    # Get a list of all JSON files in the folder
    files = [f for f in os.listdir(folder_name) if f.endswith('.json')]
    if not files:
        return "Brak zadań w podanym folderze.", "", "", ""
    
    # Choose a random file
    random_file = random.choice(files)
    
    # Load the task data from the JSON file
    with open(os.path.join(folder_name, random_file), "r", encoding="utf-8") as f:
        task_data = json.load(f)
    
    # Extract the relevant fields
    task_number = task_data.get("Numer zadania", "")
    task_description = task_data.get("Treść zadania", "")
    max_points = task_data.get("Max liczba punktów", "")
    grading_criteria = task_data.get("Zasady oceniania", "")
    example_solutions = task_data.get("Przykładowe rozwiązania", "")
    remarks = task_data.get("Uwagi", "")
    
    # Store the additional fields for later use
    global current_task_data
    current_task_data = {
        "task_number": task_number,
        "task_description": task_description,
        "max_points": max_points,
        "grading_criteria": grading_criteria,
        "example_solutions": example_solutions,
        "remarks": remarks
    }
    
    return task_number, task_description, max_points, ""

def check_answer(api_key, user_answer):
    if not current_task_data:
        return "Najpierw wylosuj zadanie."
    
    # Load the prompt from the file
    with open("prompt.txt", "r", encoding="utf-8") as f:
        system_prompt = f.read()
    
    # Format the prompt with the current task data
    formatted_prompt = system_prompt.format(
        task_description=current_task_data["task_description"],
        max_points=current_task_data["max_points"],
        grading_criteria=current_task_data["grading_criteria"],
        example_solutions=current_task_data["example_solutions"],
        remarks=current_task_data["remarks"],
    )
    
    # Initialize the Groq client
    client = Groq(api_key=api_key)
    
    # Make a request to the Groq model
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": formatted_prompt
            },
            {
                "role": "user",
                "content": "Odpowiedź użytkownika: " + user_answer
            }
        ],
        model="llama-3.2-90b-text-preview",
    )
    
    # Return the response from the model
    return chat_completion.choices[0].message.content

# Gradio UI components
api_key_input = gr.Textbox(label="Klucz API Groq", placeholder="Wprowadź swój klucz API", type="password")
folder_name_input = gr.Textbox(label="Nazwa folderu z zadaniami", placeholder="np. Matura 2024")
random_task_button = gr.Button("Wylosuj zadanie")

task_number_output = gr.Label(label="Numer zadania")
task_description_output = gr.Label(label="Treść zadania")
max_points_output = gr.Label(label="Max liczba punktów")
user_answer_input = gr.Textbox(label="Twoja odpowiedź", placeholder="Wpisz swoją odpowiedź tutaj", lines=5, interactive=True)

check_button = gr.Button("Sprawdź")
model_response_output = gr.Textbox(label="Odpowiedź modelu", interactive=False, lines=5)

# Define the Gradio interface using Blocks to separate actions
demo = gr.Blocks()

with demo:
    with gr.Row():
        folder_name_input.render()
        random_task_button.render()
    
    task_number_output.render()
    task_description_output.render()
    max_points_output.render()
    user_answer_input.render()
    
    with gr.Row():
        api_key_input.render()
        check_button.render()
    
    model_response_output.render()

    # Button actions
    random_task_button.click(load_random_task, inputs=[folder_name_input], outputs=[task_number_output, task_description_output, max_points_output])
    check_button.click(check_answer, inputs=[api_key_input, user_answer_input], outputs=model_response_output)

# Run the Gradio interface
demo.launch()
