<template>
	<div class="d-flex flex-grow-1">
		<Loader v-if="requestsUnsatisfied"/>
		<div v-if="!requestsUnsatisfied" class="flex-grow-1">
			<div class="navbar-placeholder"></div>
			<div class="container">
				<h1>{{ $t('Recipes') }}</h1>
				<div class="row">
					<RecipeCard v-for="recipe in recipes" :key="recipe.id" :recipe="recipe"></RecipeCard>
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
				articleList: [],
				articleContentTranslation: [],
				articleTypeAssociation: [],
				requestsUnsatisfied: 0
			};
		},
		methods: {
			getArticles: function () {
				this.requestsUnsatisfied++;
				this.$http.get('/api/article/')
					.then((response) => {
						this.articleList = response.data;
						this.requestsUnsatisfied--;
					})
					.catch((err) => {
						console.log(err);
					});
			},
			getArticleContentTranslation: function () {
				this.requestsUnsatisfied++;
				this.$http.get('/api/articleContentTranslation/')
					.then((response) => {
						this.articleContentTranslation = response.data;
						this.requestsUnsatisfied--;
					})
					.catch((err) => {
						console.log(err);
					});
			},
			getArticleTypeAssociation: function () {
				this.requestsUnsatisfied++;
				this.$http.get('/api/articleTypeAssociation/')
					.then((response) => {
						this.articleTypeAssociation = response.data;
						this.requestsUnsatisfied--;
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
