<template>
	<div id="carousel" v-if="articleList.length" style="position: relative">
		<a class="btn btn-circle bgGreen2 text-white" href="#carouselControls" role="button" data-slide="prev" style="
				   font-size: 1.5rem;
				   font-family: 'AC-ScriptCondenced_unicode', sans-serif;
				   position: absolute;
				   top: 50%;
				   left: 1%;
				   z-index: 1029;
				   ">
			<span aria-hidden="true"><</span>
			<span class="sr-only">Previous</span>
		</a>
		<a class="btn btn-circle bgGreen2 text-white" href="#carouselControls" role="button" data-slide="next" style="
				   font-size: 1.5rem;
				   font-family: 'AC-ScriptCondenced_unicode', sans-serif;
				   position: absolute;
				   top: 50%;
				   right: 1%;
				   z-index: 1029;
				   ">
			<span aria-hidden="true">></span>
			<span class="sr-only">Next</span>
		</a>
		<div style="height:100vh;clip-path: polygon(2% 0%, 98% 0%, 97% 20%, 98% 70%, 96% 90%, 97.5% 95%, 98% 100%, 2% 100%, 3% 95%, 2% 80%, 2% 70%, 3% 20%);">
			<div id="carouselControls" class="carousel slide" data-ride="carousel">
				<div class="carousel-inner">
					<div v-for="(article, index) in articleList" :key="article.id" class="carousel-item" :class="{ 'active' : index === 0 }">
						<div class="full-screen-img">
							<div class="full-screen-img" :style="{'background-image': 'url(' + article.Thumbnail + ')'}">
								<div class="container-fluid h-100">
									<div class="row h-100">
										<div class="col-md-6 h-100 bgGreenTrans0 text-white text-center d-table">
											<div class="d-table-cell align-middle">
												<div class="container w-75 mt-5">
													<h1 class="d-none d-lg-block carousel-title">{{ article.Title }}</h1>
													<h2 class="d-inline d-lg-none ">{{ article.Title }}</h2>
												</div>
												<div v-if="article.ArticleTypeId === 1" class="container w-75">
													<div class="row">
<!--														<div class="col-lg-12">-->
														<div class="col-lg-6">
															<h1 class="d-none d-lg-block">{{ $t('Main Ingredients') }}:</h1>
															<h4 class="d-inline d-lg-none">{{ $t('Main Ingredients') }}:</h4>
															<p class="d-none d-lg-block font-weight-bold">{{ article.MainIngredients }}</p>
															<p class="d-inline d-lg-none">{{ article.MainIngredients }}</p>
														</div>
														<div class="col-lg-6">
															<h1 class="d-none d-lg-block">{{ $t('Ready in') }}:</h1>
															<h4 class="d-inline d-lg-none">{{ $t('Ready in') }}:</h4>
															<p class="d-none d-lg-block font-weight-bold">{{ article.ReadyIn }}'</p>
															<p class="d-inline d-lg-none">{{ article.ReadyIn }}'</p>
														</div>
													</div>
													<router-link :to="{ name: 'RecipeView', params: { id: article.id }, query : { title: article.Title.replace(/ /g, '_') }}" class="btn bgGreen0 text-white text-uppercase px-4 font-weight-bold mt-5" style="border-radius: 2rem;">{{ $t('Go to the recipe') }}</router-link>
												</div>
												<div v-if="article.ArticleTypeId === 2" class="container w-75">
													<p>{{ article.Preview }}</p>
													<router-link :to="{ name: 'ArticleView', params: { id: article.id }, query : { title: article.Title.replace(/ /g, '_') }}" class="btn bgGreen0 text-white text-uppercase px-4 font-weight-bold mt-5" style="border-radius: 2rem;">{{ $t('Read more') }}</router-link>
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

</style>
