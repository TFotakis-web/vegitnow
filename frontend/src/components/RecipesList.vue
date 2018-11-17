<template>
	<div>
		<div class="navbar-placeholder"></div>
		<div class="container">
			<h1>Recipes</h1>
			<div class="row">
				<RecipeCard v-for="recipe in recipes" :key="recipe.id" :recipe="recipe"></RecipeCard>
			</div>
		</div>
	</div>
</template>

<script>
	import RecipeCard from './RecipeCard';

	export default {
		name: 'RecipesList',
		components: {
			RecipeCard
		},
		data: function () {
			return {
				articleList: [],
				articleContentTranslation: [],
				articleTypeAssociation: []
			};
		},
		methods: {
			getArticles: function () {
				this.$http.get('/api/article/')
					.then((response) => {
						this.articleList = response.data;
					})
					.catch((err) => {
						console.log(err);
					});
			},
			getArticleContentTranslation: function () {
				this.$http.get('/api/articleContentTranslation/')
					.then((response) => {
						this.articleContentTranslation = response.data;
					})
					.catch((err) => {
						console.log(err);
					});
			},
			getArticleTypeAssociation: function () {
				this.$http.get('/api/articleTypeAssociation/')
					.then((response) => {
						this.articleTypeAssociation = response.data;
					})
					.catch((err) => {
						console.log(err);
					});
			}
		},
		mounted: function () {
			this.getArticles();
			this.getArticleContentTranslation();
			this.getArticleTypeAssociation();
		},
		computed: {
			recipes: function () {
				var arr = [];
				for (var article in this.articleList) {
					var isRecipe = false;
					for (var ata in this.articleTypeAssociation) {
						if (this.articleTypeAssociation[ata].Article === this.articleList[article].id) {
							isRecipe = this.articleTypeAssociation[ata].Type === 1;
							break;
						}
					}
					if (!isRecipe) continue;
					for (var act in this.articleContentTranslation) {
						if (this.articleContentTranslation[act].Article === this.articleList[article].id) {
							arr.push(this.articleContentTranslation[act]);
							break;
						}
					}
				}
				return arr;
			}
		}
	};
</script>

<style scoped>

</style>
