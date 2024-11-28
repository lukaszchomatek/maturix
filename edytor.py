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
    
    return f"Exercise {task_number} saved in folder {task_name}."

# Gradio UI components
task_name_input = gr.Textbox(label="Name of the set", placeholder="for example, IIT 2024")
task_number_input = gr.Textbox(label="Exercise #", placeholder="for example, 3.1")
task_description_input = gr.Textbox(label="Exercise content", placeholder="Put the content here", lines=5)
max_points_dropdown = gr.Dropdown(label="Maximum number of points", choices=[str(i) for i in range(1, 11)], type="index")
grading_criteria_input = gr.Textbox(label="Grading rules", placeholder="Put the grading rules here", lines=5)
example_solutions_input = gr.Textbox(label="Examplary answers", placeholder="Put the examplary answer here", lines=5)
remarks_input = gr.Textbox(label="Remarks", placeholder="Put additional remarks here", lines=3)

# Button to save the task
save_button = gr.Button("Save")

# Define the Gradio interface
demo = gr.Interface(
    fn=save_task,
    inputs=[task_name_input, task_number_input, task_description_input, max_points_dropdown, grading_criteria_input, example_solutions_input, remarks_input],
    outputs="text",
    live=False,
    title="Student's Assistant",
    description="Enter exercise details to save to JSON format."
)

# Run the Gradio interface
demo.launch()
