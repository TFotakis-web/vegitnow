<template>
	<div id="carousel" v-if="articleList.length" style="position: relative;">
		<a class="btn btn-circle bgGreen2 text-white" href="#carouselControls" role="button" data-slide="prev"
		   style=" font-size: 1.5rem; font-family: 'AC-ScriptCondenced_unicode', sans-serif; position: absolute; top: 50vh; left: 1%; z-index: 1029; margin-top: -22.5px">
			<span aria-hidden="true"><</span>
			<span class="sr-only">Previous</span>
		</a>
		<a class="btn btn-circle bgGreen2 text-white" href="#carouselControls" role="button" data-slide="next"
		   style=" font-size: 1.5rem; font-family: 'AC-ScriptCondenced_unicode', sans-serif; position: absolute; top: 50vh; right: 1%; z-index: 1029; margin-top: -22.5px">
			<span aria-hidden="true">></span>
			<span class="sr-only">Next</span>
		</a>
		<div class="h-100-minus-navbar box-clip-path1">
			<div id="carouselControls" class="carousel slide" data-ride="not-carousel">
				<div class="carousel-inner">
					<div v-for="(article, index) in articleList" :key="article.id" class="carousel-item" :class="{ 'active' : index === 0 }">
						<div class="full-screen-img">
							<div class="full-screen-img" :style="{'background-image': 'url(' + article.Thumbnail + ')'}">
								<div class="container-fluid h-100">
									<div class="row h-100">
										<div class="col-md-6 h-100 bgGreenTrans0 bg-blur text-white text-center">
											<div class="d-table h-50 w-100">
												<div class="d-table-cell align-bottom">
													<div class="container w-75 mb-5">
														<h1 class="d-none d-lg-block">{{ article.Title }}</h1>
														<h2 class="d-inline d-lg-none ">{{ article.Title }}</h2>
													</div>
												</div>
											</div>
											<div class="h-50" style="border-top: dashed 2px var(--v-green2);">
												<div v-if="article.ArticleTypeId === 1" class="container w-75">
													<div class="row text-center">
														<div class="col-lg-6 carousel-border-right">
															<span class="v-icon v-icon-ingredients bg-white mr-2 mt-5"></span>
															<h2 class="d-none d-lg-inline mt-5">{{ $t('Main Ingredients') }}:</h2>
															<h4 class="d-inline d-lg-none mt-5">{{ $t('Main Ingredients') }}:</h4>
															<p class="d-none d-lg-block">{{ article.MainIngredients }}</p>
															<p class="d-inline d-lg-none">{{ article.MainIngredients }}</p>
														</div>
														<div class="col-lg-6">
															<span class="v-icon v-icon-clock bg-white d-lg-none mr-2 mt-lg-5"></span>
															<h2 class="d-none d-lg-block mt-lg-5">{{ $t('Ready in') }}:</h2>
															<h4 class="d-inline d-lg-none mt-lg-5">{{ $t('Ready in') }}:</h4>
															<span class="v-icon v-icon-clock bg-white d-none d-lg-inline-block mr-2"></span>
															<p class="d-none d-lg-inline-block">{{ article.Cooking + article.Preparation }}'</p>
															<p class="d-inline d-lg-none">{{ article.Cooking + article.Preparation }}'</p>
														</div>
														<router-link
															:to="{ name: 'RecipeView', params: { id: article.id }, query : { title: $root.toGreeklish(article.Title).replace(/ /g, '-') }}"
															class="btn bgGreen0 text-white text-uppercase px-4 font-weight-bold mt-5 mx-auto"
															style="border-radius: 2rem;">{{ $t('Go to the recipe') }}
														</router-link>
													</div>
												</div>
												<div v-if="article.ArticleTypeId === 2" class="container w-75 mt-5">
													<p>{{ article.Preview }}</p>
													<router-link
														:to="{ name: 'ArticleView', params: { id: article.id }, query : { title: $root.toGreeklish(article.Title).replace(/ /g, '-') }}"
														class="btn bgGreen0 text-white text-uppercase px-4 font-weight-bold mt-5"
														style="border-radius: 2rem;">{{ $t('Read more') }}
													</router-link>
												</div>
											</div>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	export default {
		name: 'Carousel',
		data: function () {
			return {
				articleList: []
			};
		},
		mounted: function () {
			this.getArticles();
		},
		methods: {
			getArticles: function () {
				this.$http.get('/api/article/?locale=' + this.$cookie.get('locale') + '&carousel')
					.then(response => { this.articleList = response.data; })
					.catch(this.$root.notifyAction.error);
			}
		}
	};
</script>

<style scoped>
	@media (min-width: 576px) {
		.carousel-title {
			font-size: 4rem;
		}
	}

	@media (min-width: 992px) {
		.carousel-border-right {
			border-right: dashed 2px var(--v-green2);
		}
	}
</style>
