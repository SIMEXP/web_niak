from pyramid.config import Configurator

from . import cfg
from .resources import bootstrap

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings,
                          root_factory=bootstrap)
    config.include('pyramid_mako')
    config.include('cornice')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_static_view('data', cfg.DATA_PATH, cache_max_age=3600)

    config.scan()
    return config.make_wsgi_app()
