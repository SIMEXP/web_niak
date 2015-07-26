import os
import shutil

import colander
import deform
import deform_bootstrap
from pyramid import exceptions, response
from pyramid.view import view_config, render_view_to_response
from pyramid.renderers import render_to_response
from pyramid.httpexceptions import HTTPFound
from cornice.resource import resource, view, Service


from . import forms, cfg


home = Service(name='home', path='/', description="Simplest app", renderer="form.mako")

@home.get()
def get_home(request):
    return {"fig_form": request.route_url('upload'), "values": None, "fig": ""}


upload = Service(name='upload', path='/upload', description="Simplest app", renderer="upload.mako")

@upload.get()
def get_upload(request):
    return {"fig_form": "", "values": None, "fig": ""}

@upload.post()
def post_upload(request):
    file = request.POST['files']


    if not os.path.isdir(cfg.DATA_PATH):
        os.mkdir(cfg.DATA_PATH)

    out_path = os.path.join(cfg.PROJECT_ROOT, cfg.DATA_PATH, file.filename)

    with open(out_path, "wb") as outfp:
        outfp.write(file.file.read())

    return HTTPFound(location=request.static_url("niak_server:{}{}".format(cfg.DATA_PATH, file.filename)))



@resource(collection_path='/data', path='/data/{figure}', renderer='figure.mako')
class FigViews(object):

    def __init__(self, request):
        self.request = request


    def get(self):
        name = self.request.matchdict['name']
        return {self.request.static_url("niak_server:{}{}".format(cfg.DATA_PATH, name))}



@resource(collection_path='/all', path='/all/{template}')
class RandomTemplate(object):

    def __init__(self, request):
        self.request = request


    def get(self):

        name = self.request.matchdict['template']
        full_path = os.path.join(cfg.PROJECT_ROOT, cfg.TEMPLATE_PATH, name)

        if name in self.collection_get()['templates']:
            return response.FileResponse("{}".format(full_path))
        else:
            raise exceptions.NotFound("{} not in /templates dir".format(name))

    def collection_get(self):
        """
        :return: All templates in the project
        """
        template_path = os.path.join(cfg.PROJECT_ROOT, cfg.TEMPLATE_PATH)
        all_templates = os.listdir(template_path)

        return {'templates': all_templates}

