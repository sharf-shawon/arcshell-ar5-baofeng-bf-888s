import os
import re

def fix_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove trailing spaces (MD009)
    content = re.sub(r'[ \t]+$', '', content, flags=re.MULTILINE)

    # 2. Ensure headers have blank lines around them (MD022)
    # This regex looks for headers and ensures they are surrounded by blank lines.
    # We'll do this in two steps to avoid complex regex.
    
    lines = content.splitlines()
    new_lines = []
    
    for i, line in enumerate(lines):
        if re.match(r'^#{1,6}\s', line):
            # Before header
            if i > 0 and new_lines and new_lines[-1] != '':
                new_lines.append('')
            
            new_lines.append(line)
            
            # After header
            if i < len(lines) - 1 and lines[i+1] != '':
                new_lines.append('')
        else:
            new_lines.append(line)
            
    # 3. Ensure no consecutive blank lines (MD012)
    final_lines = []
    for line in new_lines:
        if line == '' and final_lines and final_lines[-1] == '':
            continue
        final_lines.append(line)
    
    new_content = '\n'.join(final_lines)
    if not new_content.endswith('\n'):
        new_content += '\n'

    with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(new_content)

files_to_check = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.md') or file.endswith('.yml'):
            files_to_check.append(os.path.join(root, file))

for file_path in files_to_check:
    if file_path.endswith('.md'):
        print(f"Fixing {file_path}")
        fix_markdown(file_path)
    elif file_path.endswith('.yml'):
        print(f"Fixing trailing spaces in {file_path}")
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        new_content = re.sub(r'[ \t]+$', '', content, flags=re.MULTILINE)
        if not new_content.endswith('\n'):
            new_content += '\n'
        with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(new_content)
