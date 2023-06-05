import os
import shutil
from pylive import ableton

def collect_and_save_projects(master_folder):
    # Get a list of all the project files in the master folder
    project_files = [file for file in os.listdir(master_folder) if file.endswith('.als')]

    # Open each project file and perform "Collect All and Save"
    for project_file in project_files:
        project_path = os.path.join(master_folder, project_file)

        # Open the project in Ableton Live
        live = ableton.Live()
        live.open_project(project_path)

        # Perform "Collect All and Save"
        live.app().collect_all_and_save()

        # Close the project
        live.close_project()

        print(f"Processed project: {project_file}")

    print("All projects have been collected and saved.")

# Specify the master folder containing all the projects
master_folder = '/path/to/master/folder'

# Call the function to collect and save all the projects
collect_and_save_projects(master_folder)
