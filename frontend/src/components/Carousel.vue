<template>
	<div id="carousel" style="position: relative">
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
					<div v-for="(article, index) in articles" :key="article.id" class="carousel-item" :class="{ 'active' : index === 0 }">
						<div class="full-screen-img">
							<div class="full-screen-img" :style="{'background-image': 'url(' + article.Thumbnail + ')'}">
								<div class="container-fluid h-100">
									<div class="row h-100">
										<div class="col-md-6 h-100 bgGreenTrans0 text-white text-center d-table">
											<div class="d-table-cell align-middle">
												<div class="container w-75">
													<h1 style="font-size: 4rem;">{{ article.Title }}</h1>
												</div>
												<div class="container w-75">
													<div class="row">
														<div class="col-lg-6">
															<h1>Main Ingredients:</h1>
															<p class="font-weight-bold">{{ article.MainIngredients }}</p>
														</div>
														<div class="col-lg-6">
															<h1>Ready in:</h1>
															<p class="font-weight-bold">{{ article.ReadyIn }}</p>
														</div>
													</div>
													<!--<router-link :to="'/articles/' + article.id + '/'" class="btn bgGreen0 text-white text-uppercase px-4 font-weight-bold mt-5" style="border-radius: 2rem;">Go to recipe</router-link>-->
													<router-link :to="{ name: 'RecipeView', params: { id: article.id }}" class="btn bgGreen0 text-white text-uppercase px-4 font-weight-bold mt-5" style="border-radius: 2rem;">Go to recipe</router-link>
													<!--<a href="{% url 'articles:recipeView' article.Article_id article.Title %}" class="btn bgGreen0 text-white text-uppercase px-4 font-weight-bold mt-5" style="border-radius: 2rem;">{% trans "Go to the Recipe" %}</a>-->
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
				articleList: [],
				articleContentTranslation: []
			};
		},
		methods: {
			getArticles: function () {
				this.$http.get('/api/article/')
					.then((response) => {
						this.articleList = response.data;
					})
					.catch((err) => {
						console.log(err);
					});
			},
			getArticleContentTranslation: function () {
				this.$http.get('/api/articleContentTranslation/')
					.then((response) => {
						this.articleContentTranslation = response.data;
					})
					.catch((err) => {
						console.log(err);
					});
			}
		},
		mounted: function () {
			this.getArticles();
			this.getArticleContentTranslation();
		},
		computed: {
			articles: function () {
				var arr = [];
				for (var article in this.articleList) {
					for (var act in this.articleContentTranslation) {
						if (this.articleContentTranslation[act].Article === this.articleList[article].id) {
							arr.push(this.articleContentTranslation[act]);
							break;
						}
					}
				}
				return arr;
			}
		}
	};
</script>

<style scoped>

</style>
