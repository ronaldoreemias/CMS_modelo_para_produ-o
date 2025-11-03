from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost/acompanhantes'
app.config['SECRET_KEY'] = 'teste123'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Acompanhante(db.Model):
    __tablename__ = 'acompanhantes'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    numero = db.Column(db.String(20), nullable=False)
    descricao = db.Column(db.Text)
    idade = db.Column(db.Integer)
    altura = db.Column(db.String(10))
    peso = db.Column(db.String(10))
    cor_olhos = db.Column(db.String(50))
    pe = db.Column(db.String(5))
    horario_atendimento = db.Column(db.String(100))
    a_quem_atende = db.Column(db.String(200))
    possui_local = db.Column(db.Boolean, default=False)
    eh_completa = db.Column(db.Boolean, default=False)
    atende_moteis_hoteis = db.Column(db.Boolean, default=False)
    categoria = db.Column(db.String(50), default='vip')
    ativo = db.Column(db.Boolean, default=True)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)

# Rotas do site
@app.route('/')
def homepage():
    top_vip = Acompanhante.query.filter_by(categoria='topvip', ativo=True).all()
    vip = Acompanhante.query.filter_by(categoria='vip', ativo=True).all()
    da_casa = Acompanhante.query.filter_by(categoria='dacasa', ativo=True).all()
    
    return render_template('modelo.html', top_vip=top_vip, vip=vip, da_casa=da_casa)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('logged_in'):
        return redirect('/admin/simple')
    
    if request.method == 'POST':
        if request.form.get('usuario') == 'admin' and request.form.get('senha') == 'admin':
            session['logged_in'] = True
            flash('Login realizado!', 'sucesso')
            return redirect('/admin/simple')
        else:
            flash('Login inválido', 'erro')
    
    return render_template('login.html')

@app.route('/admin/simple')
def admin_simple():
    if not session.get('logged_in'):
        return redirect('/login')
    
    acompanhantes = Acompanhante.query.all()
    return render_template('admin_dashboard.html', acompanhantes=acompanhantes)

@app.route('/admin/add', methods=['POST'])
def admin_add():
    if not session.get('logged_in'):
        return redirect('/login')
    
    novo = Acompanhante(
        nome=request.form['nome'],
        numero=request.form['numero'],
        descricao=request.form['descricao'],
        idade=request.form['idade'],
        categoria=request.form['categoria']
    )
    db.session.add(novo)
    db.session.commit()
    flash('Acompanhante adicionado!', 'sucesso')
    return redirect('/admin/simple')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

def init_db():
    db.create_all()
    if Acompanhante.query.count() == 0:
        db.session.add(Acompanhante(nome="Exemplo", numero="(00) 00000-0000", categoria="vip", atende_moteis_hoteis="Motel", possui_local="Com Local"))
        db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        init_db()
    app.run(debug=True)