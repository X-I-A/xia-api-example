import os
import json
from xia_api import OpenApi
from xia_engine_test import DocumentSimple


class Config:
    DEBUG = True
    DEVELOPMENT = True
    API_PREFIX = "/api"
    RESOURCE_MAPPING = {
        "Simple": DocumentSimple
    }


class DevConfig(Config):
    DEBUG = True
    DEVELOPMENT = True


class ProdConfig(Config):
    DEBUG = True
    DEVELOPMENT = False


if __name__ == "__main__":
    # The compilation time operation will be defined here
    document_library = {}
    OpenApi.compile_spec(Config.RESOURCE_MAPPING, document_library, "./static/specs/", "API Example", Config.API_PREFIX)
