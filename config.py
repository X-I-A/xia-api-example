import os
import json


class Config:
    DEBUG = True
    DEVELOPMENT = True


class DevConfig(Config):
    DEBUG = True
    DEVELOPMENT = True


class ProdConfig(Config):
    DEBUG = False
    DEVELOPMENT = False
