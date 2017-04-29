<html>
<head>
<title></title>
	<link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
	<link rel="stylesheet" href="https://code.getmdl.io/1.3.0/material.yellow-indigo.min.css" />
	<script src="js/material.min.js"></script>
	<style>
		.demo-card-square.mdl-card {
			width: 600px;
		}
		.mybody {
			background: #ECEFF1;
		}
	</style>
</head>
<body class="mybody">
	<header class="mdl-layout__header">
		<div class="mdl-layout__header-row">
			<h1></h1><span class="mdl-layout__title">EatIt</span></h1>
		</div>
	</header>
	<center>
			<br>
			<div class="demo-card-square mdl-card mdl-shadow--2dp">
				<div class="mdl-card__title">
					<h2 class="mdl-card__title-text">{{ name }}</h2>
				</div>
				<div class="mdl-card__supporting-text">
				    <h3 class="mdl-card__title-text">{{ num }}</h3>
				</div>
			</div>
			<br>
			<div class="demo-card-square mdl-card mdl-shadow--2dp">
				<div class="mdl-card__title">
					<h2 class="mdl-card__title-text">Рецепт с <br><a href='http://allrecipes.com'>allrecipes.com</a></h2>
				</div>
				<div class="mdl-card__supporting-text">
					<form method="POST" action="/">
						<div class="mdl-textfield mdl-js-textfield">
							<input class="mdl-textfield__input" type="text" name="url">
							<label class="mdl-textfield__label" for="sample1">Номер рецепта</label>
						</div>
						<input type="submit" class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect">
					</form>
				</div>
			</div>
	</center>
</body>
</html>