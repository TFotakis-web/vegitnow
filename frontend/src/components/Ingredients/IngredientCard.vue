<template>
	<div class="ingredient-card">
		<router-link class="v-link-no-underline v-underline-card-title" :to="routerUrl" style="color: inherit;">
			<div class="card border-0 bg-transparent">
				<div class="card-body">
					<div class="d-inline-block">
						<h3 class="v-card-title v-card-title-shadow">{{ ingredient.Name }}</h3>
						<NutritionStats :ingredient-list="[Object.assign({}, ingredient, {Quantity: 100})]" calories_bg="calories-dark"/>
					</div>
					<div class="d-inline-block ingredient-thumbnail">
						<div class="dashedCircle v-border rotating"></div>
						<div class="ingredientThumbnailCircle">
							<div class="bg-white rounded-circle ingredient-img mx-auto" :style="{ 'background-image': 'url(' + ingredient.Thumbnail + ')' }"></div>
						</div>
					</div>
				</div>
			</div>
		</router-link>
	</div>
</template>

<script>
	import NutritionStats from '../Structure/NutritionStats';

	export default {
		name: 'IngredientCard',
		components: {
			NutritionStats
		},
		props: {
			ingredient: {
				type: Object,
				default: {}
			}
		},
		data: function () {
			return {
				routerUrl: {
					name: 'IngredientView',
					params: {id: this.ingredient.id},
					query: {
						title: this.$root.toGreeklish(this.ingredient.Name).replace(/ /g, '-')
					}
				},
			};
		},
	};
</script>

<style scoped>
	.ingredient-card {
		--v-dashed-circle-size: 140px;
		--v-dashed-circle-padding: 10px;
	}

	.ingredient-img {
		height: calc(var(--v-dashed-circle-size) - 2 * var(--v-dashed-circle-padding));
		width: calc(var(--v-dashed-circle-size) - 2 * var(--v-dashed-circle-padding));
		background-size: cover;
		background-repeat: inherit;
		background-position: center center;
	}

	.ingredientThumbnailCircle {
		margin-top: calc(var(--v-dashed-circle-padding) - var(--v-dashed-circle-size))
	}

	.dashedCircle {
		height: var(--v-dashed-circle-size);
		width: var(--v-dashed-circle-size);
		border-radius: 50%;
		pointer-events: none;
		overflow: hidden;
	}

	.ingredient-thumbnail {
		height: var(--v-dashed-circle-size);
		width: var(--v-dashed-circle-size);
		position: relative;
		z-index: 2;
		top: -50px;
		margin-left: -45px;
	}

	.ingredient-card {
		min-width: max-content;
	}
</style>
