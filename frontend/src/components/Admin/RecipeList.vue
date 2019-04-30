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
				this.$http.get('/api/article/?type=1&location=admin')
					.then(response => {
						this.recipeList = response.data;
						this.requestsUnsatisfied--;
					})
					.catch(this.$root.notifyAction.error);
			}
		}
	};
</script>

<style scoped>

</style>
