from jinja2 import Environment, PackageLoader


def load_template_file(template_name, **template_vars):
    env = Environment(loader=PackageLoader("haasbot", "templates"))
    template = env.get_template(template_name)
    thread_file = template.render(template_vars)
    return thread_file
