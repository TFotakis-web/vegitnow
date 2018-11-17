<template>
	<div id="navigationBar">
		<nav class="navbar navbar-expand-md navbar-light bg-white fixed-top d-md-none">
			<div class="container">
				<router-link :to="{ name: 'Home' }">
					<img src="/static/img/logo.png" alt="Vegitnow Logo" height="40">
				</router-link>
				<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
					<span class="navbar-toggler-icon"></span>
				</button>
				<div class="collapse navbar-collapse" id="navbarNav">
					<ul class="navbar-nav">
						<li class="nav-item{% if activeTab == 'recipes' %} active{% endif %}">
							<router-link :to="{ name: 'RecipesList' }" class="nav-link font-weight-bold">Recipes</router-link>
							<!--<a class="nav-link font-weight-bold" href="{% url 'articles:recipesList' %}">{% trans "Recipes" %}</a>-->
						</li>
						<li class="nav-item{% if activeTab == 'tips' %} active{% endif %}">
							<router-link :to="{ name: 'ArticlesList' }" class="nav-link font-weight-bold">Articles</router-link>
							<!--<a class="nav-link font-weight-bold" href="{% url 'articles:tipsList' %}">{% trans "Tips" %}</a>-->
						</li>
						<li class="nav-item{% if activeTab == 'whoWeAre' %} active{% endif %}">
							<router-link :to="{ name: 'WhoWeAre' }" class="nav-link font-weight-bold">Who we are</router-link>
							<!--<a class="nav-link font-weight-bold" href="{% url 'general:whoWeAre' %}">{% trans "Who we are" %}</a>-->
						</li>
						<li class="nav-item{% if activeTab == 'communication' %} active{% endif %}">
							<router-link :to="{ name: 'Communication' }" class="nav-link font-weight-bold">Communication</router-link>
							<!--<a class="nav-link font-weight-bold" href="{% url 'general:communication' %}">{% trans "Communication" %}</a>-->
						</li>
						<li class="nav-item">
							<router-link :to="{ name: 'Shop' }" class="nav-link">
								<div class="vegShop-btn">
									<span>VEG SHOP</span>
								</div>
							</router-link>
							<!--<a href="{% url 'shop:home' %}" class="nav-link">-->
							<!--<div class="vegShop-btn">-->
							<!--<span>VEG SHOP</span>-->
							<!--</div>-->
							<!--</a>-->
						</li>
						<li class="nav-item">
							<!--{% if LANGUAGE_CODE == 'en' %}-->
							<!--<a href="{% url 'general:setLanguage' 'el' %}" class="nav-link">-->
							<!--<div class="locale-btn">-->
							<!--<span>EL</span>-->
							<!--</div>-->
							<!--</a>-->
							<!--{% else %}-->
							<!--<a href="{% url 'general:setLanguage' 'en' %}" class="nav-link ">-->
							<!--<div class="locale-btn">-->
							<!--<span>EN</span>-->
							<!--</div>-->
							<!--</a>-->
							<!--{% endif %}-->
							<router-link :to="{ name: 'Home' }" class="nav-link">
								<div class="locale-btn">
									<span>EN</span>
								</div>
							</router-link>
						</li>
					</ul>
				</div>
			</div>
		</nav>

		<nav class="navbar navbar-light bg-white fixed-top navbar-expand-md flex-nowrap d-none d-md-flex">
			<div class="container">
				<div class="d-flex w-100 align-items-center">
					<div class="">
						<router-link :to="{ name: 'Home' }" class="navbar-brand">
							<img src="/static/img/logo.png" alt="Vegitnow Logo" height="40">
						</router-link>
					</div>
					<div class="flex-grow-1">
						<ul class="navbar-nav w-100 justify-content-center">
							<li class="nav-item{% if activeTab == 'recipes' %} active{% endif %}">
								<router-link :to="{ name: 'RecipesList' }" class="nav-link font-weight-bold">Recipes</router-link>
								<!--<a class="nav-link font-weight-bold" href="{% url 'articles:recipesList' %}">{% trans "Recipes" %}</a>-->
							</li>
							<li class="nav-item{% if activeTab == 'tips' %} active{% endif %}">
								<router-link :to="{ name: 'ArticlesList' }" class="nav-link font-weight-bold">Articles</router-link>
								<!--<a class="nav-link font-weight-bold" href="{% url 'articles:tipsList' %}">{% trans "Tips" %}</a>-->
							</li>
							<li class="nav-item{% if activeTab == 'whoWeAre' %} active{% endif %}">
								<router-link :to="{ name: 'WhoWeAre' }" class="nav-link font-weight-bold">Who we are</router-link>
								<!--<a class="nav-link font-weight-bold" href="{% url 'general:whoWeAre' %}">{% trans "Who we are" %}</a>-->
							</li>
							<li class="nav-item{% if activeTab == 'communication' %} active{% endif %}">
								<router-link :to="{ name: 'Communication' }" class="nav-link font-weight-bold">Communication</router-link>
								<!--<a class="nav-link font-weight-bold" href="{% url 'general:communication' %}">{% trans "Communication" %}</a>-->
							</li>
						</ul>
					</div>
					<div class="">
						<ul class="navbar-nav justify-content-end" style="position: relative; top: 2rem;">
							<!--<li class="nav-item">-->
							<!--<a href="{% url 'shop:home' %}" class="nav-link">-->
							<!--<div class="vegShop-btn">-->
							<!--<span>VEG SHOP</span>-->
							<!--</div>-->
							<!--</a>-->
							<!--</li>-->
							<!--<li class="nav-item">-->
							<!--{% if LANGUAGE_CODE == 'en' %}-->
							<!--<a href="{% url 'general:setLanguage' 'el' %}" class="nav-link">-->
							<!--<div class="locale-btn">-->
							<!--<span>EL</span>-->
							<!--</div>-->
							<!--</a>-->
							<!--{% else %}-->
							<!--<a href="{% url 'general:setLanguage' 'en' %}" class="nav-link">-->
							<!--<div class="locale-btn">-->
							<!--<span>EN</span>-->
							<!--</div>-->
							<!--</a>-->
							<!--{% endif %}-->
							<!--</li>-->

							<li class="nav-item">
								<router-link :to="{ name: 'Shop' }" class="nav-link">
									<div class="vegShop-btn">
										<span>VEG SHOP</span>
									</div>
								</router-link>
								<!--<a href="{% url 'shop:home' %}" class="nav-link">-->
								<!--<div class="vegShop-btn">-->
								<!--<span>VEG SHOP</span>-->
								<!--</div>-->
								<!--</a>-->
							</li>
							<li class="nav-item">
								<!--{% if LANGUAGE_CODE == 'en' %}-->
								<!--<a href="{% url 'general:setLanguage' 'el' %}" class="nav-link">-->
								<!--<div class="locale-btn">-->
								<!--<span>EL</span>-->
								<!--</div>-->
								<!--</a>-->
								<!--{% else %}-->
								<!--<a href="{% url 'general:setLanguage' 'en' %}" class="nav-link ">-->
								<!--<div class="locale-btn">-->
								<!--<span>EN</span>-->
								<!--</div>-->
								<!--</a>-->
								<!--{% endif %}-->
								<router-link :to="{ name: 'Home' }" class="nav-link">
									<div class="locale-btn">
										<span>EN</span>
									</div>
								</router-link>
							</li>
						</ul>
					</div>
				</div>
			</div>
		</nav>
	</div>
</template>

<script>
	export default {
		name: 'NavigationBar'
	};
</script>

<style scoped>

</style>
