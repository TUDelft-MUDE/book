import os
import re
import shutil
import yaml
import json

# Define the folder where images will be copied
output_folder = "new_images"
base_url = "https://files.mude.citg.tudelft.nl/"

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Function to parse the _toc.yml file and extract all Markdown and Notebook files
def get_files_from_toc(toc_file):
    files = []
    with open(toc_file, "r", encoding="utf-8") as f:
        toc = yaml.safe_load(f)

        # Recursive function to extract file paths
        def extract_files(item):
            if isinstance(item, dict):
                if "file" in item:
                    # Add the file with the appropriate extension
                    file_path = item["file"]
                    if not file_path.endswith((".md", ".ipynb")):
                        if os.path.isfile(file_path + ".md"):
                            file_path += ".md"
                        elif os.path.isfile(file_path + ".ipynb"):
                            file_path += ".ipynb"
                    files.append(file_path)
                if "sections" in item:
                    for section in item["sections"]:
                        extract_files(section)
                if "chapters" in item:
                    for chapter in item["chapters"]:
                        extract_files(chapter)
            elif isinstance(item, list):
                for sub_item in item:
                    extract_files(sub_item)

        # Start extracting files from the "parts" section
        extract_files(toc.get("parts", []))
    return files

# Function to normalize image paths
def normalize_image_path(file_dir, image_path):
    # Check if the path starts with a `/` (absolute path relative to the project root)
    if image_path.startswith("/"):
        # Resolve the path relative to the project root
        project_root = os.getcwd()  # Assuming the script is run from the project root
        resolved_path = os.path.join(project_root, image_path.lstrip("/"))
    else:
        # Resolve the path relative to the file's directory
        resolved_path = os.path.join(file_dir, image_path.lstrip("./"))
    return resolved_path

# Function to find and replace local image references
def process_file(file_path):
    if file_path.endswith(".md"):
        process_markdown(file_path)
    elif file_path.endswith(".ipynb"):
        process_notebook(file_path)

# Process Markdown files
def process_markdown(file_path):
    file_dir = os.path.dirname(file_path)  # Get the directory of the file
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find all standard Markdown image references
    matches = re.findall(r"!\[.*?\]\((.*?)\)", content)
    # Find all MyST figure syntax references
    myst_matches = re.findall(r"\{figure\}\s+(.*?)\n---", content)
    matches.extend(myst_matches)

    for match in matches:
        # Normalize and resolve the image path
        image_path = normalize_image_path(file_dir, match)
        if os.path.isfile(image_path):
            # Copy the image to the output folder
            image_name = os.path.basename(image_path)
            new_path = os.path.join(output_folder, image_name)
            shutil.copy(image_path, new_path)

            # Replace the local URL with the new URL
            new_url = base_url + image_name
            content = content.replace(match, new_url)

    # Write the updated content back to the file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

# Process Jupyter Notebook files
def process_notebook(file_path):
    file_dir = os.path.dirname(file_path)  # Get the directory of the file
    with open(file_path, "r", encoding="utf-8") as f:
        notebook = json.load(f)

    updated = False
    for cell in notebook.get("cells", []):
        if cell.get("cell_type") == "markdown":
            for i, line in enumerate(cell.get("source", [])):
                # Find all standard Markdown image references
                matches = re.findall(r"!\[.*?\]\((.*?)\)", line)
                # Find all MyST figure syntax references
                myst_matches = re.findall(r"\{figure\}\s+(.*?)\n---", line)
                matches.extend(myst_matches)

                for match in matches:
                    # Normalize and resolve the image path
                    image_path = normalize_image_path(file_dir, match)
                    print(f"Resolved image path: {image_path}")  # Debugging output
                    if os.path.isfile(image_path):
                        # Copy the image to the output folder
                        image_name = os.path.basename(image_path)
                        new_path = os.path.join(output_folder, image_name)
                        shutil.copy(image_path, new_path)

                        # Replace the local URL with the new URL
                        new_url = base_url + image_name
                        cell["source"][i] = cell["source"][i].replace(match, new_url)
                        updated = True

    # Write the updated notebook back to the file if changes were made
    if updated:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(notebook, f, indent=2)

# Main function
def main():
    toc_file = "_toc.yml"  # Replace with the path to your _toc.yml file
    files = get_files_from_toc(toc_file)

    print("Files extracted from TOC:", files)  # Debugging output

    for file_path in files:
        # Ensure the file has the correct extension and exists
        if os.path.isfile(file_path):
            print(f"Processing file: {file_path}")  # Debugging output
            process_file(file_path)
        else:
            print(f"Warning: File {file_path} not found or unsupported.")

if __name__ == "__main__":
    main()