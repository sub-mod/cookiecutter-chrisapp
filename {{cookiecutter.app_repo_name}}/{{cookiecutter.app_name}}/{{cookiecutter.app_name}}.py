#                                                            _
# {{ cookiecutter.app_name }} {{ cookiecutter.app_type }} app
#
# (c) 2016 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#

import os

# import the Chris app superclass
from chrisapp.base import ChrisApp



class {{ cookiecutter.app_python_class_name }}(ChrisApp):
    """
    {{ cookiecutter.app_description }}.
    """
    AUTHORS         = '{{ cookiecutter.author_name }} ({{ cookiecutter.author_email }})'
    SELFPATH        = os.path.dirname(os.path.abspath(__file__))
    SELFEXEC        = os.path.basename(__file__)
    EXECSHELL       = 'python3'
    TITLE           = '{{ cookiecutter.app_title }}'
    CATEGORY        = '{{ cookiecutter.app_category }}'
    TYPE            = '{{ cookiecutter.app_type }}'
    DESCRIPTION     = '{{ cookiecutter.app_description }}'
    DOCUMENTATION   = '{{ cookiecutter.app_documentation }}'
    VERSION         = '{{ cookiecutter.app_version }}'
    LICENSE         = 'Opensource (MIT)'

    def define_parameters(self):

    def run(self, options):



# ENTRYPOINT
if __name__ == "__main__":
    app = {{ cookiecutter.app_python_class_name }}()
    app.launch()
