<template>
	<div id="Administration" class="d-flex flex-column flex-grow-1">
		<div class="container h-100">
			<ul class="nav nav-tabs mb-3">
				<li class="nav-item">
					<router-link :to="{ name: 'CreateArticle' }" class="nav-link">{{ $t('Create New') }}</router-link>
				</li>
				<li class="nav-item">
					<router-link :to="{ name: 'ArticleList' }" class="nav-link">{{ $t('Articles') }}</router-link>
				</li>
				<li class="nav-item">
					<router-link :to="{ name: 'RecipeList' }" class="nav-link">{{ $t('Recipes') }}</router-link>
				</li>
				<li class="nav-item">
					<router-link :to="{ name: 'IngredientList' }" class="nav-link">{{ $t('Ingredients') }}</router-link>
				</li>
				<li class="nav-item">
					<router-link :to="{ name: 'StaticPages' }" class="nav-link">{{ $t('Static Pages') }}</router-link>
				</li>
				<li class="nav-item">
					<router-link :to="{ name: 'Ads' }" class="nav-link">{{ $t('Ads') }}</router-link>
				</li>
			</ul>
			<router-view/>
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
