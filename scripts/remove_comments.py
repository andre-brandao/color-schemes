import os
import re
def clean_yaml_comments(directory):
    """
    Removes all comments from .yaml files in the given directory, 
    while preserving valid hex color codes and YAML structure.

    :param directory: Path to the directory containing .yaml files
    """
    if not os.path.isdir(directory):
        print(f"The path '{directory}' is not a valid directory.")
        return

    for file_name in os.listdir(directory):
        if file_name.endswith(".yaml") or file_name.endswith(".yml"):
            file_path = os.path.join(directory, file_name)
            
            with open(file_path, "r") as file:
                lines = file.readlines()
            
            cleaned_lines = []
            for line in lines:
                # Match and retain hex codes with regex
                if re.search(r':\s*"#?[a-fA-F0-9]{6}"', line):
                    # Remove anything after the hex value while preserving YAML syntax
                    match = re.match(r'(.*#?[a-fA-F0-9]{6}".*?)#', line)
                    cleaned_line = match.group(1) if match else line
                    cleaned_lines.append(cleaned_line.rstrip() + "\n")
                else:
                    # For non-hex lines, remove comments after "#"
                    line_content = line.split("#", 1)[0].rstrip()
                    if line_content:  # Skip adding completely blank lines
                        cleaned_lines.append(line_content + "\n")

            # Save cleaned content back to the file
            with open(file_path, "w") as file:
                file.writelines(cleaned_lines)
            
            print(f"Processed {file_name}: all comments removed.")


if __name__ == "__main__":
    directory = '/home/andre/dotfiles/color-schemes/base16'
    clean_yaml_comments(directory)
