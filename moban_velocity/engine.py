import codecs

from airspeed import Template

from moban.externals import file_system
import moban.utils as utils


class EngineVelocity(object):
    def __init__(self, template_fs, extensions=None):
        self.template_fs = template_fs

    def get_template(self, template_file):
        actual_file = utils.get_template_path(
            self.template_fs, template_file
        )
        with codecs.open(actual_file, "r", encoding="utf-8") as source:
            template = Template(source.read())
        return template

    def get_template_from_string(self, string):
        return Template(string)

    def apply_template(self, template, data, output):
        rendered_content = template.merge(data)
        return rendered_content
