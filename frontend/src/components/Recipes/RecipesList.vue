<template>
	<div class="d-flex flex-grow-1 mb-5">
		<Loader v-if="requestsUnsatisfied"/>
		<div v-if="!requestsUnsatisfied" class="flex-grow-1">
			<div class="navbar-placeholder"></div>
			<div class="container">
				<div class="row">
					<template v-for="(item, index) in items">
						<template v-if="item.hasOwnProperty('article')">
							<RecipeCard :recipe="item['article']" :key="'article' + item['article'].id"/>
						</template>
						<template v-if="item.hasOwnProperty('ad')">
							<AdCard :ad="item['ad']" :key="'ad' + item['ad']['id'] + '-' + index" :listType="'recipes'"/>
						</template>
					</template>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import RecipeCard from './RecipeCard';
	import Loader from '../Structure/Loader';
	import AdCard from '../Structure/Ads/AdCard';

	export default {
	name: 'RecipesList',
	components: {
		RecipeCard,
		Loader,
		AdCard
	},
	data: function () {
		return {
			recipeList: [],
			ads: [],
			requestsUnsatisfied: 0
		};
	},
	mounted: function () {
		this.getRecipes();
		this.getAds();
	},
	methods: {
		getRecipes: function () {
			this.requestsUnsatisfied++;
			this.$http.get('/api/article/?locale=' + this.$cookie.get('locale') + '&type=1')
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
	computed: {
		items: function () {
			return this.$root.combineArticlesWithAds(this.recipeList, this.ads);
		}
	},
	head: {
		title: function () {
			return {
				inner: this.$t('Recipes')
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
