<template>
	<div id="AdminArticleEditAccordion">
		<div class="card mb-1" v-for="(article, index) in articleData['Translations']">
			<div class="card-header" :id="'heading' + index">
				<h5 class="mb-0">
					<button class="btn btn-link" data-toggle="collapse" :data-target="'#collapse' + index" aria-expanded="false" :aria-controls="'collapse' + index">
						{{ $root.languages[article.Language].Name }}
					</button>
					<button type="button" class="align-middle float-right btn btn-sm bg-danger text-white" @click="removeTranslation(index)">
						<i class="fas fa-trash"></i>
						{{ $t('Delete') }}
					</button>
					<!--<button type="button" class="align-middle float-right btn btn-sm bgGreen0 text-white mr-1" @click="saveTranslation()">-->
					<!--<i class="fas fa-save"></i>-->
					<!--{{ $t('Save') }}-->
					<!--</button>-->
				</h5>
			</div>

			<div :id="'collapse' + index" class="collapse" :aria-labelledby="'heading' + index" data-parent="#AdminArticleEditAccordion">
				<div class="card-body">
					<ArticleForm :article="article"/>
				</div>
			</div>
		</div>
		<button type="button" class="btn btn-primary" @click="addTranslation()"><i class="fas fa-plus"></i> {{ $t('Add Language') }}</button>

		<div v-if="articleData['ArticleTypeId'] === 1">
			<hr>

			<div class="row">
				<label id="YoutubeLinkInput" class="label col-12">Youtube Link:
					<input type="text" class="form-control" id="YoutubeLink" placeholder="YouTube Link" v-model="articleData['YoutubeLink']">
				</label>

				<label id="DishesInput" class="label col-sm-6">{{ $t('Dishes') }}:
					<input type="number" class="form-control" id="Dishes" :placeholder="$t('Dishes')" v-model="articleData['Dishes']">
				</label>

				<label id="ReadyInInput" class="label col-sm-6">{{ $t('Ready in') }} (minutes):
					<input type="number" class="form-control" id="ReadyIn" :placeholder="$t('Ready in')" v-model="articleData['ReadyIn']">
				</label>
			</div>

			<fieldset id="IngredientsInput" class="form-group" v-if="ingredients">
				<div class="row">
					<label class="label col-12">{{ $t('Ingredients') }}:</label>
					<div class="col-12">
						<table class="table text-center" v-if="ingredients.length!==0">
							<thead>
							<tr>
								<th scope="col">{{ $t('Ingredient') }}</th>
								<th scope="col">{{ $t('Quantity') }}</th>
								<th scope="col">{{ $t('Main Ingredient') }}</th>
								<th scope="col">{{ $t('Delete') }}</th>
							</tr>
							</thead>
							<tbody>
							<tr v-for="(ingredient, index) in articleData['Ingredients']">
								<td>{{ ingredients[ingredient.Ingredient].Name }}</td>
								<td>{{ ingredient['Quantity'] }}</td>
								<td>
									<div class="form-check form-check-inline">
										<input @change="setMainIngredient(ingredient)" v-model="ingredient['IsMainIngredient']" :aria-label="$t('Main Ingredient')" class="form-check-input" type="checkbox">
									</div>
								</td>
								<td>
									<a class="text-dark ml-2" @click="removeIngredient(index)"><i class="fas fa-trash"></i></a>
								</td>
							</tr>
							</tbody>
						</table>
						<div class="row">
							<label class="label col-md-4 col-lg-4">
								<select class="custom-select" id="IngredientSelect" v-model="selectedIngredient">
									<option v-for="ingredient in ingredientsSorted" :value="ingredient">{{ ingredient.Name }}</option>
								</select>
							</label>
							<label class="label col-md-3 col-lg-3">
								<input type="number" class="form-control" id="IngredientQuantity" :placeholder="$t('Quantity')" v-model="selectedQuantity">
							</label>
							<label class="label col-md-5 col-lg-3">
								<input class="form-check form-check-inline" type="checkbox" v-model="isMainIngredient">
								{{ $t('Main Ingredient') }}
							</label>
							<div class="col-lg-2">
								<button class="btn bgGreen0 text-white" @click="addIngredient()"><i class="fas fa-plus"></i> {{ $t('Add') }}</button>
							</div>
						</div>
					</div>
				</div>
			</fieldset>
		</div>
	</div>
</template>

<script>
	import ArticleForm from './ArticleForm';

	export default {
		name: 'AdminArticleAccordion',
		components: {
			ArticleForm
		},
		props: ['articleData'],
		data: function () {
			return {
				ingredients: {},
				selectedIngredient: {},
				selectedQuantity: 0,
				isMainIngredient: false
			};
		},
		mounted: function () {
			// if (this.articleData['ArticleTypeId'] === 1) this.getIngredients();
			this.getIngredients();
		},
		methods: {
			getIngredients: function () {
				// this.requestsUnsatisfied++;
				this.$http.get('/api/ingredient/?locale=' + this.$cookie.get('locale'))
					.then(response => {
						this.ingredients = response.data;
						this.selectedIngredient = this.ingredientsSorted[0];
						// this.requestsUnsatisfied--;
					})
					.catch(this.$root.notifyAction.error);
			},
			addIngredient: function () {
				const data = {
					Quantity: this.selectedQuantity,
					IsMainIngredient: this.isMainIngredient,
					Article: this.articleData.id,
					Ingredient: this.selectedIngredient.id
				};
				this.$http.post('/api/ingredientAssociation/', data)
					.then(response => {
						this.articleData['Ingredients'].push(response.data);
						this.$root.notifyAction.success();
					})
					.catch(this.$root.notifyAction.error);
			},
			removeIngredient: function (index) {
				this.$http.delete('/api/ingredientAssociation/' + this.articleData['Ingredients'][index]['id'] + '/')
					.then(response => {
						this.articleData['Ingredients'].splice(index, 1);
						this.$notify({
							text: this.$t('Deleted successfully!'),
							type: 'success'
						});
					})
					.catch(this.$root.notifyAction.error);
			},
			setMainIngredient: function (ingredient) {
				this.$http.put('/api/ingredientAssociation/' + ingredient.id + '/', Object.assign({}, ingredient, {'Article': this.articleData.id}))
					.then(response => {
						this.$root.notifyAction.success();
					})
					.catch(this.$root.notifyAction.error);
			},
			removeTranslation: function (index) {
				this.$http.delete('/api/articleContentTranslation/' + this.articleData['Translations'][index]['id'] + '/')
					.then(response => {
						this.articleData['Translations'].splice(index, 1);
						this.$notify({
							text: this.$t('Deleted successfully!'),
							type: 'success'
						});
					})
					.catch(this.$root.notifyAction.error);
			},
			addTranslation: function () {
				this.articleData['Translations'].push({
					AuthorName: '',
					AuthorProfession: '',
					AuthorProfilePicture: {
						name: '',
						data: ''
					},
					Content: '',
					DoneEditing: false,
					Language: 1,
					OnCarousel: false,
					ReleaseDateTime: {
						data: '',
						time: ''
					},
					Thumbnail: {
						name: '',
						data: ''
					},
					Title: '',
					id: -1
				});
			}
		},
		computed: {
			ingredientsSorted: function () {
				return Object.values(this.ingredients).sort((a, b) => (a.Name > b.Name) ? 1 : ((b.Name > a.Name) ? -1 : 0));
			}
		}
	};
</script>

<style scoped>

</style>
