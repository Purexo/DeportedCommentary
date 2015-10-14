from bottle import Bottle, view, static_file, request, html_escape, redirect, response
from urllib.parse import urlparse
import database
import setmimetypes

import json
with open('config.json') as json_data:
    config = json.load(json_data)

app = Bottle()
theme = config['theme'] or 'default'

def set_headers():
    """
        Applique les ces headers  aux pages qui en ont besoin
    """
    
    for url in config["Allow-Origin"]:
        response.add_header('Access-Control-Allow-Origin', url)
    response.set_header('Access-Control-Allow-Credentials', 'true')

def return_host():
    """
        renvois l'adresse simplifie de la requete :
        par exemple http://purexo.eu:8080/
        si le programme est lance a cete adresse
    """
    
    host = urlparse(request.url)
    return '%s://%s' % (host.scheme, host.netloc)

@app.get('/')
@view('view/%s/index.tpl' % theme)
def server_index():
    context = {
        'title': config["sitename"] or "Un Nom Bidon",
        'host': return_host()
    }
    return (context)

@app.get('/static/<filepath:path>')
def server_static(filepath):
    """ Sert les fichiers statiques tel que .js, .css, .jpeg, etc... """
    return static_file(filepath, root='static/%s/' % theme)

@app.get('/list')
@view('view/%s/commentary.tpl' % theme)
def server_list_commentary():
    """
        Renvois la liste des commentaires lie a la page du Referer
    """
    
    set_headers()
    from markdown import markdown
    url = urlparse(request.headers.get('Referer') or '/localhost/')
    context = {
        'listComm': database.listCommentaryFromPages(url),
        'markdown': markdown,
        'host': return_host()
    }
    return(context)

@app.post('/add')
def server_add_commentary():
    """
        Receptionne la requete POST /add pour ajouter un commentaire
    """
    
    set_headers()
    from validate_email import validate_email as is_email
    com = dict()
    com['pseudo'] = request.forms.pseudo if len(request.forms.pseudo) > 0 else None
    com['email'] = request.forms.email if is_email(request.forms.email) else None
    com['website'] = request.forms.website if len(request.forms.website) > 0 else None
    com['content'] = request.forms.content if len(request.forms.content) > 0 else None
    com['website'] = html_escape(com['website'])
    
    referer = request.headers.get('Referer') or '/localhost/'
    url = urlparse(referer)
    
    from akismet import Akismet
    api = Akismet(key=config['akismet-key'] or '', blog_url=referer)
    data = {
        'user_ip': request.remote_addr,
        'user_agent': request.environ['HTTP_USER_AGENT'],
        'comment_type': 'comment',
        'comment_author': com['pseudo'],
        'comment_author_email': com['email'],
        'comment_author_url': com['website']
    }
    
    """
        ajoute le commentaire si il n'est pas considere comme spam
    """
    if not api.comment_check(com['content'], data=data, build_data=True):
        database.addCommentary(url, com)
        api.submit_ham(com['content'], data)
    else:
        api.submit_spam(com['content'], data)
        print("Un commentaire a ete analyse comme spam :")
        print(com)
    redirect(referer)
    return None

@app.get('/integrate')
@view('view/%s/integrate.js' % theme)
def server_integrate_commentary():
    """
        Cette page renvois le code JS permettant de load avec AJAX la liste des commentaires
        + le formulaire pour commenter
    """
    set_headers()
    context = {
        'host': return_host()
    }
    return(context)