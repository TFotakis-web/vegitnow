<template>
	<div class="d-flex flex-grow-1">
		<Loader v-if="requestsUnsatisfied"/>
		<div v-if="!requestsUnsatisfied" class="flex-grow-1">
			<div class="navbar-placeholder"></div>
			<div class="container">
				<div class="row">
					<RecipeCard v-for="recipe in recipeList" :key="recipe.id" :recipe="recipe"></RecipeCard>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import RecipeCard from './RecipeCard';
	import Loader from '../Structure/Loader';

	export default {
		name: 'RecipesList',
		components: {
			RecipeCard,
			Loader
		},
		data: function () {
			return {
				recipeList: [],
				requestsUnsatisfied: 0
			};
		},
		mounted: function () {
			this.getRecipes();
		},
		methods: {
			getRecipes: function () {
				this.requestsUnsatisfied++;
				this.$http.get('/api/article/?locale=' + this.$cookie.get('locale') + '&type=1')
					.then((response) => {
						this.recipeList = response.data;
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
