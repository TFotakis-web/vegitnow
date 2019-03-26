<template>
	<div class="d-flex flex-grow-1">
		<Loader v-if="requestsUnsatisfied"/>
		<div id="AdminRecipeList" v-if="!requestsUnsatisfied" class="flex-grow-1 container">
			<div class="row">
				<RecipeCard v-for="(recipe, index) in recipeList" :key="index" :recipe="recipe"></RecipeCard>
			</div>
		</div>
		<ArticleModal :articleId="editArticleId"/>
	</div>
</template>

<script>
	import RecipeCard from './RecipeCard';
	import Loader from '../Structure/Loader';
	import ArticleModal from './ArticleModal';

	export default {
		name: 'AdminRecipeList',
		components: {
			RecipeCard,
			Loader,
			ArticleModal
		},
		data: function () {
			return {
				recipeList: [],
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
				this.$http.get('/api/article/?type=1')
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
