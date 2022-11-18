import os
import json
from xia_fields import StringField
from xia_engine import Document
from xia_api import OpenApi


class DocumentSimple(Document):
    _meta = {"collection_name": "DocumentSimple"}
    name: str = StringField(description="Name", sample="Dupont")


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
    OpenApi.compile_page(Config.RESOURCE_MAPPING, "./templates", False)
