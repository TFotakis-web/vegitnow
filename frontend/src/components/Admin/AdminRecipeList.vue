<template>
	<div class="d-flex flex-grow-1">
		<Loader v-if="requestsUnsatisfied"/>
		<div id="AdminRecipeList" v-if="!requestsUnsatisfied" class="flex-grow-1 container">
			<div class="row">
				<RecipeCard v-for="(recipe, index) in recipeList" :key="index" :recipe="recipe"></RecipeCard>
			</div>
		</div>
	</div>
</template>

<script>
	import RecipeCard from './AdminRecipeCard';
	import Loader from '../Structure/Loader';

	export default {
		name: 'AdminRecipeList',
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
			this.getArticles();
		},
		methods: {
			getArticles: function () {
				this.requestsUnsatisfied++;
				this.$http.get('/api/article/?type=1&carousel')
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
