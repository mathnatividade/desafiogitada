import os
import json
from jinja2 import Template

# Carrega dados do JSON
with open('resources/posts.json') as json_file:
    dados = json.load(json_file)

# Substitui as quebras de linha por <br> no conteúdo
for postagem in dados:
    postagem['conteudo'] = postagem['conteudo'].replace('\n', '<br>')

# Carrega o template HTML
with open('templates/model.html') as template_file:
    template = Template(template_file.read())

# Gera páginas HTML
for postagem in dados:
    html = template.render(
        titulo=postagem['titulo'],
        autor=postagem['autor'],
        data=postagem['data'],
        conteudo=postagem['conteudo']
    )

    # Salva o HTML gerado em um arquivo
    with open(f'docs/posts/{postagem["titulo"].lower().replace(" ", "_")}.html', 'w') as output_file:
        output_file.write(html)
