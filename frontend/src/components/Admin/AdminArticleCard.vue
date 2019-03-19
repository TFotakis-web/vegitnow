<template>
	<div class="col-12 col-lg-6 mb-3" :class="{'article-card-bordered': isLeft }">
		<div class="row">
			<div class="col-6">
				<h4>{{ article.Title }}</h4>
				<hr class="fgGreen1" style="border-top: dashed 2px;">
				<p style="font-size: 0.8em;">{{ article.Preview }}</p>
			</div>
			<div class="col-6 d-table">
				<div class="d-table-cell align-middle">
					<div class="full-screen-img" style="height: 160px;" :style="{ 'background-image': 'url(' + article.Thumbnail + ')' }"></div>
				</div>
			</div>
		</div>
		<div class="row py-4">
			<router-link :to="{ name: 'ArticleView', params: { id: article.id }}" class="btn px-4 bgGreen0 text-white text-uppercase font-weight-bold mx-auto" style="border-radius: 2rem;">{{ $t('Read more') }}</router-link>
			<router-link :to="{ name: 'ArticleView', params: { id: article.id }}" class="btn px-4 bg-info text-white text-uppercase font-weight-bold mx-auto" style="border-radius: 2rem;">{{ $t('Edit') }}</router-link>
			<button @click="deleteArticle()" class="btn px-4 bg-danger text-white text-uppercase font-weight-bold mx-auto" style="border-radius: 2rem;">{{ $t('Delete') }}</button>
		</div>
	</div>
</template>

<script>
	export default {
		name: 'AdminArticleCard',
		props: [
			'article',
			'isLeft'
		],
		methods: {
			deleteArticle: function () {
				this.$http.delete('/api/article/' + this.article['ArticleContentTranslationId'] + '/')
					.then((response) => {
						this.$parent.getArticles();
					})
					.catch((err) => {
						console.log(err);
						this.$notify({
							text: this.$t('Something went wrong... Please check your connection.'),
							type: 'error'
						});
					});
			}
		}
	};
</script>

<style scoped>
	.article-card-bordered {
		border-right: dashed 2px #327317;
	}
</style>
