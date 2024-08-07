from flask import Flask, render_template, request, redirect, session, flash
from proyectoApp import app

@app.route('/',methods=["GET"])
def despliegaInicio():
    # print("ARRIBA MUCHACHOS")
    return render_template("index.html")