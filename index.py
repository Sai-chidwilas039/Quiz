import webbrowser
import os

# Save the HTML content to a specific path
file_path = os.path.abspath('index.html')  # Get the absolute path

html_content = '''
score: userChoices.score
'''

# Save the HTML content to the file
with open(file_path, 'w') as file:
    file.write(html_content)

# Open the HTML file in the default web browser
webbrowser.open_new_tab(file_path)
