<template>
	<div id="Administration" class="container mb-5 h-100">
		<div class="navbar-placeholder"></div>
		<h1 class="text-center">Administration</h1>
		<router-link :to="{ name: 'CreateArticle' }" class="nav-link font-weight-bold">{{ $t('Create New') }}</router-link>
		<router-link :to="{ name: 'AdminArticleList' }" class="nav-link font-weight-bold">{{ $t('Articles') }}</router-link>
		<router-link :to="{ name: 'AdminRecipeList' }" class="nav-link font-weight-bold">{{ $t('Recipes') }}</router-link>
		<router-link :to="{ name: 'AdminIngredientList' }" class="nav-link font-weight-bold">{{ $t('Ingredients') }}</router-link>
	</div>
</template>

<script>
	export default {
		name: 'Administration'
	};
</script>

<style scoped>

</style>
