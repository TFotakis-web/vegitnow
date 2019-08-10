<template>
	<div class="d-flex flex-grow-1 mb-5">
		<Loader v-if="requestsUnsatisfied"/>
		<div v-if="!requestsUnsatisfied" class="flex-grow-1 mt-3">
			<div class="container">
				<div class="row">
					<template v-for="(item, index) in pageItems">
						<template v-if="item.hasOwnProperty('article')">
							<ArticleCard :article="item['article']" :key="'article' + item['article'].id"/>
						</template>
						<template v-if="item.hasOwnProperty('ad')">
							<AdCard :ad="item['ad']" :key="'ad' + item['ad']['id'] + '-' + index"/>
						</template>
					</template>
				</div>
				<Pagination :items="items" :itemsPerPage="6"/>
			</div>
		</div>
	</div>
</template>

<script>
	import ArticleCard from './ArticleCard';
	import Loader from '../Structure/Loader';
	import AdCard from '../Structure/Ads/AdCard';
	import Pagination from '../Structure/Pagination';

	export default {
		name: 'ArticlesList',
		components: {
			ArticleCard,
			Loader,
			AdCard,
			Pagination
		},
		data: function () {
			return {
				articleList: [],
				ads: [],
				requestsUnsatisfied: 0,
				items: [],
				pageItems: []
			};
		},
		mounted: function () {
			this.getArticles();
			this.getAds();
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
			},
			getAds: function () {
				this.requestsUnsatisfied++;
				this.$http.get('/api/vegitnowad/?locale=' + this.$cookie.get('locale') + '&type=INSIDE_POST')
					.then(response => {
						this.ads = response.data;
						this.requestsUnsatisfied--;
					})
					.catch(err => {
						this.requestsUnsatisfied--;
						this.$root.notifyAction.error(err);
					});
			}
		},
		watch: {
			requestsUnsatisfied: function () {
				if (this.requestsUnsatisfied) return;
				this.items = this.$root.combineArticlesWithAds(this.articleList, this.ads);
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
