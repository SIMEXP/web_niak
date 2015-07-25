""" All forms used in the site are defines here

"""

import os

import colander
from deform_bootstrap import Form
import deform
from deform.widget import OptGroup

from . import cfg

# Validator

def valid_input(node, value):
    """Check if value is an accessible path

    :param node:
    :param value:
    :return:
    """
    if not os.path.isdir(value):

        raise colander.Invalid(node,
                  '{} is not a valid result directory'.format(value))


# forms


class XFigureForm(colander.MappingSchema):
    """ Form to request a figure

    """


    home = os.getenv('HOME')
    input = colander.SchemaNode(colander.String(),
                                validator=valid_input,
                                description='Input path starting, must be in "$HOME/',
                                default=home)

    # output = colander.SchemaNode(colander.String(),
    #                              validator=colander.Length(max=100),
    #                              description='Output path, must be in $HOME/',
    #                              default=home)

