import os
import json
from xia_api import OpenApi
from xia_engine_test import DocumentSimple


class Config:
    DEBUG = True
    DEVELOPMENT = True
    resource_mapping = {
        "Simple": DocumentSimple
    }


class DevConfig(Config):
    DEBUG = True
    DEVELOPMENT = True


class ProdConfig(Config):
    DEBUG = False
    DEVELOPMENT = False


if __name__ == "__main__":
    # The compilation time operation will be defined here
    document_library = {}
    full_spec = OpenApi.get_full_spec(Config.resource_mapping, document_library)
    for doc_name, doc_schema in document_library.items():
        with open(f"./static/specs/documents/{doc_name}.json", "w") as fp:
            json.dump(doc_schema, fp, ensure_ascii=False, indent=2)
    with open(f"./static/specs/openapi.json", "w") as fp:
        json.dump(full_spec, fp, ensure_ascii=False, indent=2)
