<template>
	<div id="ingredientView" class="d-flex flex-grow-1">
		<Loader v-if="requestsUnsatisfied"/>
		<div v-if="!requestsUnsatisfied" class="flex-grow-1">
			<div class="bgGreen1">
				<div class="container py-5 d-none d-lg-block">
					<div class="row v-border-bottom">
						<div class="col-4 mt-auto mb-2">
							<h1 class="fgGreen0">{{ ingredient.Name }}</h1>
						</div>
						<div class="col-4">
							<div class="ingredient-thumbnail mx-auto">
								<div class="dashedCircle v-border rotating bgGreen1" style="position:relative; z-index: 1;"></div>
								<div class="ingredientThumbnailCircle">
									<div class="bg-white rounded-circle ingredient-img mx-auto" style="position:relative; z-index: 2;" :style="{ 'background-image': 'url(' + ingredient.Thumbnail + ')' }"></div>
								</div>
							</div>
						</div>
						<div class="col-4">

						</div>
					</div>
					<div class="row">
						<div class="col-4 my-auto">
							<NutritionStats class="pt-3" :ingredient-list="[Object.assign({}, ingredient, {Quantity: 100})]" calories_bg="calories-dark"/>
						</div>
						<div class="col-4"></div>
						<div class="col-4"></div>
					</div>
				</div>

				<div class="container d-lg-none">
					<div class="row pt-5">
						<div class="col text-center">
							<h1 class="fgGreen0">{{ ingredient.Name }}</h1>
							<NutritionStats class="pt-3" :ingredient-list="[Object.assign({}, ingredient, {Quantity: 100})]" calories_bg="calories-dark"/>
						</div>
					</div>
					<div class="row ingredient-thumbnail-bottom-margin">
						<div class="ingredient-thumbnail mx-auto">
							<div class="dashedCircle v-border rotating"></div>
							<div class="ingredientThumbnailCircle">
								<div class="bg-white rounded-circle ingredient-img mx-auto" :style="{ 'background-image': 'url(' + ingredient.Thumbnail + ')' }"></div>
							</div>
						</div>
					</div>
				</div>
			</div>
			<div class="container pt-5">
				<div class="row">
					<div class="col-6 mb-3">
						<h2 class="fgGreen1 ml-5 w-100" style="margin-bottom: -1rem">{{ $t('Vitamins') }}</h2>
						<div class="bg-white px-5 pb-5" style="width: max-content">
							<table class="v-table">
								<thead>
								<tr>
									<th></th>
									<th>{{ $t('Per') }} 100gr</th>
									<th>{{ $t('RDI') }} %</th>
									<th></th>
								</tr>
								</thead>
								<tbody>
								<tr>
									<td class="pl-0">{{ $t('Vitamin A') }}</td>
									<td>{{ ingredient.VitaminA }}IU</td>
									<td>{{ ingredient.VitaminAPerc }}%</td>
									<td class="pr-0">
										<div class="progress" style="width: 10rem">
											<div class="progress-bar bgGreen1" role="progressbar" :style="{ width: ingredient.VitaminAPerc + '%'}" :aria-valuenow="ingredient.VitaminAPerc" aria-valuemin="0" aria-valuemax="100"></div>
										</div>
									</td>
								</tr>
								<tr>
									<td class="pl-0">{{ $t('Carotin B') }}</td>
									<td>{{ ingredient.CarotinB }}mcg</td>
									<td>{{ ingredient.CarotinBPerc }}</td>
									<td class="pr-0">
										<div class="progress" style="width: 10rem">
											<div class="progress-bar bgGreen1" role="progressbar" :style="{ width: ingredient.CarotinBPerc + '%'}" :aria-valuenow="ingredient.CarotinBPerc" aria-valuemin="0" aria-valuemax="100"></div>
										</div>
									</td>
								</tr>
								<tr>
									<td class="pl-0">{{ $t('Vitamin C') }}</td>
									<td>{{ ingredient.VitaminC }}mg</td>
									<td>{{ ingredient.VitaminCPerc }}</td>
									<td class="pr-0">
										<div class="progress" style="width: 10rem">
											<div class="progress-bar bgGreen1" role="progressbar" :style="{ width: ingredient.VitaminCPerc + '%'}" :aria-valuenow="ingredient.VitaminCPerc" aria-valuemin="0" aria-valuemax="100"></div>
										</div>
									</td>
								</tr>
								<tr>
									<td class="pl-0">{{ $t('Vitamin D') }}</td>
									<td>{{ ingredient.VitaminD }}mg</td>
									<td>{{ ingredient.VitaminDPerc }}</td>
									<td class="pr-0">
										<div class="progress" style="width: 10rem">
											<div class="progress-bar bgGreen1" role="progressbar" :style="{ width: ingredient.VitaminDPerc + '%'}" :aria-valuenow="ingredient.VitaminDPerc" aria-valuemin="0" aria-valuemax="100"></div>
										</div>
									</td>
								</tr>
								<tr>
									<td class="pl-0">{{ $t('Vitamin E') }}</td>
									<td>{{ ingredient.VitaminE }}mg</td>
									<td>{{ ingredient.VitaminEPerc }}</td>
									<td class="pr-0">
										<div class="progress" style="width: 10rem">
											<div class="progress-bar bgGreen1" role="progressbar" :style="{ width: ingredient.VitaminEPerc + '%'}" :aria-valuenow="ingredient.VitaminEPerc" aria-valuemin="0" aria-valuemax="100"></div>
										</div>
									</td>
								</tr>
								<tr>
									<td class="pl-0">{{ $t('Vitamin K') }}</td>
									<td>{{ ingredient.VitaminK }}mcg</td>
									<td>{{ ingredient.VitaminKPerc }}</td>
									<td class="pr-0">
										<div class="progress" style="width: 10rem">
											<div class="progress-bar bgGreen1" role="progressbar" :style="{ width: ingredient.VitaminKPerc + '%'}" :aria-valuenow="ingredient.VitaminKPerc" aria-valuemin="0" aria-valuemax="100"></div>
										</div>
									</td>
								</tr>
								<tr>
									<td class="pl-0">{{ $t('Vitamin B3') }}</td>
									<td>{{ ingredient.VitaminB3 }}mg</td>
									<td>{{ ingredient.VitaminB3Perc }}</td>
									<td class="pr-0">
										<div class="progress" style="width: 10rem">
											<div class="progress-bar bgGreen1" role="progressbar" :style="{ width: ingredient.VitaminB3Perc + '%'}" :aria-valuenow="ingredient.VitaminB3Perc" aria-valuemin="0" aria-valuemax="100"></div>
										</div>
									</td>
								</tr>
								<tr>
									<td class="pl-0">{{ $t('Vitamin B6') }}</td>
									<td>{{ ingredient.VitaminB6 }}mg</td>
									<td>{{ ingredient.VitaminB6Perc }}</td>
									<td class="pr-0">
										<div class="progress" style="width: 10rem">
											<div class="progress-bar bgGreen1" role="progressbar" :style="{ width: ingredient.VitaminB6Perc + '%'}" :aria-valuenow="ingredient.VitaminB6Perc" aria-valuemin="0" aria-valuemax="100"></div>
										</div>
									</td>
								</tr>
								<tr>
									<td class="pl-0">{{ $t('Vitamin B12') }}</td>
									<td>{{ ingredient.VitaminB12 }}mg</td>
									<td>{{ ingredient.VitaminB12Perc }}</td>
									<td class="pr-0">
										<div class="progress" style="width: 10rem">
											<div class="progress-bar bgGreen1" role="progressbar" :style="{ width: ingredient.VitaminB12Perc + '%'}" :aria-valuenow="ingredient.VitaminB12Perc" aria-valuemin="0" aria-valuemax="100"></div>
										</div>
									</td>
								</tr>
								<tr>
									<td class="pl-0">{{ $t('Vitamin B9') }}</td>
									<td>{{ ingredient.VitaminB9 }}mcg</td>
									<td>{{ ingredient.VitaminB9Perc }}</td>
									<td class="pr-0">
										<div class="progress" style="width: 10rem">
											<div class="progress-bar bgGreen1" role="progressbar" :style="{ width: ingredient.VitaminB9Perc + '%'}" :aria-valuenow="ingredient.VitaminB9Perc" aria-valuemin="0" aria-valuemax="100"></div>
										</div>
									</td>
								</tr>
								<tr>
									<td class="pl-0">{{ $t('Choline') }}</td>
									<td>{{ ingredient.Choline }}mg</td>
									<td>{{ ingredient.CholinePerc }}</td>
									<td class="pr-0">
										<div class="progress" style="width: 10rem">
											<div class="progress-bar bgGreen1" role="progressbar" :style="{ width: ingredient.CholinePerc + '%'}" :aria-valuenow="ingredient.CholinePerc" aria-valuemin="0" aria-valuemax="100"></div>
										</div>
									</td>
								</tr>
								</tbody>
							</table>
						</div>
					</div>
					<div class="col-6 mb-3">
						<h2 class="fgGreen1 ml-5  w-100" style="margin-bottom: -1rem">{{ $t('Minerals') }}</h2>
						<div class="bg-white px-5 pb-5" style="width: max-content">
							<table class="v-table">
								<thead>
								<tr>
									<th></th>
									<th>{{ $t('Per') }} 100gr</th>
									<th>{{ $t('RDI') }} %</th>
									<th></th>
								</tr>
								</thead>
								<tbody>
								<tr>
									<td class="pl-0">{{ $t('Calcium') }}</td>
									<td>{{ ingredient.Calcium }}mg</td>
									<td>{{ ingredient.CalciumPerc }}</td>
									<td class="pr-0">
										<div class="progress" style="width: 10rem">
											<div class="progress-bar bgGreen1" role="progressbar" :style="{ width: ingredient.CalciumPerc + '%'}" :aria-valuenow="ingredient.CalciumPerc" aria-valuemin="0" aria-valuemax="100"></div>
										</div>
									</td>
								</tr>
								<tr>
									<td class="pl-0">{{ $t('Iron') }}</td>
									<td>{{ ingredient.Iron }}mg</td>
									<td>{{ ingredient.IronPerc }}</td>
									<td class="pr-0">
										<div class="progress" style="width: 10rem">
											<div class="progress-bar bgGreen1" role="progressbar" :style="{ width: ingredient.IronPerc + '%'}" :aria-valuenow="ingredient.IronPerc" aria-valuemin="0" aria-valuemax="100"></div>
										</div>
									</td>
								</tr>
								<tr>
									<td class="pl-0">{{ $t('Magnesium') }}</td>
									<td>{{ ingredient.Magnesium }}mg</td>
									<td>{{ ingredient.MagnesiumPerc }}</td>
									<td class="pr-0">
										<div class="progress" style="width: 10rem">
											<div class="progress-bar bgGreen1" role="progressbar" :style="{ width: ingredient.MagnesiumPerc + '%'}" :aria-valuenow="ingredient.MagnesiumPerc" aria-valuemin="0" aria-valuemax="100"></div>
										</div>
									</td>
								</tr>
								<tr>
									<td class="pl-0">{{ $t('Phosphorus') }}</td>
									<td>{{ ingredient.Phosphorus }}mg</td>
									<td>{{ ingredient.PhosphorusPerc }}</td>
									<td class="pr-0">
										<div class="progress" style="width: 10rem">
											<div class="progress-bar bgGreen1" role="progressbar" :style="{ width: ingredient.PhosphorusPerc + '%'}" :aria-valuenow="ingredient.PhosphorusPerc" aria-valuemin="0" aria-valuemax="100"></div>
										</div>
									</td>
								</tr>
								<tr>
									<td class="pl-0">{{ $t('Potassium') }}</td>
									<td>{{ ingredient.Potassium }}mg</td>
									<td>{{ ingredient.PotassiumPerc }}</td>
									<td class="pr-0">
										<div class="progress" style="width: 10rem">
											<div class="progress-bar bgGreen1" role="progressbar" :style="{ width: ingredient.PotassiumPerc + '%'}" :aria-valuenow="ingredient.PotassiumPerc" aria-valuemin="0" aria-valuemax="100"></div>
										</div>
									</td>
								</tr>
								<tr>
									<td class="pl-0">{{ $t('Sodium') }}</td>
									<td>{{ ingredient.Sodium }}mg</td>
									<td>{{ ingredient.SodiumPerc }}</td>
									<td class="pr-0">
										<div class="progress" style="width: 10rem">
											<div class="progress-bar bgGreen1" role="progressbar" :style="{ width: ingredient.SodiumPerc + '%'}" :aria-valuenow="ingredient.SodiumPerc" aria-valuemin="0" aria-valuemax="100"></div>
										</div>
									</td>
								</tr>
								<tr>
									<td class="pl-0">{{ $t('Zinc') }}</td>
									<td>{{ ingredient.Zinc }}mg</td>
									<td>{{ ingredient.ZincPerc }}</td>
									<td class="pr-0">
										<div class="progress" style="width: 10rem">
											<div class="progress-bar bgGreen1" role="progressbar" :style="{ width: ingredient.ZincPerc + '%'}" :aria-valuenow="ingredient.ZincPerc" aria-valuemin="0" aria-valuemax="100"></div>
										</div>
									</td>
								</tr>
								<tr>
									<td class="pl-0">{{ $t('Selenium') }}</td>
									<td>{{ ingredient.Selenium }}mcg</td>
									<td>{{ ingredient.SeleniumPerc }}</td>
									<td class="pr-0">
										<div class="progress" style="width: 10rem">
											<div class="progress-bar bgGreen1" role="progressbar" :style="{ width: ingredient.SeleniumPerc + '%'}" :aria-valuenow="ingredient.SeleniumPerc" aria-valuemin="0" aria-valuemax="100"></div>
										</div>
									</td>
								</tr>
								<tr>
									<td class="pl-0">{{ $t('Manganese') }}</td>
									<td>{{ ingredient.Manganese }}mg</td>
									<td>{{ ingredient.ManganesePerc }}</td>
									<td class="pr-0">
										<div class="progress" style="width: 10rem">
											<div class="progress-bar bgGreen1" role="progressbar" :style="{ width: ingredient.ManganesePerc + '%'}" :aria-valuenow="ingredient.ManganesePerc" aria-valuemin="0" aria-valuemax="100"></div>
										</div>
									</td>
								</tr>
								</tbody>
							</table>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import Loader from '../Structure/Loader';
	import NutritionStats from '../Structure/NutritionStats';

	export default {
		name: 'IngredientView',
		components: {
			Loader,
			NutritionStats
		},
		data: function () {
			return {
				id: this.$route.params['id'].toString(),
				ingredient: {},
				requestsUnsatisfied: -1
			};
		},
		mounted: function () {
			this.getIngredientData();
		},
		methods: {
			getIngredientData: function () {
				this.requestsUnsatisfied = this.requestsUnsatisfied === -1 ? 1 : this.requestsUnsatisfied + 1;
				this.$http.get('/api/ingredient/' + this.id + '/?locale=' + this.$cookie.get('locale'))
					.then(response => {
						this.ingredient = response.data;
						this.ingredient.Preview = this.$root.$t('Energy') + ': ' + this.ingredient.Calories + 'cal | ' +
							this.$root.$t('Protein') + ': ' + this.ingredient.Protein + 'g | ' +
							this.$root.$t('Carbohydrate') + ': ' + this.ingredient.CarbonHydrates + 'g | ' +
							this.$root.$t('Fat') + ': ' + this.ingredient.Fats + 'g';
						this.ingredient.VitaminAPerc = this.ingredient.VitaminA;
						this.ingredient.CarotinBPerc = this.ingredient.CarotinB;
						this.ingredient.VitaminCPerc = this.ingredient.VitaminC;
						this.ingredient.VitaminDPerc = this.ingredient.VitaminD;
						this.ingredient.VitaminEPerc = this.ingredient.VitaminE;
						this.ingredient.VitaminKPerc = this.ingredient.VitaminK;
						this.ingredient.VitaminB3Perc = this.ingredient.VitaminB3;
						this.ingredient.VitaminB6Perc = this.ingredient.VitaminB6;
						this.ingredient.VitaminB12Perc = this.ingredient.VitaminB12;
						this.ingredient.VitaminB9Perc = this.ingredient.VitaminB9;
						this.ingredient.CholinePerc = this.ingredient.Choline;
						this.ingredient.CalciumPerc = this.ingredient.Calcium;
						this.ingredient.IronPerc = this.ingredient.Iron;
						this.ingredient.MagnesiumPerc = this.ingredient.Magnesium;
						this.ingredient.PhosphorusPerc = this.ingredient.Phosphorus;
						this.ingredient.PotassiumPerc = this.ingredient.Potassium;
						this.ingredient.SodiumPerc = this.ingredient.Sodium;
						this.ingredient.ZincPerc = this.ingredient.Zinc;
						this.ingredient.SeleniumPerc = this.ingredient.Selenium;
						this.ingredient.ManganesePerc = this.ingredient.Manganese;
						this.$emit('updateHead');
						this.requestsUnsatisfied--;
					})
					.catch(this.$root.notifyAction.error);
				return;
			}

		},
		head: {
			title: function () {
				return this.ingredient.Name ? {inner: this.ingredient.Name} : '';
			},
			meta: function () {
				return this.$root.headData.updateMeta({
					GeneralDescription: this.ingredient.Preview,
					// GeneralKeywords: '',
					GooglePlusName: this.ingredient.Name,
					GooglePlusDescription: this.ingredient.Preview,
					GooglePlusImage: location.origin + this.ingredient.Thumbnail,
					// TwitterCard: '',
					// TwitterSite: '',
					TwitterTitle: this.ingredient.Name,
					TwitterDescription: this.ingredient.Preview,
					// TwitterCreator: '',
					TwitterImage: location.origin + this.ingredient.Thumbnail,
					OpenGraphTitle: this.ingredient.Name,
					OpenGraphType: 'article',
					OpenGraphUrl: location.href,
					OpenGraphImage: location.origin + this.ingredient.Thumbnail,
					OpenGraphDescription: this.ingredient.Preview,
					// OpenGraphSiteName: '',
					// OpenGraphPublishedTime: '',
					// OpenGraphModifiedTime: '',
					// OpenGraphSection: '',
					// OpenGraphTag: '',
					// OpenGraphAdmins: ''
				});
			}
		}
	};
</script>

<style scoped>
	#ingredientView {
		--v-dashed-circle-size: 250px;
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
		margin-bottom: calc(-1 * var(--v-dashed-circle-size) / 2);
	}

	.ingredient-card {
		min-width: max-content;
	}

	.ingredient-thumbnail-bottom-margin {
		margin-bottom: calc(var(--v-dashed-circle-size) / 2);
	}

	.v-border-bottom-dotted {
		border-bottom: dotted;
	}

	.v-table {
		width: max-content;
		color: #212529;
	}

	.v-table td, .v-table th {
		padding: .75rem;
		vertical-align: middle;
	}

	.v-table td {
		border-bottom: 2px dotted #dee2e6;
	}
</style>
