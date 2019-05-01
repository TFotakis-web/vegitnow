<template>
	<div id="Administration" class="d-flex flex-column flex-grow-1">
		<!--<div class="navbar-placeholder"></div>-->
		<div class="container h-100">
			<div class="row text-center">
				<!--<h1 class="text-center">Administration</h1>-->
				<router-link :to="{ name: 'CreateArticle' }" class="col">{{ $t('Create New') }}</router-link>
				<router-link :to="{ name: 'ArticleList' }" class="col">{{ $t('Articles') }}</router-link>
				<router-link :to="{ name: 'RecipeList' }" class="col">{{ $t('Recipes') }}</router-link>
				<router-link :to="{ name: 'IngredientList' }" class="col">{{ $t('Ingredients') }}</router-link>
				<router-link :to="{ name: 'StaticPages' }" class="col">{{ $t('Static Pages') }}</router-link>
				<router-link :to="{ name: 'Ads' }" class="col">{{ $t('Ads') }}</router-link>
			</div>
			<div class="row">
				<hr>
			</div>
			<div class="row h-100">
				<!--<transition name="fade">-->
				<router-view/>
				<!--</transition>-->
			</div>
		</div>
	</div>
</template>

<script>
	export default {
		name: 'Administration'
	};
</script>

<style scoped>

</style>
