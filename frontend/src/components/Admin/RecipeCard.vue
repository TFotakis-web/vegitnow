<template>
	<div class="col-12 col-lg-6 col-xl-4 mb-3">
		<div class="row" :class="{ 'recipe-card-bordered': isMiddle }">
			<div class="col-6">
				<h4>{{ recipe.Title }}</h4>
				<hr class="fgGreen1" style="border-top: dashed 2px;">
				<h5 class="fgGreen1">{{ $t('Main Ingredients') }}:</h5>
				<p style="font-size: 0.8em;">{{ recipe.MainIngredients }}</p>
				<h5 class="fgGreen1">{{ $t('Ready in') }}:</h5>
				<p style="font-size: 0.8em;">{{ recipe.Cooking + recipe.Preparation }}</p>
			</div>
			<div class="col-6 d-table">
				<div class="d-table-cell align-middle">
					<div class="full-screen-img" style="height: 160px;" :style="{ 'background-image': 'url(' + recipe.Thumbnail + ')' }"></div>
				</div>
			</div>
		</div>
		<div class="row py-4">
			<router-link :to="{ name: 'RecipeView', params: { id: recipe.id }}" class="btn px-4 bgGreen0 text-white text-uppercase font-weight-bold mx-auto" style="border-radius: 2rem;">{{ $t('Read more') }}</router-link>
			<button @click="$parent.editArticleId = recipe.id" type="button" class="btn px-4 bg-info text-white text-uppercase font-weight-bold mx-auto" style="border-radius: 2rem;" data-toggle="modal" data-target="#articleEditModal">
				{{ $t('Edit') }}
			</button>
		</div>
	</div>
</template>

<script>
	export default {
		name: 'AdminRecipeCard',
		props: [
			'recipe',
			'isMiddle'
		]
	};
</script>

<style scoped>
	.recipe-card-bordered {
		border-left: dashed 2px var(--v-green6);
		border-right: dashed 2px var(--v-green6);
	}

</style>
