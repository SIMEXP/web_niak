import os


PROJECT_ROOT = os.getenv("PROJECT_ROOT_IN_DOCKER") \
    if os.getenv("PROJECT_ROOT_IN_DOCKER") else '/home/poquirion/simexp/web_niak/niak_server/niak_server/'

DATA_PATH = "data/"

TEMPLATE_PATH = "templates/"

STATIC_PATH = "static/"


