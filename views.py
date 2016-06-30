"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from PRI_web import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
    
@app.route('/interfaces')
def interfaces():
    """Renders the interfaces page."""
    return render_template(
        'interfaces.html',
        title='Interfaces',
        ifacelist = [["eth0",True,"Wired"],["eth1", True,"Wired"],["wlan0",False,"Wireless"],["lo",True,"Loopback"]],
        year=datetime.now().year,

    )
@app.route('/interfaces/<ifaceid>')
def ifaceDetails(ifaceid):
    """Renders the interfaces setting page."""
    return render_template(
        'ifaceid.html',
        title=ifaceid+ " Settings",
        year=datetime.now().year
    )
    
@app.route('/services')
def services():
    """Renders the services page."""
    return render_template(
        'services.html',
        title='Services',
        services = [["DHCP",True],["DNS", True],["Firewall", True],["NAT", True],["Content Filtering", False],["UPnP", False],["Traffic Shaping (QoS)", True]],
        year=datetime.now().year,

    )
@app.errorhandler(404)
def page_not_found(e):
    return render_template(
        'errors/404.html',
        title="These are not the droids you are looking for",
        year = datetime.now().year
        ), 404