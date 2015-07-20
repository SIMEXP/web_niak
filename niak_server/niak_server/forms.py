""" All forms used in the site are defines here

"""

import os

import colander
from deform_bootstrap import Form
import deform
from deform.widget import OptGroup


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


class FigureForm(colander.MappingSchema):
    """ Form to request a figure

    """

    Comments= colander.SchemaNode(
        colander.String(),
        title='Comments',
        widget=deform.widget.TextInputWidget(
            size=60, css_class='form-control')
        )

    pipeleine_name = colander.SchemaNode(
        colander.String(),
        title='Name',
        )


    input = colander.SchemaNode(colander.String(),
                                       validator=valid_input,
                                       description='Input path')
    output = colander.SchemaNode(colander.String(),
                                       validator=colander.Length(max=100),
                                       description='Output path')