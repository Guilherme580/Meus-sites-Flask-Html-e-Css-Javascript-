from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_user
from dotenv import load_dotenv
from models import User
import os


load_dotenv()

bp = Blueprint("seguranca", __name__)

@bp.route("/login_admin", methods=["GET", "POST"])
def login_admin():
    
    if request.method == "POST":
        senha = request.form["senha_admin"]
        
        if senha == os.getenv("admin"):
            usuaio = User.query.first()
            login_user(usuaio)
            
            return redirect(url_for("admin.index")) 
        
    return render_template("login_admin.html")     
        