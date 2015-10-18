import peewee

# exemple avec sqlite
DATABASE_CONNECTION = peewee.SqliteDatabase('databases/db.sqlite', pragmas=(
    ('encoding', '"UTF-8"'),
))
 
class BaseModel(peewee.Model):
    class Meta:
        database = DATABASE_CONNECTION

class Sites(BaseModel):
    url = peewee.CharField(max_length=256, null=False, unique=True)

class Pages(BaseModel):
    base_url = peewee.ForeignKeyField(Sites, related_name='Table Pages')
    relative_url = peewee.CharField(max_length=256, null=False, unique=True)

class Commentary(BaseModel):
    pseudo = peewee.CharField(max_length=256, null=False, default='anonymous')
    email = peewee.CharField(max_length=256, null=False, default='anonymous@anonymous.org')
    website = peewee.CharField(max_length=256, null=True)
    content = peewee.TextField(null=False)
    last_update = peewee.DateTimeField(null=False, default=peewee.datetime.datetime.now)
    full_url = peewee.ForeignKeyField(Pages, null=False, related_name='Table Commentaires')
 
for model in (Sites, Pages, Commentary):
    try:
        model.create_table()
    except:
        pass

def separate_url(url):
    return (url.netloc, url.path + ';' + url.params + '?' + url.query)

def listCommentaryFromPages(url):
    base_url, relative_url = separate_url(url)
    req = Commentary.select().join(Pages).where(Pages.relative_url == relative_url).join(Sites).where(base_url == Sites.url)
    return req

def addCommentary(url, com):
    base_url, relative_url = separate_url(url)
    
    site, created = Sites.get_or_create(url=base_url)
    if created: site.save()
    
    page, created = Pages.get_or_create(relative_url=relative_url, base_url=site)
    if created: page.save()
    
    commentary = Commentary(full_url=page)
    if com['pseudo']:
        commentary.pseudo = com['pseudo']
    if com['email']:
        commentary.email = com['email']
    if com['website']:
        commentary.website = com['website']
    if com['content']:
        commentary.content = com['content']
    
    try:
        commentary.save()
    except peewee.IntegrityError as e:
        print(e)