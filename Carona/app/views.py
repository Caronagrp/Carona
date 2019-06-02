import psycopg2, psycopg2.extras
from flask import g, render_template, request, redirect, url_for, session
from app import app


@app.before_request
def before_request():
    g.db = psycopg2.connect('dbname=Carona user=postgres password=123 host=127.0.0.1')

@app.route('/Login/', methods=['GET'])
def Login (cpf, senha):
    if cpf and senha == cur.execute(f"SELECT * FROM Cadastro WHERE {cpf}, {senha} "):
        print ("funfou")




@app.route('/')
def index():
  return 'Hello world'