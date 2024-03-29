<template>
	<div id="recipesList" class="d-flex flex-grow-1 mb-5">
		<Loader v-if="requestsUnsatisfied"/>
		<div v-if="!requestsUnsatisfied" class="flex-grow-1 mt-3">
			<div class="container">
				<div class="row mb-3">
					<template v-for="(item, index) in pageItems">
						<template v-if="item.hasOwnProperty('article')">
							<RecipeCard :recipe="item['article']" :key="'article' + item['article'].id"/>
						</template>
						<template v-if="item.hasOwnProperty('ad')">
							<AdCard :ad="item['ad']" :key="'ad' + item['ad']['id'] + '-' + index" :listType="'recipes'"/>
						</template>
					</template>
				</div>
				<Pagination :items="items" :itemsPerPage="9"/>
			</div>
		</div>
	</div>
</template>

<script>
	import RecipeCard from './RecipeCard';
	import Loader from '../Structure/Loader';
	import AdCard from '../Structure/Ads/AdCard';
	import Pagination from '../Structure/Pagination';

	export default {
		name: 'RecipesList',
		components: {
			RecipeCard,
			Loader,
			AdCard,
			Pagination
		},
		data: function () {
			return {
				recipeList: [],
				ads: [],
				requestsUnsatisfied: 0,
				items: [],
				pageItems: [],
				routeQuery: this.$route.query
			};
		},
		mounted: function () {
			this.getRecipes();
			this.getAds();
		},
		methods: {
			getRecipes: function () {
				this.requestsUnsatisfied++;
				let requestUrl = '/api/article/?locale=' + this.$cookie.get('locale') + '&type=1';
				if ('ingredients' in this.$route.query)
					requestUrl += '&ingredients=' + this.$route.query['ingredients'];
				this.$http.get(requestUrl)
					.then(response => {
						this.recipeList = response.data;
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
				this.items = this.$root.combineArticlesWithAds(this.recipeList, this.ads);
			},
			$route: function (to, from) {
				if (JSON.stringify(to.query) === JSON.stringify(from.query))
					return;
				this.getRecipes();
			}
		},
		head: {
			title: function () {
				return {
					inner: this.$t('Recipes')
				};
			},
			meta: function () {
				return this.$root.headData.updateMeta({
					// GeneralDescription: '',
					// GeneralKeywords: '',
					GooglePlusName: this.$t('Recipes'),
					// GooglePlusDescription: '',
					// GooglePlusImage: '',
					// TwitterCard: '',
					// TwitterSite: '',
					TwitterTitle: this.$t('Recipes'),
					// TwitterDescription: '',
					// TwitterCreator: '',
					// TwitterImage: '',
					OpenGraphTitle: this.$t('Recipes'),
					OpenGraphType: 'article',
					OpenGraphUrl: location.href,
					// OpenGraphImage: '',
					// OpenGraphDescription: '',
					// OpenGraphSiteName: '',
					// OpenGraphPublishedTime: '',
					// OpenGraphModifiedTime: '',
					// OpenGraphSection: '',
					// OpenGraphTag: '',
					// OpenGraphAdmins: ''
				});
			}
		}
	};
</script>

<style scoped>
	#recipesList {
		--card-title-shadow: var(--v-gray2);
	}
</style>
