import codecs

from airspeed import Template

from moban.externals import file_system


class EngineVelocity(object):
    def __init__(self, template_fs, options=None):
        """
        template_fs is a multfs instance and gives you the power to load
        a template from equiped template directories.
        :param fs.multifs.MultiFS template_fs: a MultiFS instance or a FS instance
        :param options: a dictionary of potential parameters.
                        not used yet.
        """
        self.template_fs = template_fs

    def get_template(self, template_file):
        template_file = file_system.to_unicode(template_file)
        actual_file = self.template_fs.readtext(template_file)
        with codecs.open(actual_file, "r", encoding="utf-8") as source:
            template = Template(source.read())
        return template

    def get_template_from_string(self, string):
        return Template(string)

    def apply_template(self, template, data, output):
        rendered_content = template.merge(data)
        return rendered_content
