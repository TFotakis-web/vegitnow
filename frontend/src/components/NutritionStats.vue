<template>
	<div>
		<div class="d-flex justify-content-center justify-content-lg-start" style="font-size: 0.8em; border-radius: 2px">
			<div class="p-2 bg-white text-center" style="border-top-left-radius: 2px; border-bottom-left-radius: 2px;">
				<p class="text-capitalize m-0 sans">Energy</p>
				<strong>137</strong>
				<p class="sans fgGreen0 m-0">6.7%*</p>
			</div>
			<div class="p-2 bgGreen4 text-center">
				<p class="text-capitalize m-0 sans">Carbohydrate</p>
				<strong>3.8g</strong>
				<p class="sans fgGreen0 m-0">6.7%*</p>
			</div>
			<div class="p-2 bgGreen4 text-center">
				<p class="text-capitalize m-0 sans">Fat</p>
				<strong>5g</strong>
				<p class="sans fgGreen0 m-0">6.7%*</p>
			</div>
			<div class="p-2 bgGreen4 text-center">
				<p class="text-capitalize m-0 sans">Sat. Fat</p>
				<strong>2.4g</strong>
				<p class="sans fgGreen0 m-0">6.7%*</p>
			</div>
			<div class="p-2 bgGreen4 text-center"
			     style="border-top-right-radius: 2px; border-bottom-right-radius: 2px;">
				<p class="text-capitalize m-0 sans">Salt</p>
				<strong>0.4g</strong>
				<p class="sans fgGreen0 m-0">6.7%*</p>
			</div>
		</div>
		<p class="text-dark text-center text-lg-left" style="font-size: 0.8em;">* Reference intake of an average adult (8400kJ/2000kcal)</p>
	</div>
</template>

<script>
	export default {
		name: 'NutritionStats'
	};
</script>

<style scoped>

</style>
