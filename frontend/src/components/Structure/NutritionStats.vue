<template>
	<div>
		<div class="d-flex justify-content-center justify-content-lg-start" style="font-size: 0.8em; border-radius: 2px">
			<div class="p-4 bg-white text-center calories-box-clip-path" style="margin-right: -3rem; position: relative; z-index: 1">
				<h6 class="text-capitalize m-0 sans fgGreen1">{{ $t('Energy') }}</h6>
				<strong class="fgGreen1">{{ calories }}</strong>
				<p class="sans fgGreen0 m-0">{{ caloriesPerc }}%*</p>
			</div>
			<div class="d-flex nutritionStats-box-clip-path">
				<div class="p-3 bgGreen4 text-center pl-5">
					<h6 class="text-capitalize m-0 sans fgGreen1">{{ $t('Carbohydrate') }}</h6>
					<strong class="fgGreen1">{{ carbohydrate }}g</strong>
					<p class="sans fgGreen0 m-0">{{ carbohydratePerc }}%*</p>
				</div>
				<div class="p-3 bgGreen4 text-center">
					<h6 class="text-capitalize m-0 sans fgGreen1">{{ $t('Fat') }}</h6>
					<strong class="fgGreen1">{{ fat }}g</strong>
					<p class="sans fgGreen0 m-0">{{ fatPerc }}%*</p>
				</div>
				<div class="p-3 bgGreen4 text-center">
					<h6 class="text-capitalize m-0 sans fgGreen1">{{ $t('Sat. Fat') }}</h6>
					<strong class="fgGreen1">{{ satFat }}g</strong>
					<p class="sans fgGreen0 m-0">{{ satFatPerc }}%*</p>
				</div>
				<div class="p-3 bgGreen4 text-center"
				     style="border-top-right-radius: 2px; border-bottom-right-radius: 2px;">
					<h6 class="text-capitalize m-0 sans fgGreen1">{{ $t('Salt') }}</h6>
					<strong class="fgGreen1">{{ salt }}mg</strong>
					<p class="sans fgGreen0 m-0">{{ saltPerc }}%*</p>
				</div>
			</div>
		</div>
		<p class="text-dark text-center text-lg-left" style="font-size: 0.8em;">* {{ $t('Reference intake of an average adult') }} (8400kJ/2000kcal)</p>
	</div>
</template>

<script>
	export default {
		name: 'NutritionStats',
		props: {
			ingredientList: {
				type: Array,
				default: () => []
			},
			dishes: {
				type: Number,
				default: 1
			}
		},
		data: function () {
			return {
				calories: 0,
				carbohydrate: 0,
				fat: 0,
				satFat: 0,
				salt: 0,
				caloriesPerc: 0,
				carbohydratePerc: 0,
				fatPerc: 0,
				satFatPerc: 0,
				saltPerc: 0,
				requestsUnsatisfied: 0
			};
		},
		mounted: function () {
			this.getIngredientData();
		},
		methods: {
			getIngredientData: function () {
				for (let i = 0; i < this.ingredientList.length; i++) {
					this.requestsUnsatisfied++;
					this.$http.get('/api/ingredient/' + this.ingredientList[i].id + '/?locale=' + this.$cookie.get('locale'))
						.then(response => {
							this.ingredientList[i] = Object.assign({}, this.ingredientList[i], response.data);
							this.requestsUnsatisfied--;
						})
						.catch(this.$root.notifyAction.error);
				}
				return;
			}
		},
		watch: {
			requestsUnsatisfied: function (newValue, oldValue) {
				if (newValue) return;
				for (const ingredient of this.ingredientList) {
					this.calories += ingredient.Calories * ingredient.Quantity / 100 / this.dishes;
					this.carbohydrate += ingredient.CarbonHydrates * ingredient.Quantity / 100 / this.dishes;
					this.fat += ingredient.Fats * ingredient.Quantity / 100 / this.dishes;
					this.satFat += ingredient.SaturatedFats * ingredient.Quantity / 100 / this.dishes;
					this.salt += ingredient.Sodium * ingredient.Quantity / 100 / this.dishes;
				}
				this.calories = Math.round(this.calories * 10) / 10;
				this.carbohydrate = Math.round(this.carbohydrate * 10) / 10;
				this.fat = Math.round(this.fat * 10) / 10;
				this.satFat = Math.round(this.satFat * 10) / 10;
				this.salt = Math.round(this.salt * 10) / 10;

				this.caloriesPerc = this.calories / 2000 * 100;
				this.carbohydratePerc = this.carbohydrate / 260 * 100;
				this.fatPerc = this.fat / 70 * 100;
				this.satFatPerc = this.satFat / 20 * 100;
				this.saltPerc = this.salt / 6000 * 100;

				this.caloriesPerc = Math.round(this.caloriesPerc * 10) / 10;
				this.carbohydratePerc = Math.round(this.carbohydratePerc * 10) / 10;
				this.fatPerc = Math.round(this.fatPerc * 10) / 10;
				this.satFatPerc = Math.round(this.satFatPerc * 10) / 10;
				this.saltPerc = Math.round(this.saltPerc * 10) / 10;
			}
		}
	};
</script>

<style scoped>
	.calories-box-clip-path {
		mask-image: url(/static/app/img/clip-masks/calories-clip-mask.svg?v1.0);
		mask-mode: alpha;
		mask-repeat: no-repeat;
		mask-size: 100%;
		mask-position: center;
	}

	.nutritionStats-box-clip-path {
		mask-image: url(/static/app/img/clip-masks/nutritionStats-clip-mask.svg?v1.0);
		mask-mode: alpha;
		mask-repeat: no-repeat;
		mask-size: 100%;
		mask-position: center;
	}
</style>
