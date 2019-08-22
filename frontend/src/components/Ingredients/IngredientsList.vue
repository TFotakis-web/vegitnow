<template>
	<div id="ingredientsList" class="d-flex flex-grow-1 mb-5">
		<Loader v-if="requestsUnsatisfied"/>
		<div v-if="!requestsUnsatisfied" class="flex-grow-1 mt-3">
			<div class="container">
				<div class="row mb-5">
					<IngredientCard class="mx-auto mb-3" :ingredient="item" :key="'ingredient' + item.id" v-for="item in pageItems"/>
				</div>
				<Pagination :items="ingredients" :itemsPerPage="6"/>
			</div>
		</div>
	</div>
</template>

<script>
	import IngredientCard from './IngredientCard';
	import Loader from '../Structure/Loader';
	import Pagination from '../Structure/Pagination';

	export default {
		name: 'IngredientsList',
		components: {
			IngredientCard,
			Loader,
			Pagination
		},
		data: function () {
			return {
				requestsUnsatisfied: 0,
				ingredients: [],
				pageItems: []
			};
		},
		mounted: function () {
			this.getIngredients();
		},
		methods: {
			getIngredients: function () {
				this.requestsUnsatisfied++;
				this.$http.get('/api/ingredient/?locale=' + this.$cookie.get('locale'))
					.then(response => {
						this.ingredients = Object.values(response.data).sort((a, b) => (a.Name > b.Name) ? 1 : ((b.Name > a.Name) ? -1 : 0));
						this.requestsUnsatisfied--;
					})
					.catch(this.$root.notifyAction.error);
			}
		},
		head: {
			title: function () {
				return {
					inner: this.$t('Ingredients')
				};
			},
			meta: function () {
				return this.$root.headData.updateMeta({
					// GeneralDescription: '',
					// GeneralKeywords: '',
					GooglePlusName: this.$t('Ingredients'),
					// GooglePlusDescription: '',
					// GooglePlusImage: '',
					// TwitterCard: '',
					// TwitterSite: '',
					TwitterTitle: this.$t('Ingredients'),
					// TwitterDescription: '',
					// TwitterCreator: '',
					// TwitterImage: '',
					OpenGraphTitle: this.$t('Ingredients'),
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

</style>
