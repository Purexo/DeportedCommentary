<!-- --> <link rel="stylesheet" href="{{host}}/static/awesome-font/css/font-awesome.min.css"> <!--  -->
<!--  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css"> -->

<link rel="stylesheet" type="text/css" href="{{host}}/static/css/commentary.css">
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<div id="Commentary">

	<form id="formCommentary" action="{{host}}/add" method="post">
		<div id="headerCommentary">
		    <input name="pseudo" type="text" placeholder="Pseudo" />
		    <input name="email" type="email" placeholder="Email"/>
		    <input name="website" type="url" placeholder="Website"/>
	    </div>
	    <textarea name="content" placeholder="Votre Commentaire" required></textarea>
	    <button type="submit" value="Submit"><i class="fa fa-send fa-1_5x"></i></button>
	</form>

	<div id="CommentaryList">
	  % for com in listComm:
	    <div class="Commentary" id="com-{{com.id}}">
	    	<div class="headerCommentary">
		    	% if com.website:
		    	<a href="{{com.website}}" class="pseudo">
					{{com.pseudo}}
		    	</a>
		    	% else:
		    	<div class="pseudo">{{com.pseudo}}</div>
		    	% end
		    	<a href="#com-{{com.id}}" class="last_update" title="{{com.last_update}}">#com-{{com.id}}</a>
	    	</div>
	    	% # Préprataion du choix de formatage (Markdown ou RST)
	    	% if True:
	    		<div class="content">{{!markdown(com.content)}}</div>
	    	% else :
	    		<div class="content">{{!markdown(com.content)}}</div>
	    </div>
	  % end
	</div>

	<!-- <a href="http://localhost:8080/list/">http://localhost:8080/list</a>  -->

</div>