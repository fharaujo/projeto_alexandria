from flask import render_template , request

from alexandria.run import app, db




@app.route('/sobre')
def sobre():
    # codigo 
    return render_template('about.html')