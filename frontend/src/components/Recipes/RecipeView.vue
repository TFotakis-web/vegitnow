<template>
	<div id="recipeView">
		<div id="RecipeImageAndStats" class="d-flex flex-column" style="height: 100vh;clip-path: polygon(2% 0%, 98% 0%, 97% 20%, 98% 70%, 96% 90%, 97.5% 95%, 98% 100%, 2% 100%, 3% 95%, 2% 80%, 2% 70%, 3% 20%);">
			<div class="full-box-img flex-grow-1 d-flex flex-column justify-content-end" :style="{ 'background-image': 'url(' + article.Thumbnail + ')' }">
				<div class="container">
					<h1 class="text-white w-100 text-center text-lg-left mb-4" style="text-shadow: black 0 0 20px;">{{ article.Title }}</h1>
				</div>
			</div>
			<div class="bgGreen1" style="">
				<div class="container">
					<div class="row text-center py-4">
						<div class="col-sm-4">
							<h2 class="fgGreen1">{{ $t('Ready in') }}:</h2>
							<p class="font-weight-bold mb-sm-0">{{ article.ReadyIn }} {{ $t('Min') }}</p>
						</div>
						<div class="col-sm-4" style="border-left: dashed 2px #327317; border-right: dashed 2px #327317">
							<h2 class="fgGreen1">{{ $t('Main Ingredients') }}:</h2>
							<p class="font-weight-bold mb-sm-0">
								<span v-for="(ingredient, index) in articleMainIngredients">{{ ingredient.data.Name }}<span v-if="index !== articleMainIngredients.length - 1"> - </span></span>
							</p>
						</div>
						<div class="col-sm-4">
							<h2 class="fgGreen1">{{ $t('Dishes') }}:</h2>
							<p class="font-weight-bold mb-0">{{ article.Dishes }}</p>
						</div>
					</div>
				</div>
			</div>
		</div>
		<div id="Instructions">
			<div class="container">
				<div class="row py-5">
					<div class="col-sm-4 text-center">
						<h2 class="fgGreen1">{{ $t('Ingredients') }}</h2>
						<p v-for="ingredient in articleIngredients">{{ ingredient.Quantity }}gr {{ ingredient.data.Name }}</p>
					</div>
					<div class="col-sm-8" style="border-left: dashed 2px #327317;">
						<h2 class="fgGreen1 text-center text-sm-left">{{ $t('Execution') }}</h2>
						<div v-html="article.Content"></div>
					</div>
				</div>
			</div>
		</div>
		<div id="VideoAndNutrition" v-if="article.YoutubeLink !== ''" class="bgGreen1" style="clip-path: polygon(2% 0%, 98% 0%, 98.5% 20%, 97% 60%, 97% 85%, 98% 100%, 2% 100%, 3% 60%, 1.5% 20%);">
			<div class="container py-5 text-center">
				<div class="row">
					<div class="col-sm-4 text-sm-right">
						<h2 class="fgGreen1 w-100" style="border-bottom: dashed 2px #327317;">{{ $t('Execution from us') }}</h2>
					</div>
					<div class="col-sm-8">
						<div class="embed-responsive embed-responsive-16by9">
							<iframe class="embed-responsive-item" :src="article.YoutubeLink" allowfullscreen></iframe>
						</div>
					</div>
				</div>
				<div class="row mt-3">
					<div class="col-sm-4 text-sm-right ">
						<h2 class="fgGreen1 w-100">{{ $t('Nutrition facts') }}</h2>
					</div>
					<div class="col-sm-8 align-left float-left text-left">
						<NutritionStats></NutritionStats>
					</div>
				</div>
			</div>
		</div>
		<RecommendedRecipes></RecommendedRecipes>
	</div>
</template>

<script>
	import RecommendedRecipes from './RecommendedRecipes';
	import NutritionStats from '../Various/NutritionStats';

	export default {
		name: 'RecipeView',
		components: {
			RecommendedRecipes,
			NutritionStats
		},
		data: function () {
			return {
				id: 0,
				article: {},
				articleIngredients: [],
				ingredients: []
			};
		},
		computed: {
			articleMainIngredients: function () {
				return this.articleIngredients.filter(function (ingredient) {
					return ingredient.IsMainIngredient;
				});
			}
		},
		methods: {
			getArticleData: function () {
				this.$http.get('/api/articleContentTranslation/' + this.id + '/')
					.then((response) => {
						this.article = response.data;
						this.$http.get('/api/ingredientAssociation/' + this.article.Article + '/')
							.then((response) => {
								var articleIngredients = response.data;
								this.$http.get('/api/ingredient/')
									.then((response) => {
										this.ingredients = response.data;
										for (var i = 0; i < articleIngredients.length; i++) {
											articleIngredients[i].data = this.ingredients[articleIngredients[i].Ingredient];
										}
										this.articleIngredients = articleIngredients;
									})
									.catch((err) => {
										console.log(err);
									});
							})
							.catch((err) => {
								console.log(err);
							});
					})
					.catch((err) => {
						console.log(err);
					});
			},
			getIngredients: function () {
				this.$http.get('/api/ingredient/')
					.then((response) => {
						this.ingredients = response.data;
					})
					.catch((err) => {
						console.log(err);
					});
			}
		},
		created: function () {
			this.id = this.$route.params.id;
		},
		mounted: function () {
			this.getArticleData();
			// this.getIngredients();
		}
	};
</script>

<style scoped>

</style>
