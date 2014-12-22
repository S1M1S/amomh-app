from bottle import TEMPLATE_PATH, route, jinja2_template as template
import app.models

TEMPLATE_PATH.append('./app/templates')

@route('/')
@route('/landing')
def home():
    return template('landing.html')

@route('/website-design/information')
def website_design():
    return template('website_design/information.html')

@route('/website-design/portfolio')
def website_design():
    return template('website_design/portfolio.html')

@route('/website-design/contact-me')
def website_design():
    return template('website_design/contact-me.html')

@route('/internet-radio/information')
def website_design():
    return template('internet_radio/information.html')

@route('/internet-radio/listen')
def website_design():
    return template('internet_radio/listen.html')

@route('/music-production/information')
def website_design():
    return template('music_production/information.html')