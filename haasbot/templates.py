from jinja2 import Environment, PackageLoader, select_autoescape


class ThreadTemplate(object):
    def __init__(self, filename):
        self.filename = filename
        self.env = Environment(loader=PackageLoader("haasbot", "templates"))

    def load(self, template_name):
        template = env.get_template(template_name)
