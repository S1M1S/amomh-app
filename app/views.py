from bottle import TEMPLATE_PATH, route, static_file, jinja2_template as template
from invoices import invoices


TEMPLATE_PATH.append('./app/templates')


@route('/')
@route('/landing')
def home():
    return template ('under-construction.html')
    #  TODO: return template('landing.html')


@route('/website-design/information')
def wd_info():
    return template('website-design/information.html')


@route('/website-design/portfolio')
def wd_port():
    return template('website-design/portfolio.html')


@route('/website-design/quote-estimates')
def wd_quotes():
    return template('website-design/quote-estimates.html')


@route('/website-design/contact-me')
def wd_contact():
    return template('website-design/contact-me.html')


@route('/internet-radio/information')
def ir_info():
    return template('internet-radio/information.html')


@route('/internet-radio/listen')
def ir_listen():
    return template('internet-radio/listen.html')


@route('/music-production/information')
def mp_info():
    return template('music-production/information.html')

@route('/invoices')
def invoice():
    return template('email/invoice/invoice-base.html', invoices=invoices)

@route('/media/<path:path>')
def static_media(path):
    return static_file(path)