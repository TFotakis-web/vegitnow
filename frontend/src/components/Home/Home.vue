<template>
	<div class="flex-grow-1">
		<Carousel/>
		<JoinOurFamily/>
		<IngredientOfTheDay/>
		<RecommendedRecipes location="home" noAdCards/>
		<RecommendedArticles location="home" noAdCards/>
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
		},
		head: {
			title: function () {
				return {
					inner: this.$t('Home')
				};
			},
			meta: function () {
				return this.$root.headData.defaultMeta();
			}
		}
	};
</script>

<style scoped>

</style>
