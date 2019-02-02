import codecs

from airspeed import Template
import moban.utils as utils


class EngineVelocity(object):
    def __init__(self, template_dirs, extensions=None):
        self.template_dirs = template_dirs

    def get_template(self, template_file):
        actual_file = utils.get_template_path(
            self.template_dirs, template_file
        )
        with codecs.open(actual_file, "r", encoding="utf-8") as source:
            template = Template(source.read())
        return template

    def get_template_from_string(self, string):
        return Template(string)

    def apply_template(self, template, data, output):
        rendered_content = template.merge(data)
        return rendered_content
