<template>
	<div class="col-12 col-md-6 col-xl-4 py-2">
		<router-link class="v-link-no-underline v-underline-card-title" :to="routerUrl" style="color: inherit; ">
			<div class="card border-0 bg-transparent">
				<div class="card-body position-relative">
					<div class="full-screen-img position-absolute mt-3" style="height: 160px; width:160px; right: 0; z-index:1" :style="{ 'background-image': 'url(' + recipe.Thumbnail + ')' }"></div>
					<div style="position: relative; z-index: 2">
						<h3 class="v-card-title v-card-title-shadow">{{ recipe.Title }}</h3>
						<span class="v-icon v-icon-card-line fgGreen1-as-bg position-relative d-block mb-3" style="height: 1.5rem; width: 18rem; z-index: 10"></span>
						<span class="v-icon v-icon-ingredients fgGreen1-as-bg mr-2 float-left"></span>
						<h5 class="fgGreen1 m-0">{{ $t('Main Ingredients') }}:</h5>
						<p style="font-size: 0.7em;">{{ recipe.MainIngredients }}</p>

						<table style="height: 2rem">
							<tbody>
							<tr>
								<td class="align-middle">
									<span class="v-icon v-icon-clock fgGreen1-as-bg mr-2 float-left"></span>
								</td>
								<td class="align-middle">
									<h5 class="fgGreen1 d-inline">{{ $t('Ready in') }}:</h5>
									<span style="font-size: 0.7em;">{{ recipe.Cooking + recipe.Preparation }}'</span>
								</td>
							</tr>
							</tbody>
						</table>

					</div>
				</div>
			</div>
		</router-link>
	</div>
</template>

<script>
	export default {
		name: 'RecipeCard',
		props: [
			'recipe',
		],
		data: function () {
			return {
				routerUrl: {
					name: 'RecipeView',
					params: {
						id: this.recipe.id
					},
					query: {
						title: this.$root.toGreeklish(this.recipe.Title).replace(/ /g, '-')
					}
				}
			};
		}
	};
</script>

<style scoped>

</style>
