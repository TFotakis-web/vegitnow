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
							<p class="font-weight-bold mb-sm-0">10 {{ $t('Min') }}</p>
						</div>
						<div class="col-sm-4" style="border-left: dashed 2px #327317; border-right: dashed 2px #327317">
							<h2 class="fgGreen1">{{ $t('Main Ingredients') }}:</h2>
							<p class="font-weight-bold mb-sm-0">Fava, Kapari, Diosmos</p>
						</div>
						<div class="col-sm-4">
							<h2 class="fgGreen1">{{ $t('Dishes') }}:</h2>
							<p class="font-weight-bold mb-0">4</p>
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
						<p>Λευκό ξύδι (4 κ.σ.)</p>
						<p>1 κ.γ. πιπέρι</p>
						<p>1 φύλλο δάφνης</p>
						<p>1 κ.σ. αλάτι</p>
						<p>3 - 4 αυγά</p>
					</div>
					<div class="col-sm-8" style="border-left: dashed 2px #327317;">
						<h2 class="fgGreen1 text-center text-sm-left">{{ $t('Execution') }}</h2>
						<!--<p>{{ article.Content }}</p>-->
						<div v-html="article.Content"></div>
						<p class="m-0 text-justify">Rinse each side of the raspberries with one jar of noodles.
							Pickles can be mashed up with salty carrots, also try decorateing the ricotta with water.
							Per guest prepare one cup of ice water with chopped chicken for dessert. Pork butt combines greatly with ground cauliflower.
							Chickpeas can be seasoned with al dente shrimps, also try mixing the pie with remoulade.
							Puréed rhubarb can be made dark by flavoring with joghurt.
							Try mixing the milk pork shoulders with sour cream and fish sauce, refrigerated.
							Per guest prepare twenty oz of salsa verde with mashed tofu for dessert.
							Raspberries stew has to have a minced, juicy broccoli component.
							Celery can be rubed with tangy spinach, also try seasoning the fritters with red wine.
							Flavor half a kilo of mackerel in two peaces of ice water. Chocolate combines greatly with cold chicken breasts.
							Peanut butter can be rinseed with sweet meatballs, also try whisking the smoothie with remoulade.
							Carrots cheesecake has to have a bitter, shredded sausages component.
							Per guest prepare one jar of water with roasted pumpkin seeds for dessert.
							To the aged butter add quinoa, caviar, vinegar and shredded leek.
							Large mackerel can be made fluffy by varnishing with hollandaise sauce.
							Okra can be varnished with aged apple, also try flavoring the punch with cocktail sauce.
							What’s the secret to roasted and muddy squid? Always use aromatic thyme. Chili combines greatly with sticky quinoa.
							Nachos can be enameled with warm strudel, also try covering the salad with honey.
							Mash up each side of the chicken lard with one cup of pickles.
							To the soaked cabbage add meatloaf, rhubarb, triple sec and bitter leek.
							To the thin peanut butter add meatballs, escargot, champaign and heated cauliflower.
						</p>
					</div>
				</div>
			</div>
		</div>
		<div id="VideoAndNutrition" class="bgGreen1" style="clip-path: polygon(2% 0%, 98% 0%, 98.5% 20%, 97% 60%, 97% 85%, 98% 100%, 2% 100%, 3% 60%, 1.5% 20%);">
			<div class="container py-5 text-center">
				<div class="row">
					<div class="col-sm-4 text-sm-right">
						<h2 class="fgGreen1 w-100" style="border-bottom: dashed 2px #327317;">{{ $t('Execution from us') }}</h2>
					</div>
					<div class="col-sm-8">
						<div class="embed-responsive embed-responsive-16by9">
							<iframe class="embed-responsive-item" src="https://www.youtube.com/embed/LRYdGgH9YQk" allowfullscreen></iframe>
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
	import NutritionStats from './NutritionStats';

	export default {
		name: 'RecipeView',
		components: {
			RecommendedRecipes,
			NutritionStats
		},
		data: function () {
			return {
				id: 0,
				article: {}
			};
		},
		methods: {
			getArticleData: function () {
				this.$http.get('/api/articleContentTranslation/' + this.id + '/')
					.then((response) => {
						this.article = response.data;
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
		}
	};
</script>

<style scoped>

</style>
