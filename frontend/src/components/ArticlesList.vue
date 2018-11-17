<template>
	<div>
		<div class="navbar-placeholder"></div>
		<div class="container">
			<h1>Articles</h1>
			<div class="row">
				<ArticleCard v-for="article in articles" :key="article.id" :article="article"></ArticleCard>
			</div>
		</div>
	</div>
</template>

<script>
	import ArticleCard from './ArticleCard'

	export default {
		name: 'ArticlesList',
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
			}
		}
	}
</script>

<style scoped>

</style>
