from jinja2 import Environment, PackageLoader, select_autoescape


class ThreadTemplate(object):
    def __init__(self, filename):
        self.filename = filename
        self.env = Environment(loader=PackageLoader("haasbot", "templates"))

    def load(self, **template_vars):
        template = self.env.get_template(self.filename)
        thread_file = template.render(template_vars)
        return thread_file
