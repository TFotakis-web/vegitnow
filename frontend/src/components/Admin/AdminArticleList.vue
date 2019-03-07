<template>
	<div class="d-flex flex-grow-1">
		<Loader v-if="requestsUnsatisfied"/>
		<div id="AdminArticleList" v-if="!requestsUnsatisfied" class="flex-grow-1 container">
			<div class="row">
				<ArticleCard v-for="(article, index) in articleList" :key="index" :article="article"></ArticleCard>
			</div>
		</div>
	</div>
</template>

<script>
	import ArticleCard from './AdminArticleCard';
	import Loader from '../Structure/Loader';

	export default {
		name: 'AdminArticleList',
		components: {
			ArticleCard,
			Loader
		},
		data: function () {
			return {
				articleList: [],
				requestsUnsatisfied: 0
			};
		},
		mounted: function () {
			this.getArticles();
		},
		methods: {
			getArticles: function () {
				this.requestsUnsatisfied++;
				this.$http.get('/api/article/?type=2&carousel')
					.then((response) => {
						this.articleList = response.data;
						this.requestsUnsatisfied--;
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

</style>
