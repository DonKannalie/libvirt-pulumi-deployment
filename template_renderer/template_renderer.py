import os
from jinja2 import Template

template_dir = os.environ.get('PULUMI_TEMPLATE_DIR') if os.environ.get('PULUMI_TEMPLATE_DIR') else 'templates'

def render_template(filename: str, data = {}) -> str:
    with open(f'{template_dir}/{filename}.j2', 'r') as template_file:
        template = template_file.read()
        template = Template(template)

        return template.render(data)
