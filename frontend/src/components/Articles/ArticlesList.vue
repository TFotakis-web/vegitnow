<template>
	<div class="d-flex flex-grow-1">
		<Loader v-if="requestsUnsatisfied"/>
		<div v-if="!requestsUnsatisfied" class="flex-grow-1">
			<div class="navbar-placeholder"></div>
			<div class="container">
				<div class="row">
					<ArticleCard v-for="article in articleList" :key="article.id" :article="article"></ArticleCard>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import ArticleCard from './ArticleCard';
	import Loader from '../Structure/Loader';

	export default {
		name: 'ArticlesList',
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
				this.$http.get('/api/article/?locale=' + this.$cookie.get('locale') + '&type=2')
					.then(response => {
						this.articleList = response.data;
						this.requestsUnsatisfied--;
					})
					.catch(this.$root.notifyAction.error);
			}
		},
		head: {
			title: function () {
				return {
					inner: this.$t('Articles')
				};
			},
			meta: function () {
				return this.$root.headData.defaultMeta();
			}
		}
	};
</script>

<style scoped>

</style>
