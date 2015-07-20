

import deform
import deform_bootstrap
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from . import forms



@view_config(route_name='home', renderer='figure.mako')
def my_view(request):
    return {'project': 'niak_server', "fig_form": ""}



@view_config(route_name='simple_form', renderer='figure.mako')
def signin(request):
    schema = forms.FigureForm()
    submit = deform.Button(name='show_plot', css_class='btn btn-action text-right show')
    myform = deform_bootstrap.Form(schema, buttons=(submit,))

    if 'show_plot' in request.POST:
        controls = request.POST.items()
        try:
            appstruct = myform.validate(controls)
        except deform.ValidationFailure as e:
            return {'fig_form': e.render(), 'values': False}
        # Process the valid form data, do some work


        return HTTPFound(location=request.route_url('home'))
    # We are a GET not a POST
    return {"fig_form": myform.render(), "values": None}