from bottle import TEMPLATE_PATH, route, jinja2_template as template

TEMPLATE_PATH.append('./app/templates')


@route('/')
@route('/landing')
def home():
    return template('landing.html')


@route('/website-design/information')
def website_design():
    return template('website-design/information.html')


@route('/website-design/portfolio')
def website_design():
    return template('website-design/portfolio.html')


@route('/website-design/quote-estimates')
def website_design():
    return template('website-design/quote-estimates.html')


@route('/website-design/contact-me')
def website_design():
    return template('website-design/contact-me.html')


@route('/internet-radio/information')
def website_design():
    return template('internet-radio/information.html')


@route('/internet-radio/listen')
def website_design():
    return template('internet-radio/listen.html')


@route('/music-production/information')
def website_design():
    return template('music-production/information.html')