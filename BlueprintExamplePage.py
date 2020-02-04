from flask import Blueprint
"""
neat way to break up our flask app into multiple files so that we don't have one giant file containing every endpoint
"""

blueprint_example_page = Blueprint('blueprint_example_page', __name__)


@blueprint_example_page.route("/blueprint_example_page")
def blueprint_example_function():
    return "this is a blueprint example page!"
