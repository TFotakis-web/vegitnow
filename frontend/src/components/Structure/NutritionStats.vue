<template>
	<div>
	<table class="text-center d-inline-block" style="width: min-content">
		<tr>
			<td>
				<div class="calories-box-clip-path p-3" :class="calories_bg" style="position: relative; z-index: 2;">
					<h6 class="text-capitalize m-0 sans">{{ $t('Energy') }}</h6>
					<strong>{{ calories }}</strong>
					<p class="sans m-0">{{ caloriesPerc }}%*</p>
				</div>
			</td>
			<td>
				<div class="nutritionStats-box-clip-path bgGreen4" style="margin-left: -3rem; position: relative; z-index: 1;">
					<table class="table table-borderless m-0">
						<tbody>
						<tr>
							<td class="pl-5">
								<h6 class="text-capitalize m-0 sans fgGreen1">{{ $t('Protein') }}</h6>
								<strong class="fgGreen1">{{ proteins }}g</strong>
								<p class="sans fgGreen0 m-0">{{ proteinsPerc }}%*</p>
							</td>
							<td>
								<h6 class="text-capitalize m-0 sans fgGreen1">{{ $t('Carbohydrate') }}</h6>
								<strong class="fgGreen1">{{ carbohydrate }}g</strong>
								<p class="sans fgGreen0 m-0">{{ carbohydratePerc }}%*</p>
							</td>
							<td class="pr-5">
								<h6 class="text-capitalize m-0 sans fgGreen1">{{ $t('Fat') }}</h6>
								<strong class="fgGreen1">{{ fat }}g</strong>
								<p class="sans fgGreen0 m-0">{{ fatPerc }}%*</p>
							</td>
						</tr>
						</tbody>
					</table>
				</div>
			</td>
		</tr>
		<tr>
			<td colspan="4">
				<p class="text-dark text-center m-0" style="font-size: 0.7em;">* {{ $t('Reference intake of an average adult per serving') }} (8400kJ/2000kcal)</p>
			</td>
		</tr>
	</table>
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
			},
			calories_bg: {
				type: String,
				default: 'calories-light'
			}
		},
		data: function () {
			return {
				calories: 0,
				carbohydrate: 0,
				fat: 0,
				proteins: 0,
				salt: 0,
				caloriesPerc: 0,
				carbohydratePerc: 0,
				fatPerc: 0,
				proteinsPerc: 0,
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
					this.proteins += ingredient.Protein * ingredient.Quantity / 100 / this.dishes;
					this.carbohydrate += ingredient.CarbonHydrates * ingredient.Quantity / 100 / this.dishes;
					this.fat += ingredient.Fats * ingredient.Quantity / 100 / this.dishes;
					this.salt += ingredient.Sodium * ingredient.Quantity / 100 / this.dishes;
				}
				this.calories = Math.round(this.calories * 10) / 10;
				this.proteins = Math.round(this.proteins * 10) / 10;
				this.carbohydrate = Math.round(this.carbohydrate * 10) / 10;
				this.fat = Math.round(this.fat * 10) / 10;
				this.salt = Math.round(this.salt * 10) / 10;

				this.caloriesPerc = this.calories / 2000 * 100;
				this.proteinsPerc = this.proteins / 50 * 100;
				this.carbohydratePerc = this.carbohydrate / 260 * 100;
				this.fatPerc = this.fat / 70 * 100;
				this.saltPerc = this.salt / 6000 * 100;

				this.caloriesPerc = Math.round(this.caloriesPerc * 10) / 10;
				this.proteinsPerc = Math.round(this.proteinsPerc * 10) / 10;
				this.carbohydratePerc = Math.round(this.carbohydratePerc * 10) / 10;
				this.fatPerc = Math.round(this.fatPerc * 10) / 10;
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

	.calories-light {
		background: white;
	}

	.calories-light h6, strong {
		color: var(--v-green6);
	}

	.calories-light p {
		color: var(--v-green5);
	}

	.calories-dark {
		background: var(--v-green0);
	}

	.calories-dark > h6 {
		color: white !important;
	}

	.calories-dark > strong {
		color: white !important;
	}

	.calories-dark > p {
		color: white !important;
	}
</style>
