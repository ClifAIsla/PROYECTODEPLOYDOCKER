from proyectoApp import app
from flask import Flask

from proyectoApp.controladores import controlador_usuarios

if __name__ == "__main__":
    app.run(debug=True)