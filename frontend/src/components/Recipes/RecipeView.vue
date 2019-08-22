<template>
	<div id="recipeView" class="d-flex flex-grow-1">
		<Loader v-if="requestsUnsatisfied"/>
		<div v-if="!requestsUnsatisfied" class="flex-grow-1">
			<div id="RecipeImageAndStats" class="d-flex flex-column box-clip-path1 h-100-minus-navbar">
				<div class="full-box-img flex-grow-1 d-flex flex-column justify-content-end" :style="{ 'background-image': 'url(' + article.Thumbnail + ')' }">
					<div class="container">
						<h1 class="text-white w-100 text-center text-lg-left mb-4" style="text-shadow: black 0 0 20px;">{{ article.Title }}</h1>
					</div>
				</div>
				<div class="bgGreen1">
					<div class="container">
						<div class="row text-center text-md-left py-4">
							<div class="col-sm-6 col-md-3">
								<h2 class="fgGreen1">{{ $t('Ready in') }}:</h2>
								<p class="mb-sm-0 d-inline-block">
									<span class="float-left mr-2 v-icon v-icon-clock fgGreen1-as-bg" style="height: 3rem; width: 3rem;"></span>
									<span class="float-right text-left">{{ $t('Cooking') }}: {{ article.Cooking }}'<br>{{ $t('Preparation') }}: {{ article.Preparation }}'</span>
								</p>
							</div>
							<div class="col-sm-6 col-md-3 v-border-left-md">
								<h2 class="fgGreen1">{{ $t('Waiting') }}:</h2>
								<p class="mb-sm-0 d-inline-block">
									<span class="mr-2 v-icon v-icon-clock fgGreen1-as-bg" style="height: 3rem; width: 3rem;"></span>
									<span class="text-left">
										<span v-if="Math.floor(article.Waiting / 60)">{{ Math.floor(article.Waiting / 60) }}{{ $t("h")}}</span>
										<span v-if="Math.floor(article.Waiting / 60) === 0 || article.Waiting % 60">{{ article.Waiting % 60 }}'</span>
									</span>
								</p>
							</div>
							<div class="col-sm-6 col-md-3 v-border-left-md">
								<h2 class="fgGreen1">{{ $t('Main Ingredients') }}:</h2>
								<p class="mb-sm-0 d-inline-block">
									<span class="float-left mr-2 v-icon v-icon-ingredients fgGreen1-as-bg" style="height: 3rem; width: 3rem;"></span>
									<span class="text-left"><template v-for="(ingredient, index) in articleMainIngredients">{{ ingredient.Name }}<template v-if="index !== articleMainIngredients.length - 1"> - </template></template></span>
								</p>
							</div>
							<div class="col-sm-6 col-md-3 v-border-left-md">
								<h2 class="fgGreen1">{{ $t('Dishes') }}:</h2>
								<p class="mb-sm-0 d-inline-block">
									<span class="mr-2 v-icon v-icon-portions fgGreen1-as-bg" style="height: 3rem; width: 4.5rem;"></span>
									<span class="text-left">{{ article.Dishes }}</span>
								</p>
							</div>
						</div>
					</div>
				</div>
			</div>
			<div id="Instructions">
				<div class="container">
					<div class="row py-5">
						<div class="col-md-4 text-center text-md-left">
							<h2 class="fgGreen1">{{ $t('Ingredients') }}</h2>
							<p v-for="ingredient in article.Ingredients">
								<span>{{ ingredient.Quantity }}gr </span>
								<router-link class="fgGreen1" :to="{ name: 'IngredientView', params: { id: ingredient.id }, query: { title: $root.toGreeklish(ingredient.Name).replace(/ /g, '-') } }">
									{{ ingredient.Name }}
								</router-link>
							</p>
						</div>
						<div class="col-md-8 v-border-left-md">
							<h2 class="fgGreen1 text-center text-md-left">{{ $t('Execution') }}</h2>
							<div class="htmlRenderer" v-html="article.Content"></div>
						</div>
					</div>
				</div>
			</div>
			<div id="VideoAndNutrition" class="bgGreen1 box-clip-path3" style="border-top: 7rem solid var(--v-gray2);">
				<!--			<div id="VideoAndNutrition" v-if="article.YoutubeLink !== ''" class="bgGreen1 box-clip-path3" style="border-top: 7rem solid var(&#45;&#45;v-gray2);">-->
				<div class="container pb-5 text-center">
					<div class="row position-relative" v-if="article.YoutubeLink !== ''">
						<div class="col-md-4 position-relative bgGreen1">
							<span class="v-icon v-icon-pot bgGreen3 pot-position d-block"></span>
						</div>
					</div>
					<div class="row position-relative" v-if="article.YoutubeLink !== ''">
						<div class="col-md-4 position-relative bgGreen1 pr-0">
							<span class="v-icon v-icon-video bgGreen3 d-block mx-auto mb-3" style="height: 4.45rem; width: 5.25rem; margin-top: -2.2rem"></span>
							<h2 class="fgGreen1 w-100" style="border-bottom: dashed 2px var(--v-green6);">{{ $t('Execution from us') }}</h2>
						</div>
						<div class="col-md-8 pl-0">
							<div class="embed-responsive embed-responsive-16by9 video-position">
								<iframe class="embed-responsive-item" :src="article.YoutubeLink" allowfullscreen></iframe>
							</div>
						</div>
					</div>
					<div class="row mt-5">
						<div class="col-md-4 text-md-right my-auto">
							<h2 class="fgGreen1 w-100 v-border-bottom v-border-bottom-md-0">{{ $t('Nutrition facts') }}:</h2>
						</div>
						<div class="col-md-7 col-lg-5 align-left float-left text-left">
							<NutritionStats class="text-center text-md-left" :ingredient-list="article.Ingredients" :dishes="article.Dishes"/>
						</div>
						<div class="col-lg-3 v-border-left-lg my-lg-auto mt-5">
							<h2 class="fgGreen1 v-border-bottom v-border-bottom-lg-0">{{ $t('Share this recipe') }}</h2>
							<social-sharing :key="$router.fullPath" :url="$router.fullPath" :title="article.Title" hashtags="VegItNow" twitter-user="vegitnow" inline-template>
								<div class="fgGreen1 v-network-tags">
									<network network="facebook">
										<i class="icon-facebook"></i>
									</network>
									<network network="twitter">
										<i class="icon-twitter"></i>
									</network>
									<network network="pinterest">
										<i class="icon-pinterest"></i>
									</network>
									<network network="email">
										<i class="icon-mail"></i>
									</network>
								</div>
							</social-sharing>
						</div>
					</div>
				</div>
			</div>
			<RecommendedRecipes :current-recipe-id="id"/>
		</div>
	</div>
</template>

<script>
	import RecommendedRecipes from './RecommendedRecipes';
	import NutritionStats from '../Structure/NutritionStats';
	import Loader from '../Structure/Loader';

	export default {
		name: 'RecipeView',
		components: {
			RecommendedRecipes,
			NutritionStats,
			Loader
		},
		data: function () {
			return {
				id: this.$route.params['id'].toString(),
				article: {},
				requestsUnsatisfied: 0
			};
		},
		mounted: function () {
			this.getRecipeData();
		},
		methods: {
			getRecipeData: function () {
				this.requestsUnsatisfied++;
				this.$http.get('/api/article/' + this.id + '/?locale=' + this.$cookie.get('locale'))
					.then(response => {
						this.article = response.data;
						this.$emit('updateHead');
						this.requestsUnsatisfied--;
						this.$router.push('?title=' + this.$root.toGreeklish(this.article.Title).replace(/ /g, '-'));
					})
					.catch(this.$root.notifyAction.error);
			}
		},
		computed: {
			articleMainIngredients: function () {
				if (!this.article.hasOwnProperty('Ingredients')) return [];
				return this.article.Ingredients.filter(function (ingredient) {
					return ingredient.IsMainIngredient;
				});
			}
		},
		head: {
			title: function () {
				return this.article.Title ? {inner: this.article.Title} : '';
			},
			meta: function () {
				return this.$root.headData.updateMeta({
					GeneralDescription: this.article.Preview,
					// GeneralKeywords: '',
					GooglePlusName: this.article.Title,
					GooglePlusDescription: this.article.Preview,
					GooglePlusImage: location.origin + this.article.Thumbnail,
					// TwitterCard: '',
					// TwitterSite: '',
					TwitterTitle: this.article.Title,
					TwitterDescription: this.article.Preview,
					TwitterCreator: this.article.AuthorName || '',
					TwitterImage: location.origin + this.article.Thumbnail,
					OpenGraphTitle: this.article.Title,
					OpenGraphType: 'article',
					OpenGraphUrl: location.href,
					OpenGraphImage: location.origin + this.article.Thumbnail,
					OpenGraphDescription: this.article.Preview
					// ,
					// OpenGraphSiteName: '',
					// OpenGraphPublishedTime: '',
					// OpenGraphModifiedTime: '',
					// OpenGraphSection: '',
					// OpenGraphTag: '',
					// OpenGraphAdmins: ''
				});
			}
		}
	};
</script>

<style scoped>
	@media (min-width: 768px) {
		.video-position {
			margin-top: -4rem;
		}
	}

	.pot-position {
		height: 8rem;
		width: 12rem;
		position: absolute;
		top: -6.4rem;
		left: 50%;
		display: block;
		transform: translateX(-50%);
	}
</style>

<style>
	.v-network-tags > span {
		font-size: 2rem;
		cursor: pointer
	}

	.v-network-tags > span:hover {
		color: var(--v-green2);
	}
</style>
