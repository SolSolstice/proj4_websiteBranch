
from flask import Blueprint
from flask import render_template

by_Pairing = Blueprint('byPairing', __name__) 


@by_Pairing.route('/byPairing/')
def byPairing():
    return render_template("byPairing.html")