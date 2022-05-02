from flask import Blueprint
'''
Application blueprint
'''

main = Blueprint('main',__name__)

from . import views, error