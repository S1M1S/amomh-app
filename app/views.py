from bottle import TEMPLATE_PATH, route, jinja2_template as template
import app.models

TEMPLATE_PATH.append('./app/templates')

@route('/')
@route('/home')
def home():
    return template('landing.html')

@route('/website-design')
def website_design():
    return template('website_design/website-design.html')