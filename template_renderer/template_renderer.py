import os
from jinja2 import Environment, FileSystemLoader

template_dir = os.environ.get('PULUMI_TEMPLATE_DIR') if os.environ.get('PULUMI_TEMPLATE_DIR') else 'templates'
j2_env = Environment(loader=FileSystemLoader(template_dir))

def render_template(filename: str, data: dict = {}) -> str:
    template = j2_env.get_template(filename)

    return template.render(data)
