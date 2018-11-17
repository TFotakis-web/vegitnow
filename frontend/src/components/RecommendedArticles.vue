<template>
	<div>
		<div id="ArticlesDualCard" class="d-none d-lg-block" style="position: relative;">
			<a class="btn btn-circle bgGreen2 text-white" href="#articleCarouselDualCard" role="button" data-slide="prev" style="
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
			<a class="hidden btn btn-circle bgGreen2 text-white" href="#articleCarouselDualCard" role="button" data-slide="next" style="
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
			<h1 class="text-center fgGreen0" style="position: relative;top: -0.5em;margin-bottom: -1.2em;z-index: 1;">Articles</h1>
			<div class="bgGreen3 py-5" style="clip-path: polygon(5% 0%, 98% 0%, 97% 20%, 98% 70%, 96% 90%, 97.5% 95%, 98% 100%, 2% 100%, 3% 95%, 2% 80%, 2% 70%, 3% 20%, 2% 0%);">
				<div id="articleCarouselDualCard" class="carousel slide" data-ride="carousel">
					<div class="carousel-inner">
						<div v-for="(articlesPart, index) in dualArticles" class="carousel-item" :class="{ 'active': index === 0 }">
							<div class="container">
								<div class="row">
									<ArticleCard v-for="(article, index2) in articlesPart" :key="'dualArticleCard' + article.id" :article="article" :isLeft="index2 === 0"></ArticleCard>
									<!--{% include 'Shared/articleCard.html' with isLeft=True %}-->
									<!--{% include 'Shared/articleCard.html' %}-->
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>

		<div id="ArticlesSingleCard" class="d-lg-none" style="position: relative;">
			<a class="btn btn-circle bgGreen2 text-white" href="#articleCarouselSingleCard" role="button" data-slide="prev" style="
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
			<a class="hidden btn btn-circle bgGreen2 text-white" href="#articleCarouselSingleCard" role="button" data-slide="next" style="
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
			<h1 class="text-center fgGreen0" style="position: relative;top: -0.5em;margin-bottom: -1.2em;z-index: 1;">Articles</h1>
			<div class="bgGreen3 py-5" style="clip-path: polygon(5% 0%, 98% 0%, 97% 20%, 98% 70%, 96% 90%, 97.5% 95%, 98% 100%, 2% 100%, 3% 95%, 2% 80%, 2% 70%, 3% 20%, 2% 0%);">
				<div id="articleCarouselSingleCard" class="carousel slide" data-ride="carousel">
					<div class="carousel-inner">
						<div v-for="(article, index) in articles" class="carousel-item" :class="{ 'active': index === 0 }">
							<div class="container">
								<div class="row">
									<ArticleCard :article="article"></ArticleCard>
									<!--{% include 'Shared/articleCard.html' %}-->
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
	import ArticleCard from './ArticleCard'

	export default {
		name: 'RecommendedArticles',
		components: {
			ArticleCard
		},
		data: function () {
			return {
				articleList: [],
				articleContentTranslation: [],
				articleTypeAssociation: []
			}
		},
		methods: {
			getArticles: function () {
				this.$http.get('/api/article/')
					.then((response) => {
						this.articleList = response.data
					})
					.catch((err) => {
						console.log(err)
					})
			},
			getArticleContentTranslation: function () {
				this.$http.get('/api/articleContentTranslation/')
					.then((response) => {
						this.articleContentTranslation = response.data
					})
					.catch((err) => {
						console.log(err)
					})
			},
			getArticleTypeAssociation: function () {
				this.$http.get('/api/articleTypeAssociation/')
					.then((response) => {
						this.articleTypeAssociation = response.data
					})
					.catch((err) => {
						console.log(err)
					})
			}
		},
		mounted: function () {
			this.getArticles();
			this.getArticleContentTranslation();
			this.getArticleTypeAssociation()
		},
		computed: {
			articles: function () {
				var arr = [];
				for (var article in this.articleList) {
					var isArticle = false;
					for (var ata in this.articleTypeAssociation) {
						if (this.articleTypeAssociation[ata].Article === this.articleList[article].id) {
							isArticle = this.articleTypeAssociation[ata].Type === 2;
							break
						}
					}
					if (!isArticle) continue;
					for (var act in this.articleContentTranslation) {
						if (this.articleContentTranslation[act].Article === this.articleList[article].id) {
							arr.push(this.articleContentTranslation[act]);
							break
						}
					}
				}
				return arr
			},
			dualArticles: function () {
				var arr = [];
				for (var index = 0; index < this.articles.length; index += 2) {
					var tmp = [];
					tmp.push(this.articles[index]);
					if (this.articles.length > index + 1) tmp.push(this.articles[index + 1]);
					arr.push(tmp)
				}
				return arr
			}
		}
	}
</script>

<style scoped>

</style>
