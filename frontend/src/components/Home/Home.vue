<template>
	<div>
		<Carousel></Carousel>
		<JoinOurFamily></JoinOurFamily>
		<IngredientOfTheDay></IngredientOfTheDay>
		<RecommendedRecipes></RecommendedRecipes>
		<RecommendedArticles></RecommendedArticles>
	</div>
</template>

<script>
	import Carousel from './Carousel';
	import JoinOurFamily from './JoinOurFamily';
	import IngredientOfTheDay from './IngredientOfTheDay';
	import RecommendedRecipes from '../Recipes/RecommendedRecipes';
	import RecommendedArticles from '../Articles/RecommendedArticles';

	export default {
		name: 'Home',
		components: {
			Carousel,
			JoinOurFamily,
			IngredientOfTheDay,
			RecommendedRecipes,
			RecommendedArticles
		}
	};
</script>

<style scoped>

</style>
