# Create your theme on Deported Commentary
For create a theme you should :

1. Add a folder 'your theme name' in static folder and put your asset in
2. In view folder, copy default folder
   - ```cp view/default view/'your theme name'```
3. Edit the files in your theme
4. edit config.json : put your theme name :
   - "theme": "your theme name",

```
|
|- /static
  |- default
  |- your theme name 
|
|- /view
  |- default
  |- your theme name
```

# What correspond files ?
 - commentary.tpl respond to GET /list
 - index.tpl respond to GET /
 - integrate.js respond to GET /integrate

## var in :
### commentary.tpl
 - listComm : the commentary list, linked to the Referer page.
   - you can use 'for xxx in listComm' to passthrought all comments
   - comments can have attributes :
     - pseudo
     - email (should not be public printed for privacy)
     - website (can be null)
     - content (this is the commentary)
     - last_update (date to posted commentary)
     - (in future a swich for render Markdown or RST)
 - markdown : for render content commentary
   - usage : {{!markdown(com.content)}} '!' is for not escaping html
 - host : url of your service
   - this is for load static ressourses, you shall use complete url like http://your.domain/static/your.css instead of /static/your.css
   
### index.tpl
 - title : this is the "sitename" in your config.json
 - host : url of your service
 
### integrate.js
 - host : url of your service