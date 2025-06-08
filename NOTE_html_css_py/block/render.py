from jinja2 import Environment, FileSystemLoader
import os

# Path to the folder containing this script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Path to the 'templates' folder
template_dir = os.path.join(current_dir, 'templates')

# Setup Jinja2 environment
env = Environment(loader=FileSystemLoader(template_dir))

# Load and render 'home.html'
template = env.get_template('home.html')
rendered_html = template.render()

# Write the output to a file
output_path = os.path.join(current_dir, 'output.html')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(rendered_html)

print(f"Rendered HTML saved to {output_path}")
