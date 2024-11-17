import gradio as gr
import os
import json

def save_task(task_name, task_number, task_description, max_points, grading_criteria, example_solutions, remarks):
    # Create directory if it doesn't exist
    if not os.path.exists(task_name):
        os.makedirs(task_name)
    
    # Create the task dictionary
    task_data = {
        "Numer zadania": task_number,
        "Treść zadania": task_description,
        "Max liczba punktów": max_points+1,
        "Zasady oceniania": grading_criteria,
        "Przykładowe rozwiązania": example_solutions,
        "Uwagi": remarks
    }
    
    # Path to save the file
    file_path = os.path.join(task_name, f"{task_number}.json")
    
    # Save the JSON file
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(task_data, f, indent=4, ensure_ascii=False)
    
    return f"Zadanie {task_number} zapisane w folderze {task_name}."

# Gradio UI components
task_name_input = gr.Textbox(label="Nazwa arkusza", placeholder="np. Matura 2024")
task_number_input = gr.Textbox(label="Numer zadania", placeholder="np. 3.1")
task_description_input = gr.Textbox(label="Treść zadania", placeholder="Podaj treść zadania", lines=5)
max_points_dropdown = gr.Dropdown(label="Max liczba punktów", choices=[str(i) for i in range(1, 11)], type="index")
grading_criteria_input = gr.Textbox(label="Zasady oceniania", placeholder="Podaj zasady oceniania", lines=5)
example_solutions_input = gr.Textbox(label="Przykładowe rozwiązania", placeholder="Podaj przykładowe rozwiązania", lines=5)
remarks_input = gr.Textbox(label="Uwagi", placeholder="Podaj dodatkowe uwagi", lines=3)

# Button to save the task
save_button = gr.Button("Zapisz zadanie")

# Define the Gradio interface
demo = gr.Interface(
    fn=save_task,
    inputs=[task_name_input, task_number_input, task_description_input, max_points_dropdown, grading_criteria_input, example_solutions_input, remarks_input],
    outputs="text",
    live=False,
    title="Asystent Sprawdzania Wiedzy - Zadania Maturalne",
    description="Wprowadź dane dotyczące zadania maturalnego, aby zapisać je do formatu JSON."
)

# Run the Gradio interface
demo.launch()
