<template>
	<div class="d-flex flex-grow-1">
		<Loader v-if="requestsUnsatisfied"/>
		<div id="AdminArticleList" v-if="!requestsUnsatisfied" class="flex-grow-1 container">
			<div class="row">
				<ArticleCard v-for="(article, index) in articleList" :key="index" :article="article"/>
			</div>
		</div>
		<AdminArticleModal :articleId="editArticleId"/>
	</div>
</template>

<script>
	import ArticleCard from './AdminArticleCard';
	import Loader from '../Structure/Loader';
	import AdminArticleModal from './AdminArticleModal';

	export default {
		name: 'AdminArticleList',
		components: {
			ArticleCard,
			Loader,
			AdminArticleModal
		},
		data: function () {
			return {
				articleList: [],
				requestsUnsatisfied: 0,
				editArticleId: null
			};
		},
		mounted: function () {
			this.getArticles();
		},
		methods: {
			getArticles: function () {
				this.requestsUnsatisfied++;
				this.$http.get('/api/article/?type=2')
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
			},

			removeTranslation: function () {

			},
			saveTranslation: function () {

			}
		}
	};
</script>

<style scoped>

</style>
