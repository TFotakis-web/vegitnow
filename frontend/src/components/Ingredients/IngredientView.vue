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
						<div class="col-4 mt-auto mb-3">
							<router-link :to="{ name: 'RecipesList', query: { page:1, ingredients: ingredient.id } }" class="btn px-4 bgGreen0 text-white text-uppercase mx-auto" style="border-radius: 2rem;">
								{{ $t('Related recipes') }}
							</router-link>
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

							<router-link :to="{ name: 'RecipesList', query: { page:1, ingredients: ingredient.id } }" class="btn px-4 bgGreen0 text-white text-uppercase mx-auto mb-3" style="border-radius: 2rem;">
								{{ $t('Related recipes') }}
							</router-link>
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
			<div class="container pt-5 mb-5">
				<div class="row">
					<div class="col-lg-6 mb-3">
						<div class="mx-auto mr-lg-0 ml-lg-auto" style="width: max-content;">
							<h2 class="fgGreen1 ml-5 w-100" style="margin-bottom: -1rem">{{ $t('Vitamins') }}</h2>
							<div class="bg-white px-4 pb-4" style="width: max-content">
								<table class="v-table">
									<thead>
									<tr>
										<th></th>
										<th>{{ $t('Per') }} 100gr</th>
										<th class="text-center" colspan="2">{{ $t('RDI') }} %</th>
									</tr>
									</thead>
									<tbody>
									<tr>
										<td class="pl-0">{{ $t('Vitamin A') }}</td>
										<td>{{ ingredient.VitaminA }}IU</td>
										<td class="pl-0 text-right">{{ ingredient.VitaminAPerc }}%</td>
										<td class="px-0">
											<div class="progress">
												<div class="progress-bar bgGreen1" role="progressbar" :style="{ width: ingredient.VitaminAPerc + '%'}" :aria-valuenow="ingredient.VitaminAPerc" aria-valuemin="0" aria-valuemax="100"></div>
											</div>
										</td>
									</tr>
									<tr>
										<td class="pl-0">{{ $t('Carotin B') }}</td>
										<td>{{ ingredient.CarotinB }}mcg</td>
										<td class="pl-0 text-right">{{ ingredient.CarotinBPerc }}%</td>
										<td class="px-0">
											<div class="progress">
												<div class="progress-bar bgGreen1" role="progressbar" :style="{ width: ingredient.CarotinBPerc + '%'}" :aria-valuenow="ingredient.CarotinBPerc" aria-valuemin="0" aria-valuemax="100"></div>
											</div>
										</td>
									</tr>
									<tr>
										<td class="pl-0">{{ $t('Vitamin C') }}</td>
										<td>{{ ingredient.VitaminC }}mg</td>
										<td class="pl-0 text-right">{{ ingredient.VitaminCPerc }}%</td>
										<td class="px-0">
											<div class="progress">
												<div class="progress-bar bgGreen1" role="progressbar" :style="{ width: ingredient.VitaminCPerc + '%'}" :aria-valuenow="ingredient.VitaminCPerc" aria-valuemin="0" aria-valuemax="100"></div>
											</div>
										</td>
									</tr>
									<tr>
										<td class="pl-0">{{ $t('Vitamin D') }}</td>
										<td>{{ ingredient.VitaminD }}mg</td>
										<td class="pl-0 text-right">{{ ingredient.VitaminDPerc }}%</td>
										<td class="px-0">
											<div class="progress">
												<div class="progress-bar bgGreen1" role="progressbar" :style="{ width: ingredient.VitaminDPerc + '%'}" :aria-valuenow="ingredient.VitaminDPerc" aria-valuemin="0" aria-valuemax="100"></div>
											</div>
										</td>
									</tr>
									<tr>
										<td class="pl-0">{{ $t('Vitamin E') }}</td>
										<td>{{ ingredient.VitaminE }}mg</td>
										<td class="pl-0 text-right">{{ ingredient.VitaminEPerc }}%</td>
										<td class="px-0">
											<div class="progress">
												<div class="progress-bar bgGreen1" role="progressbar" :style="{ width: ingredient.VitaminEPerc + '%'}" :aria-valuenow="ingredient.VitaminEPerc" aria-valuemin="0" aria-valuemax="100"></div>
											</div>
										</td>
									</tr>
									<tr>
										<td class="pl-0">{{ $t('Vitamin K') }}</td>
										<td>{{ ingredient.VitaminK }}mcg</td>
										<td class="pl-0 text-right">{{ ingredient.VitaminKPerc }}%</td>
										<td class="px-0">
											<div class="progress">
												<div class="progress-bar bgGreen1" role="progressbar" :style="{ width: ingredient.VitaminKPerc + '%'}" :aria-valuenow="ingredient.VitaminKPerc" aria-valuemin="0" aria-valuemax="100"></div>
											</div>
										</td>
									</tr>
									<tr>
										<td class="pl-0">{{ $t('Vitamin B3') }}</td>
										<td>{{ ingredient.VitaminB3 }}mg</td>
										<td class="pl-0 text-right">{{ ingredient.VitaminB3Perc }}%</td>
										<td class="px-0">
											<div class="progress">
												<div class="progress-bar bgGreen1" role="progressbar" :style="{ width: ingredient.VitaminB3Perc + '%'}" :aria-valuenow="ingredient.VitaminB3Perc" aria-valuemin="0" aria-valuemax="100"></div>
											</div>
										</td>
									</tr>
									<tr>
										<td class="pl-0">{{ $t('Vitamin B6') }}</td>
										<td>{{ ingredient.VitaminB6 }}mg</td>
										<td class="pl-0 text-right">{{ ingredient.VitaminB6Perc }}%</td>
										<td class="px-0">
											<div class="progress">
												<div class="progress-bar bgGreen1" role="progressbar" :style="{ width: ingredient.VitaminB6Perc + '%'}" :aria-valuenow="ingredient.VitaminB6Perc" aria-valuemin="0" aria-valuemax="100"></div>
											</div>
										</td>
									</tr>
									<tr>
										<td class="pl-0">{{ $t('Vitamin B12') }}</td>
										<td>{{ ingredient.VitaminB12 }}mg</td>
										<td class="pl-0 text-right">{{ ingredient.VitaminB12Perc }}%</td>
										<td class="px-0">
											<div class="progress">
												<div class="progress-bar bgGreen1" role="progressbar" :style="{ width: ingredient.VitaminB12Perc + '%'}" :aria-valuenow="ingredient.VitaminB12Perc" aria-valuemin="0" aria-valuemax="100"></div>
											</div>
										</td>
									</tr>
									<tr>
										<td class="pl-0">{{ $t('Vitamin B9') }}</td>
										<td>{{ ingredient.VitaminB9 }}mcg</td>
										<td class="pl-0 text-right">{{ ingredient.VitaminB9Perc }}%</td>
										<td class="px-0">
											<div class="progress">
												<div class="progress-bar bgGreen1" role="progressbar" :style="{ width: ingredient.VitaminB9Perc + '%'}" :aria-valuenow="ingredient.VitaminB9Perc" aria-valuemin="0" aria-valuemax="100"></div>
											</div>
										</td>
									</tr>
									<tr>
										<td class="pl-0">{{ $t('Choline') }}</td>
										<td>{{ ingredient.Choline }}mg</td>
										<td class="pl-0 text-right">{{ ingredient.CholinePerc }}%</td>
										<td class="px-0">
											<div class="progress">
												<div class="progress-bar bgGreen1" role="progressbar" :style="{ width: ingredient.CholinePerc + '%'}" :aria-valuenow="ingredient.CholinePerc" aria-valuemin="0" aria-valuemax="100"></div>
											</div>
										</td>
									</tr>
									</tbody>
								</table>
							</div>
						</div>
					</div>
					<div class="col-lg-6 mb-3">
						<div class="mx-auto ml-lg-0 mr-lg-auto" style="width: max-content;">
							<h2 class="fgGreen1 ml-5 w-100" style="margin-bottom: -1rem">{{ $t('Minerals') }}</h2>
							<div class="bg-white px-4 pb-4" style="width: max-content">
								<table class="v-table">
									<thead>
									<tr>
										<th></th>
										<th>{{ $t('Per') }} 100gr</th>
										<th class="text-center" colspan="2">{{ $t('RDI') }} %</th>
									</tr>
									</thead>
									<tbody>
									<tr>
										<td class="pl-0">{{ $t('Calcium') }}</td>
										<td>{{ ingredient.Calcium }}mg</td>
										<td class="pl-0 text-right">{{ ingredient.CalciumPerc }}%</td>
										<td class="px-0">
											<div class="progress">
												<div class="progress-bar bgGreen1" role="progressbar" :style="{ width: ingredient.CalciumPerc + '%'}" :aria-valuenow="ingredient.CalciumPerc" aria-valuemin="0" aria-valuemax="100"></div>
											</div>
										</td>
									</tr>
									<tr>
										<td class="pl-0">{{ $t('Iron') }}</td>
										<td>{{ ingredient.Iron }}mg</td>
										<td class="pl-0 text-right">{{ ingredient.IronPerc }}%</td>
										<td class="px-0">
											<div class="progress">
												<div class="progress-bar bgGreen1" role="progressbar" :style="{ width: ingredient.IronPerc + '%'}" :aria-valuenow="ingredient.IronPerc" aria-valuemin="0" aria-valuemax="100"></div>
											</div>
										</td>
									</tr>
									<tr>
										<td class="pl-0">{{ $t('Magnesium') }}</td>
										<td>{{ ingredient.Magnesium }}mg</td>
										<td class="pl-0 text-right">{{ ingredient.MagnesiumPerc }}%</td>
										<td class="px-0">
											<div class="progress">
												<div class="progress-bar bgGreen1" role="progressbar" :style="{ width: ingredient.MagnesiumPerc + '%'}" :aria-valuenow="ingredient.MagnesiumPerc" aria-valuemin="0" aria-valuemax="100"></div>
											</div>
										</td>
									</tr>
									<tr>
										<td class="pl-0">{{ $t('Phosphorus') }}</td>
										<td>{{ ingredient.Phosphorus }}mg</td>
										<td class="pl-0 text-right">{{ ingredient.PhosphorusPerc }}%</td>
										<td class="px-0">
											<div class="progress">
												<div class="progress-bar bgGreen1" role="progressbar" :style="{ width: ingredient.PhosphorusPerc + '%'}" :aria-valuenow="ingredient.PhosphorusPerc" aria-valuemin="0" aria-valuemax="100"></div>
											</div>
										</td>
									</tr>
									<tr>
										<td class="pl-0">{{ $t('Potassium') }}</td>
										<td>{{ ingredient.Potassium }}mg</td>
										<td class="pl-0 text-right">{{ ingredient.PotassiumPerc }}%</td>
										<td class="px-0">
											<div class="progress">
												<div class="progress-bar bgGreen1" role="progressbar" :style="{ width: ingredient.PotassiumPerc + '%'}" :aria-valuenow="ingredient.PotassiumPerc" aria-valuemin="0" aria-valuemax="100"></div>
											</div>
										</td>
									</tr>
									<tr>
										<td class="pl-0">{{ $t('Sodium') }}</td>
										<td>{{ ingredient.Sodium }}mg</td>
										<td class="pl-0 text-right">{{ ingredient.SodiumPerc }}%</td>
										<td class="px-0">
											<div class="progress">
												<div class="progress-bar bgGreen1" role="progressbar" :style="{ width: ingredient.SodiumPerc + '%'}" :aria-valuenow="ingredient.SodiumPerc" aria-valuemin="0" aria-valuemax="100"></div>
											</div>
										</td>
									</tr>
									<tr>
										<td class="pl-0">{{ $t('Zinc') }}</td>
										<td>{{ ingredient.Zinc }}mg</td>
										<td class="pl-0 text-right">{{ ingredient.ZincPerc }}%</td>
										<td class="px-0">
											<div class="progress">
												<div class="progress-bar bgGreen1" role="progressbar" :style="{ width: ingredient.ZincPerc + '%'}" :aria-valuenow="ingredient.ZincPerc" aria-valuemin="0" aria-valuemax="100"></div>
											</div>
										</td>
									</tr>
									<tr>
										<td class="pl-0">{{ $t('Selenium') }}</td>
										<td>{{ ingredient.Selenium }}mcg</td>
										<td class="pl-0 text-right">{{ ingredient.SeleniumPerc }}%</td>
										<td class="px-0">
											<div class="progress">
												<div class="progress-bar bgGreen1" role="progressbar" :style="{ width: ingredient.SeleniumPerc + '%'}" :aria-valuenow="ingredient.SeleniumPerc" aria-valuemin="0" aria-valuemax="100"></div>
											</div>
										</td>
									</tr>
									<tr>
										<td class="pl-0">{{ $t('Manganese') }}</td>
										<td>{{ ingredient.Manganese }}mg</td>
										<td class="pl-0 text-right">{{ ingredient.ManganesePerc }}%</td>
										<td class="px-0">
											<div class="progress">
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
			<RecommendedRecipes :current-recipe-id="id" :ingredientsIncluded="[ingredient.id]" :title="$t('Recipes with') + ' ' + ingredient.Name + '!'"/>
		</div>
	</div>
</template>

<script>
	import Loader from '../Structure/Loader';
	import NutritionStats from '../Structure/NutritionStats';
	import RecommendedRecipes from '../Recipes/RecommendedRecipes';

	export default {
		name: 'IngredientView',
		components: {
			Loader,
			NutritionStats,
			RecommendedRecipes
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

						this.ingredient.Name = this.ingredient.Name.trim();
						this.ingredient.VitaminAPerc = 0 * Math.round(this.ingredient.VitaminA / 1 * 1000) / 10;
						this.ingredient.CarotinBPerc = 0 * Math.round(this.ingredient.CarotinB / 1 * 1000) / 10;
						this.ingredient.VitaminCPerc = Math.round(this.ingredient.VitaminC / 60 * 1000) / 10;
						this.ingredient.VitaminDPerc = 0 * Math.round(this.ingredient.VitaminD / 1 * 1000) / 10;
						this.ingredient.VitaminEPerc = 0 * Math.round(this.ingredient.VitaminE / 1 * 1000) / 10;
						this.ingredient.VitaminKPerc = Math.round(this.ingredient.VitaminK / 80 * 1000) / 10;
						this.ingredient.VitaminB3Perc = Math.round(this.ingredient.VitaminB3 / 20 * 1000) / 10;
						this.ingredient.VitaminB6Perc = Math.round(this.ingredient.VitaminB6 / 2 * 1000) / 10;
						this.ingredient.VitaminB12Perc = Math.round(this.ingredient.VitaminB12 / 0.006 * 1000) / 10;
						this.ingredient.VitaminB9Perc = 0 * Math.round(this.ingredient.VitaminB9 / 1 * 1000) / 10;
						this.ingredient.CholinePerc = Math.round(this.ingredient.Choline / 550 * 1000) / 10;
						this.ingredient.CalciumPerc = Math.round(this.ingredient.Calcium / 1000 * 1000) / 10;
						this.ingredient.IronPerc = Math.round(this.ingredient.Iron / 18 * 1000) / 10;
						this.ingredient.MagnesiumPerc = Math.round(this.ingredient.Magnesium / 400 * 1000) / 10;
						this.ingredient.PhosphorusPerc = Math.round(this.ingredient.Phosphorus / 1000 * 1000) / 10;
						this.ingredient.PotassiumPerc = Math.round(this.ingredient.Potassium / 4700 * 1000) / 10;
						this.ingredient.SodiumPerc = Math.round(this.ingredient.Sodium / 1500 * 1000) / 10;
						this.ingredient.ZincPerc = Math.round(this.ingredient.Zinc / 15 * 1000) / 10;
						this.ingredient.SeleniumPerc = Math.round(this.ingredient.Selenium / 70 * 1000) / 10;
						this.ingredient.ManganesePerc = Math.round(this.ingredient.Manganese / 2 * 1000) / 10;

						this.$router.push('?title=' + this.$root.toGreeklish(this.ingredient.Name).replace(/ /g, '-'));

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
	.progress {
		width: 7rem;
	}

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
