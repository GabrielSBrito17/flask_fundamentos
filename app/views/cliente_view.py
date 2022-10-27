from flask import render_template
from app.forms import cliente_form
from app import app, db

# @app.route("/ola", defaults={'nome': None}, methods={'GET', "POST"})
# @app.route("/ola/<string:nome>")
# def teste(nome):
#     return render_template("clientes/teste.html", nome_usuario=nome)
from app.models import cliente_model


@app.route("/cadastrar_cliente", methods=["POST"])
def cadastrar_cliente():
    form = cliente_form.ClienteForm()
    print(form.errors)
    print("chegou aqui")
    if form.validate_on_submit():
        print("chegou aqui1")
        nome = form.nome.data
        email = form.email.data
        data_nascimento = form.data_nascimento.data
        profissao = form.profissao.data
        sexo = form.sexo.data

        cliente = cliente_model.Cliente(
            nome=nome,
            email=email,
            data_nascimento=data_nascimento,
            profissao=profissao,
            sexo=sexo
            )
        try:
            print("chegou aqui2")
            db.session.add(cliente)
            db.session.commit()
            print("chegou aqui3")
        except:
            print("Cliente não cadastrado")
    else:
        print(form.errors)
        print("chegou aqui4")

    return render_template("clientes/form.html", form=form)