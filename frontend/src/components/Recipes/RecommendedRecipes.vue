<template>
	<div id="recommendedRecipes" v-if="recipes.length">
		<div id="RecipesTripleCard" class="d-none d-xl-block" style="position: relative;">
			<a class="btn btn-circle bgGreen2 text-white" href="#recipeCarouselTripleCard" role="button" data-slide="prev" style="
				   font-size: 1.5rem;
				   font-family: 'AC-ScriptCondenced_unicode', sans-serif;
				   position: absolute;
				   top: 50%;
				   left: 1%;
				   z-index: 1;
				   ">
				<span aria-hidden="true"><</span>
				<span class="sr-only">Previous</span>
			</a>
			<a class="hidden btn btn-circle bgGreen2 text-white" href="#recipeCarouselTripleCard" role="button" data-slide="next" style="
				   font-size: 1.5rem;
				   font-family: 'AC-ScriptCondenced_unicode', sans-serif;
				   position: absolute;
				   top: 50%;
				   right: 1%;
				   z-index: 1;
				   ">
				<span aria-hidden="true">></span>
				<span class="sr-only">Next</span>
			</a>
			<h1 class="text-center" style="position: relative;top: -0.5em;margin-bottom: -1.2em;z-index: 1;">
				<router-link :to="{ name: 'RecipesList' }" class="fgGreen0 bg-transparent">
					{{ $t('Recipes') }}
				</router-link>
			</h1>
			<div class="bgGreen4 py-5" style="clip-path: polygon(5% 0%, 98% 0%, 97% 20%, 98% 70%, 96% 90%, 97.5% 95%, 98% 100%, 2% 100%, 3% 95%, 2% 80%, 2% 70%, 3% 20%, 2% 0%);">
				<div id="recipeCarouselTripleCard" class="carousel slide" data-ride="carousel">
					<div class="carousel-inner">
						<div v-for="(recipesPart, index) in tripleRecipes" class="carousel-item" :class="{ 'active': index === 0 }">
							<div class="container">
								<div class="row">
									<template v-if="noAdCards">
										<RecipeCard v-for="recipe in recipesPart" :key="'tripleRecipeCard' + recipe.id" :recipe="recipe"/>
									</template>
									<template v-else>
										<template v-for="recipe in recipesPart">
											<template v-if="recipe.hasOwnProperty('article')">
												<RecipeCard :recipe="recipe['article']" :key="'triple-recipe' + recipe['article'].id"/>
											</template>
											<template v-else>
												<AdCard :ad="recipe['ad']" listType="recipes" :key="'triple-ad' + recipe['ad'].id + '-' + index"/>
											</template>
										</template>
									</template>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>

		<div id="RecipesDualCard" class="d-none d-md-block d-xl-none" style="position: relative;">
			<a class="btn btn-circle bgGreen2 text-white" href="#recipeCarouselDualCard" role="button" data-slide="prev" style="
				   font-size: 1.5rem;
				   font-family: 'AC-ScriptCondenced_unicode', sans-serif;
				   position: absolute;
				   top: 50%;
				   left: 1%;
				   z-index: 1;
				   ">
				<span aria-hidden="true"><</span>
				<span class="sr-only">Previous</span>
			</a>
			<a class="hidden btn btn-circle bgGreen2 text-white" href="#recipeCarouselDualCard" role="button" data-slide="next" style="
				   font-size: 1.5rem;
				   font-family: 'AC-ScriptCondenced_unicode', sans-serif;
				   position: absolute;
				   top: 50%;
				   right: 1%;
				   z-index: 1;
				   ">
				<span aria-hidden="true">></span>
				<span class="sr-only">Next</span>
			</a>

			<h1 class="text-center" style="position: relative;top: -0.5em;margin-bottom: -1.2em;z-index: 1;">
				<router-link :to="{ name: 'RecipesList' }" class="fgGreen0 bg-transparent">
					{{ $t('Recipes') }}
				</router-link>
			</h1>
			<div class="bgGreen4 py-5" style="clip-path: polygon(5% 0%, 98% 0%, 97% 20%, 98% 70%, 96% 90%, 97.5% 95%, 98% 100%, 2% 100%, 3% 95%, 2% 80%, 2% 70%, 3% 20%, 2% 0%);">
				<div id="recipeCarouselDualCard" class="carousel slide" data-ride="carousel">
					<div class="carousel-inner">
						<div v-for="(recipesPart, index) in dualRecipes" class="carousel-item" :class="{ 'active': index === 0 }">
							<div class="container">
								<div class="row">
									<template v-if="noAdCards">
										<RecipeCard v-for="recipe in recipesPart" :key="'dualRecipeCard' + recipe.id" :recipe="recipe"/>
									</template>
									<template v-else>
										<template v-for="recipe in recipesPart">
											<template v-if="recipe.hasOwnProperty('article')">
												<RecipeCard :recipe="recipe['article']" :key="'dual-recipe' + recipe['article'].id"/>
											</template>
											<template v-else>
												<AdCard :ad="recipe['ad']" listType="recipes" :key="'dual-ad' + recipe['ad'].id + '-' + index"/>
											</template>
										</template>
									</template>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>

		<div id="RecipesSingleCard" class="d-md-none" style="position: relative;">
			<a class="btn btn-circle bgGreen2 text-white" href="#recipeCarouselSingleCard" role="button" data-slide="prev" style="
				   font-size: 1.5rem;
				   font-family: 'AC-ScriptCondenced_unicode', sans-serif;
				   position: absolute;
				   top: 68%;
				   left: 1%;
				   z-index: 1;
				   ">
				<span aria-hidden="true"><</span>
				<span class="sr-only">Previous</span>
			</a>
			<a class="hidden btn btn-circle bgGreen2 text-white" href="#recipeCarouselSingleCard" role="button" data-slide="next" style="
				   font-size: 1.5rem;
				   font-family: 'AC-ScriptCondenced_unicode', sans-serif;
				   position: absolute;
				   top: 68%;
				   right: 1%;
				   z-index: 1;
				   ">
				<span aria-hidden="true">></span>
				<span class="sr-only">Next</span>
			</a>
			<h1 class="text-center" style="position: relative;top: -0.5em;margin-bottom: -1.2em;z-index: 1;">
				<router-link :to="{ name: 'RecipesList' }" class="fgGreen0 bg-transparent">
					{{ $t('Recipes') }}
				</router-link>
			</h1>
			<div class="bgGreen4 py-5" style="clip-path: polygon(5% 0%, 98% 0%, 97% 20%, 98% 70%, 96% 90%, 97.5% 95%, 98% 100%, 2% 100%, 3% 95%, 2% 80%, 2% 70%, 3% 20%, 2% 0%);">
				<div id="recipeCarouselSingleCard" class="carousel slide" data-ride="carousel">
					<div class="carousel-inner">
						<div v-for="(recipe, index) in recipes" class="carousel-item" :class="{ 'active': index === 0 }">
							<div class="container">
								<div class="row">
									<template v-if="noAdCards">
										<RecipeCard :recipe="recipe" :key="'single-recipe' + recipe.id"/>
									</template>
									<template v-else>
										<template v-if="recipe.hasOwnProperty('article')">
											<RecipeCard :recipe="recipe['article']" :key="'single-recipe' + recipe['article'].id"/>
										</template>
										<template v-else>
											<AdCard :ad="recipe['ad']" listType="recipes" :key="'single-ad' + recipe['ad'].id + '-' + index"/>
										</template>
									</template>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
		<div v-if="location === 'home'" class="bgGreen4" style="clip-path: polygon(5% 0%, 98% 0%, 97% 20%, 98% 70%, 96% 90%, 97.5% 95%, 98% 100%, 2% 100%, 3% 95%, 2% 80%, 2% 70%, 3% 20%, 2% 0%)">
			<Ads AdType="HOME_RECIPES"/>
		</div>
	</div>
</template>

<script>
	import RecipeCard from './RecipeCard';
	import Ads from '../Structure/Ads/HomePage';
	import AdCard from '../Structure/Ads/AdCard';

	export default {
		name: 'RecommendedRecipes',
		components: {
			RecipeCard,
			Ads,
			AdCard
		},
		props: {
			currentRecipeId: String,
			location: String,
			noAdCards: Boolean
		},
		data: function () {
			return {
				recipeList: [],
				ads: []
			};
		},
		mounted: function () {
			this.getArticles();
			this.getAds();
		},
		methods: {
			getArticles: function () {
				this.$http.get('/api/article/?locale=' + this.$cookie.get('locale') + '&type=1&' + this.location)
					.then(response => {
						this.recipeList = response.data;
					})
					.catch(this.$root.notifyAction.error);
			},
			getAds: function () {
				if (this.noAdCards) return;
				this.requestsUnsatisfied++;
				this.$http.get('/api/vegitnowad/?locale=' + this.$cookie.get('locale') + '&type=INSIDE_POST')
					.then(response => {
						this.ads = response.data;
						this.requestsUnsatisfied--;
					})
					.catch(err => {
						this.requestsUnsatisfied--;
						this.$root.notifyAction.error(err);
					});
			}
		},
		computed: {
			recipes: function () {
				if (!this.currentRecipeId) return this.recipeList;
				let id = parseInt(this.currentRecipeId);
				let filteredRecipes = this.recipeList.filter(function (obj) {
					return obj.id !== id;
				});
				return this.$root.combineArticlesWithAds(filteredRecipes, this.ads);
			},
			tripleRecipes: function () {
				let arr = [];
				for (let index = 0; index < this.recipes.length; index += 3) {
					let tmp = [];
					tmp.push(this.recipes[index]);
					if (this.recipes.length > index + 1) tmp.push(this.recipes[index + 1]);
					if (this.recipes.length > index + 2) tmp.push(this.recipes[index + 2]);
					arr.push(tmp);
				}
				return arr;
			},
			dualRecipes: function () {
				let arr = [];
				for (let index = 0; index < this.recipes.length; index += 2) {
					let tmp = [];
					tmp.push(this.recipes[index]);
					if (this.recipes.length > index + 1) tmp.push(this.recipes[index + 1]);
					arr.push(tmp);
				}
				return arr;
			}
		}
	};
</script>

<style scoped>
	#recommendedRecipes {
		--card-title-shadow: var(--v-green4);
	}
</style>
