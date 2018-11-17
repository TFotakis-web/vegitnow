<template>
	<div id="IngredientOfTheDay">
		<h1 class="text-center fgGreen0"
		    style="position: relative;top: -0.5em;margin-bottom: -1.2em;z-index: 1;">Ingredient of the day</h1>
		<div class="bgGreen1 py-5"
		     style="clip-path: polygon(2% 0%, 98% 0%, 97.5% 20%, 96% 45%, 97.5% 60%, 98.5% 80%, 98% 100%, 2% 100%, 1.5% 80%, 1.5% 60%, 2.5% 45%, 1% 20%);">
			<div class="container">
				<div class="row text-center align-items-center">
					<div class="col-lg-4 mb-3 fgGreen0 order-1 order-lg-0">
						<h1>Καρότο</h1>
						<NutritionStats></NutritionStats>
					</div>
					<div class="col-lg-4 mx-auto mb-3 order-0 order-lg-1">
						<div class="bg-white rounded-circle mx-auto"
						     style="
							     height: 190px;
							     width: 190px;
							     background-size: cover;
							     background-repeat: inherit;
							     background-position: center center;
							     background-image: url(/static/img/karota.png);">
						</div>
						<div class="dashedCircle rotating mx-auto"
						     style="height: 210px; width: 210px; margin-top: -200px;">
						</div>
					</div>
					<div class="col-lg-4 mb-3 order-2 order-lg-2">
						<div class="btn bgGreen2 text-white px-4" style="border-radius: 2rem;">Recipes</div>
					</div>
				</div>
			</div>
		</div>
	</div>

</template>

<script>
	import NutritionStats from './NutritionStats';

	export default {
		name: 'IngredientOfTheDay',
		components: {
			NutritionStats
		}
	};
</script>

<style scoped>

</style>
