<template>
	<div id="Administration" class="mb-5 h-100">
		<!--<div class="navbar-placeholder"></div>-->
		<div class="container">
			<div class="row text-center">
			<!--<h1 class="text-center">Administration</h1>-->
			<router-link :to="{ name: 'CreateArticle' }" class="col">{{ $t('Create New') }}</router-link>
			<router-link :to="{ name: 'AdminArticleList' }" class="col">{{ $t('Articles') }}</router-link>
			<router-link :to="{ name: 'AdminRecipeList' }" class="col">{{ $t('Recipes') }}</router-link>
			<router-link :to="{ name: 'AdminIngredientList' }" class="col">{{ $t('Ingredients') }}</router-link>
		</div>
		</div>
		<hr>
		<router-view></router-view>
	</div>
</template>

<script>
	export default {
		name: 'Administration'
	};
</script>

<style scoped>

</style>
