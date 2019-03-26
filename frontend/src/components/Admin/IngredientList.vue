<template>
	<div id="AdminIngredientList" class="d-flex flex-grow-1">
		<Loader v-if="requestsUnsatisfied"/>
		<div v-if="!requestsUnsatisfied" class="container">
			<div class="form-group row">
				<label class="col-sm-2 col-form-label">{{ $t('Import Ingredients') }}:</label>
				<div class="col-sm-3 mb-2">
					<div class="custom-file">
						<label class="custom-file-label" for="csvFile">{{ $t('Choose file') }}</label>
						<input type="file" class="custom-file-input" id="csvFile" @change="onFileChange($event)">
					</div>
				</div>
				<div class="col-sm-3">
					<button type="button" class="btn bgGreen0 text-white" @click="importIngredients()"><i class="fas fa-save"></i> {{ $t('Import') }}</button>
				</div>
				<div class="col-sm-4">
					<span v-if="importCount > 0">Succesfully Imported: {{ importCount }}</span>
					<span v-if="importCount > 0 && importErrors > 0"> | </span>
					<span v-if="importErrors > 0">Import Errors: {{ importErrors }}</span>
					<span v-if="!done"> | Done</span>
				</div>
			</div>
			<div class="form-group row">
				<div class="col">
					<button type="button" class="btn bgGreen0 text-white" @click="createIngredient()"><i class="fas fa-plus"></i> {{ $t('Create New') }}</button>
				</div>
			</div>
			<div class="row">
				<div class="table-responsive">
					<table class="table text-center" v-if="ingredients.length!==0">
						<thead>
						<tr>
							<th scope="col">Actions</th>
							<th scope="col">#</th>
							<th scope="col">{{ $t('English') }}</th>
							<th scope="col">{{ $t('Greek') }}</th>
							<th scope="col">{{ $t('Calories') }} (kcal)</th>
							<th scope="col">{{ $t('Protein') }} (gr)</th>
							<th scope="col">{{ $t('Carbon Hydrates') }} (gr)</th>
							<th scope="col">{{ $t('Fats') }} (gr)</th>
							<th scope="col">{{ $t('Vitamin A') }} (IU)</th>
							<th scope="col">{{ $t('Carotin B') }} (mcg)</th>
							<th scope="col">{{ $t('Vitamin C') }} (mg)</th>
							<th scope="col">{{ $t('Vitamin D') }} (mg)</th>
							<th scope="col">{{ $t('Vitamin E') }} (mg)</th>
							<th scope="col">{{ $t('Vitamin K') }} (mcg)</th>
							<th scope="col">{{ $t('Vitamin B3') }} (mg)</th>
							<th scope="col">{{ $t('Vitamin B6') }} (mg)</th>
							<th scope="col">{{ $t('Vitamin B12') }} (mg)</th>
							<th scope="col">{{ $t('Vitamin B9') }} (mcg)</th>
							<th scope="col">{{ $t('Choline') }} (mg)</th>
							<th scope="col">{{ $t('Calcium') }} (mg)</th>
							<th scope="col">{{ $t('Iron') }} (mg)</th>
							<th scope="col">{{ $t('Magnesium') }} (mg)</th>
							<th scope="col">{{ $t('Phosphorus') }} (mg)</th>
							<th scope="col">{{ $t('Potassium') }} (mg)</th>
							<th scope="col">{{ $t('Sodium') }} (mg)</th>
							<th scope="col">{{ $t('Zinc') }} (mg)</th>
							<th scope="col">{{ $t('Selenium') }} (mcg)</th>
							<th scope="col">{{ $t('Manganese') }} (mg)</th>
							<th scope="col">{{ $t('Water') }} (gr)</th>
						</tr>
						</thead>
						<tbody>

						<tr v-if="createNew || editIngredient">
							<td v-if="createNew && !editIngredient">
								<a class="text-dark" @click="saveNewIngredient()"><i class="fas fa-save"></i></a>
								<a class="text-dark" @click="cancelNewIngredient()"><i class="fas fa-trash"></i></a>
							</td>
							<td v-if="!createNew && editIngredient">
								<a class="text-dark" @click="patchIngredient()"><i class="fas fa-save"></i></a>
								<a class="text-dark" @click="cancelPatchIngredient()"><i class="fas fa-trash"></i></a>
							</td>
							<td></td>
							<td><input type="text" class="form-control mb-3" id="ingredientDataEnglish" v-model="ingredientData.English"></td>
							<td><input type="text" class="form-control mb-3" id="ingredientDataGreek" v-model="ingredientData.Greek"></td>
							<td><input type="number" class="form-control mb-3" id="ingredientDataCalories" v-model="ingredientData.Calories"></td>
							<td><input type="number" class="form-control mb-3" id="ingredientDataProtein" v-model="ingredientData.Protein"></td>
							<td><input type="number" class="form-control mb-3" id="ingredientDataCarbonHydrates" v-model="ingredientData.CarbonHydrates"></td>
							<td><input type="number" class="form-control mb-3" id="ingredientDataFats" v-model="ingredientData.Fats"></td>
							<td><input type="number" class="form-control mb-3" id="ingredientDataVitaminA" v-model="ingredientData.VitaminA"></td>
							<td><input type="number" class="form-control mb-3" id="ingredientDataCarotinB" v-model="ingredientData.CarotinB"></td>
							<td><input type="number" class="form-control mb-3" id="ingredientDataVitaminC" v-model="ingredientData.VitaminC"></td>
							<td><input type="number" class="form-control mb-3" id="ingredientDataVitaminD" v-model="ingredientData.VitaminD"></td>
							<td><input type="number" class="form-control mb-3" id="ingredientDataVitaminE" v-model="ingredientData.VitaminE"></td>
							<td><input type="number" class="form-control mb-3" id="ingredientDataVitaminK" v-model="ingredientData.VitaminK"></td>
							<td><input type="number" class="form-control mb-3" id="ingredientDataVitaminB3" v-model="ingredientData.VitaminB3"></td>
							<td><input type="number" class="form-control mb-3" id="ingredientDataVitaminB6" v-model="ingredientData.VitaminB6"></td>
							<td><input type="number" class="form-control mb-3" id="ingredientDataVitaminB12" v-model="ingredientData.VitaminB12"></td>
							<td><input type="number" class="form-control mb-3" id="ingredientDataVitaminB9" v-model="ingredientData.VitaminB9"></td>
							<td><input type="number" class="form-control mb-3" id="ingredientDataCholine" v-model="ingredientData.Choline"></td>
							<td><input type="number" class="form-control mb-3" id="ingredientDataCalcium" v-model="ingredientData.Calcium"></td>
							<td><input type="number" class="form-control mb-3" id="ingredientDataIron" v-model="ingredientData.Iron"></td>
							<td><input type="number" class="form-control mb-3" id="ingredientDataMagnesium" v-model="ingredientData.Magnesium"></td>
							<td><input type="number" class="form-control mb-3" id="ingredientDataPhosphorus" v-model="ingredientData.Phosphorus"></td>
							<td><input type="number" class="form-control mb-3" id="ingredientDataPotassium" v-model="ingredientData.Potassium"></td>
							<td><input type="number" class="form-control mb-3" id="ingredientDataSodium" v-model="ingredientData.Sodium"></td>
							<td><input type="number" class="form-control mb-3" id="ingredientDataZinc" v-model="ingredientData.Zinc"></td>
							<td><input type="number" class="form-control mb-3" id="ingredientDataSelenium" v-model="ingredientData.Selenium"></td>
							<td><input type="number" class="form-control mb-3" id="ingredientDataManganese" v-model="ingredientData.Manganese"></td>
							<td><input type="number" class="form-control mb-3" id="ingredientDataWater" v-model="ingredientData.Water"></td>
						</tr>

						<tr v-for="(ingredient, index) in ingredients">
							<td>
								<a class="text-dark" @click="selectIngredientForPatch(ingredient)"><i class="fas fa-pen"></i></a>
								<a class="text-dark" @click="removeIngredient(ingredient.id, index)"><i class="fas fa-trash"></i></a>
							</td>
							<td>{{ (index + 1) }}</td>
							<td>{{ ingredient.Name }}</td>
							<td>{{ ingredient.translations[2] }}</td>
							<td>{{ ingredient.Calories }}</td>
							<td>{{ ingredient.Protein }}</td>
							<td>{{ ingredient.CarbonHydrates }}</td>
							<td>{{ ingredient.Fats }}</td>
							<td>{{ ingredient.VitaminA }}</td>
							<td>{{ ingredient.CarotinB }}</td>
							<td>{{ ingredient.VitaminC }}</td>
							<td>{{ ingredient.VitaminD }}</td>
							<td>{{ ingredient.VitaminE }}</td>
							<td>{{ ingredient.VitaminK }}</td>
							<td>{{ ingredient.VitaminB3 }}</td>
							<td>{{ ingredient.VitaminB6 }}</td>
							<td>{{ ingredient.VitaminB12 }}</td>
							<td>{{ ingredient.VitaminB9 }}</td>
							<td>{{ ingredient.Choline }}</td>
							<td>{{ ingredient.Calcium }}</td>
							<td>{{ ingredient.Iron }}</td>
							<td>{{ ingredient.Magnesium }}</td>
							<td>{{ ingredient.Phosphorus }}</td>
							<td>{{ ingredient.Potassium }}</td>
							<td>{{ ingredient.Sodium }}</td>
							<td>{{ ingredient.Zinc }}</td>
							<td>{{ ingredient.Selenium }}</td>
							<td>{{ ingredient.Manganese }}</td>
							<td>{{ ingredient.Water }}</td>
						</tr>
						</tbody>
					</table>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import Loader from '../Structure/Loader';

	export default {
		name: 'AdminIngredientList',
		components: {
			Loader
		},
		data: function () {
			return {
				csvFile: null,
				importCount: 0,
				importErrors: 0,
				done: -1,
				ingredients: [],
				createNew: false,
				editIngredient: false,
				ingredientData: {},
				selectedIngredient: null,
				requestsUnsatisfied: 0
			};
		},
		mounted: function () {
			this.getIngredients();
		},
		methods: {
			onFileChange: function (e) {
				let files = e.target.files || e.dataTransfer.files;
				if (!files.length) return;
				let file = files[0];
				let reader = new FileReader();
				reader.onload = (e) => {
					this.csvFile = e.target.result;
					// console.log(this.csvFile);
				};
				reader.readAsText(file);
			},
			importIngredients: function () {
				this.importCount = 0;
				this.importErrors = 0;
				var csvByLine = this.csvFile.split('\n');
				this.done = csvByLine.length - 2;
				for (var i = 1; i < csvByLine.length; i++) {
					let csvLine = csvByLine[i].split(';');
					if (csvLine.length !== 27) continue;

					let floatRegex = /[+-]?\d+(\.\d+)?/g;
					// let textRegex = /[A-Za-z]+/g;
					for (var j = 2; j < csvLine.length; j++) {
						var c = csvLine[j];
						var number = parseFloat(c.match(floatRegex)[0]);
						// var unit = number ? c.match(textRegex)[0] : '';
						// console.log('Num: ' + number + ' Unit: ' + unit);
						csvLine[j] = number.toString();
					}

					let data = {
						Greek: csvLine[0],
						English: csvLine[1],
						Calories: csvLine[2],
						Protein: csvLine[3],
						CarbonHydrates: csvLine[4],
						Fats: csvLine[5],
						VitaminA: csvLine[6],
						CarotinB: csvLine[7],
						VitaminC: csvLine[8],
						VitaminD: csvLine[9],
						VitaminE: csvLine[10],
						VitaminK: csvLine[11],
						VitaminB3: csvLine[12],
						VitaminB6: csvLine[13],
						VitaminB12: csvLine[14],
						VitaminB9: csvLine[15],
						Choline: csvLine[16],
						Calcium: csvLine[17],
						Iron: csvLine[18],
						Magnesium: csvLine[19],
						Phosphorus: csvLine[20],
						Potassium: csvLine[21],
						Sodium: csvLine[22],
						Zinc: csvLine[23],
						Selenium: csvLine[24],
						Manganese: csvLine[25],
						Water: csvLine[26]
					};
					// console.log(csvLine);
					this.$http.post('/api/ingredient/', data)
						.then((response) => {
							this.importCount++;
							this.done--;
							if (!this.done) {
								this.getIngredients();
							}
							// console.log(response);
							this.$notify({
								text: this.$t('Saved successfully!'),
								type: 'success'
							});
						})
						.catch((err) => {
							this.importErrors++;
							this.done--;
							if (!this.done) {
								this.getIngredients();
							}
							console.log(err);
							this.$notify({
								text: this.$t('Something went wrong... Please check your connection.'),
								type: 'error'
							});
						});
				}
			},
			createIngredient: function () {
				this.ingredientData = {
					Greek: '',
					English: '',
					Calories: 0,
					Protein: 0,
					CarbonHydrates: 0,
					Fats: 0,
					VitaminA: 0,
					CarotinB: 0,
					VitaminC: 0,
					VitaminD: 0,
					VitaminE: 0,
					VitaminK: 0,
					VitaminB3: 0,
					VitaminB6: 0,
					VitaminB12: 0,
					VitaminB9: 0,
					Choline: 0,
					Calcium: 0,
					Iron: 0,
					Magnesium: 0,
					Phosphorus: 0,
					Potassium: 0,
					Sodium: 0,
					Zinc: 0,
					Selenium: 0,
					Manganese: 0,
					Water: 0
				};
				this.createNew = true;
			},
			saveNewIngredient: function () {
				this.$http.post('/api/ingredient/', this.ingredientData)
					.then((response) => {
						this.createNew = false;
						this.getIngredients();
						this.$notify({
							text: this.$t('Saved successfully!'),
							type: 'success'
						});
					})
					.catch((err) => {
						console.log(err);
						this.$notify({
							text: this.$t('Something went wrong... Please check your connection.'),
							type: 'error'
						});
					});
			},
			cancelNewIngredient: function () {
				this.createNew = false;
			},
			getIngredients: function () {
				this.requestsUnsatisfied++;
				this.$http.get('/api/ingredient/')
					.then((response) => {
						this.ingredients = Object.values(response.data).sort((a, b) => (a.Name > b.Name) ? 1 : ((b.Name > a.Name) ? -1 : 0));
						this.requestsUnsatisfied--;
					})
					.catch((err) => {
						console.log(err);
						this.$notify({
							text: this.$t('Something went wrong... Please check your connection.'),
							type: 'error'
						});
					});
			},
			removeIngredient: function (id, index) {
				this.$http.delete('/api/ingredient/' + id + '/')
					.then((response) => {
						this.ingredients.splice(index, 1);
						this.$notify({
							text: this.$t('Deleted successfully!'),
							type: 'success'
						});
					})
					.catch((err) => {
						console.log(err);
						this.$notify({
							text: this.$t('Something went wrong... Please check your connection.'),
							type: 'error'
						});
					});
			},
			selectIngredientForPatch: function (ingredient) {
				this.selectedIngredient = ingredient;
				this.ingredientData = {
					English: ingredient.Name || '',
					Greek: ingredient.translations[2] || '',
					Calories: ingredient.Calories,
					Protein: ingredient.Protein,
					CarbonHydrates: ingredient.CarbonHydrates,
					Fats: ingredient.Fats,
					VitaminA: ingredient.VitaminA,
					CarotinB: ingredient.CarotinB,
					VitaminC: ingredient.VitaminC,
					VitaminD: ingredient.VitaminD,
					VitaminE: ingredient.VitaminE,
					VitaminK: ingredient.VitaminK,
					VitaminB3: ingredient.VitaminB3,
					VitaminB6: ingredient.VitaminB6,
					VitaminB12: ingredient.VitaminB12,
					VitaminB9: ingredient.VitaminB9,
					Choline: ingredient.Choline,
					Calcium: ingredient.Calcium,
					Iron: ingredient.Iron,
					Magnesium: ingredient.Magnesium,
					Phosphorus: ingredient.Phosphorus,
					Potassium: ingredient.Potassium,
					Sodium: ingredient.Sodium,
					Zinc: ingredient.Zinc,
					Selenium: ingredient.Selenium,
					Manganese: ingredient.Manganese,
					Water: ingredient.Water
				};
				this.editIngredient = true;
			},
			patchIngredient: function () {
				this.$http.put('/api/ingredient/' + this.selectedIngredient.id + '/', this.ingredientData)
					.then((response) => {
						// this.ingredients.splice(index, 1);
						this.editIngredient = false;
						this.getIngredients();
						this.$notify({
							text: this.$t('Saved successfully!'),
							type: 'success'
						});
					})
					.catch((err) => {
						console.log(err);
						this.$notify({
							text: this.$t('Something went wrong... Please check your connection.'),
							type: 'error'
						});
					});
			},
			cancelPatchIngredient: function () {
				this.editIngredient = false;
			}
		}
	};
</script>

<style scoped>
	input[type="number"]::-webkit-outer-spin-button, input[type="number"]::-webkit-inner-spin-button {
		-webkit-appearance: none;
		margin: 0;
	}

	input[type="number"] {
		-moz-appearance: textfield;
	}

	input[type="text"] {
		min-width: 10rem;
	}

	th {
		min-width: 5rem;
	}
</style>
