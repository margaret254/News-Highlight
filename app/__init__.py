from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap

#Initializing applcation

app =Flask(__name__,instance_relative_config = True)

# Setting up Configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

# Initializing Flask Extensions

from app import views