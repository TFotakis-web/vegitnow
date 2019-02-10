<template>
	<div id="CreateArticleComponent" class="mb-5 h-100">
		<div class="navbar-placeholder"></div>
		<div id="createArticle" class="container mb-5">
			<h1 class="text-center">{{ $t('Create Article') }}</h1>
			<div class="input-group mb-3" style="width: fit-content">
				<div class="input-group-prepend">
					<label class="input-group-text" for="selectArticleType">{{ $t('Create a new') }}</label>
				</div>
				<select class="custom-select" id="selectArticleType" v-model="data.articleType">
					<option v-for="articleType in articleTypes" :value="articleType.id">{{ articleType.Name }}</option>
				</select>
			</div>

			<form class="pb-3" v-for="(article, index) in data.translations">
				<div class="form-group row">
					<label for="ArticleLanguage" class="col-sm-2 col-form-label">{{ $t('Select Language') }}:</label>
					<div class="col-sm-10">
						<select class="custom-select" id="ArticleLanguage" v-model="article.language">
							<option v-for="language in languages" :value="language.id">{{ language.Name }}</option>
						</select>
					</div>
				</div>

				<div class="form-group row">
					<label for="ArticleTitle" class="col-sm-2 col-form-label">{{ $t('Title') }}:</label>
					<div class="col-sm-10">
						<input type="text" class="form-control" id="ArticleTitle" :placeholder="$t('Title')" v-model="article.title">
					</div>
				</div>

				<div class="form-group row">
					<label class="col-sm-2 col-form-label">{{ $t('Thumbnail') }}:</label>
					<div class="col-sm-10">
						<div class="custom-file">
							<label class="custom-file-label" :for="'ArticleThumbnail' + index">{{ $t('Choose file') }}</label>
							<input type="file" class="custom-file-input" :id="'ArticleThumbnail' + index" @change="onFileChange($event, article)">
						</div>
					</div>
				</div>

				<div class="form-group row">
					<div class="col-sm-2">
						<label>{{ $t('Content') }}:</label>
					</div>
					<div class="col-sm-10">
						<Summernote height="400" :model="article.content" v-on:change="value => { article.content = value }"></Summernote>
					</div>
				</div>

				<div class="form-group row">
					<label for="ArticleReleaseDate" class="col-sm-2 col-form-label">{{ $t('Release Date') }}:</label>
					<div class="col-sm-10">
						<div class="row">
							<div class="col">
								<input type="text" class="form-control mb-3" id="ArticleReleaseDate" :placeholder="$t('Date') + ' (dd/mm/yyyy)'" v-model="article.releaseDateTime.date">
							</div>
							<div class="col">
								<input type="text" class="form-control" id="ArticleReleaseTime" :placeholder="$t('Time') + ' (HH:MM)'" v-model="article.releaseDateTime.time">
							</div>
						</div>
					</div>
				</div>

				<div class="form-check row">
					<div class="col">
						<input type="checkbox" :id="'ArticleMarkDoneEditing' + index" class="form-check-input" v-model="article.doneEditing">
						<label class="form-check-label" :for="'ArticleMarkDoneEditing' + index">{{ $t('Mark as Done Editing') }}</label>
					</div>
				</div>

				<div class="form-group row">
					<div class="col">
						<button type="button" class="btn bgGreen0 text-white" @click="deleteLanguage(index)"><i class="fas fa-trash"></i> {{ $t('Delete') }}</button>
					</div>
				</div>
			</form>

			<div class="form-group row">
				<div class="col">
					<button type="button" class="btn bgGreen0 text-white" @click="addInitializedTranslation()"><i class="fas fa-plus"></i> {{ $t('Add Language') }}</button>
				</div>
			</div>

			<hr class="my-5" v-if="data.articleType === 1">

			<div class="form-group row" v-if="data.articleType === 1">
				<label for="YoutubeLink" class="col-sm-2 col-form-label">Youtube Link:</label>
				<div class="col-sm-10">
					<div class="row">
						<div class="col">
							<input type="text" class="form-control mb-3" id="YoutubeLink" placeholder="YouTube Link" v-model="youtubeLink">
						</div>
					</div>
				</div>
			</div>

			<div class="form-group row" v-if="data.articleType === 1">
				<label for="Dishes" class="col-sm-2 col-form-label">{{ $t('Dishes') }}:</label>
				<div class="col-sm-10">
					<div class="row">
						<div class="col">
							<input type="number" class="form-control mb-3" id="Dishes" :placeholder="$t('Dishes')" v-model="dishes">
						</div>
					</div>
				</div>
			</div>

			<fieldset class="form-group" v-if="data.articleType === 1">
				<div class="row">
					<label class="col-form-label col-sm-2 pt-0">{{ $t('Ingredients') }}:</label>
					<div class="col-sm-10">
						<table class="table text-center" v-if="ingredients.length!==0">
							<thead>
							<tr>
								<th scope="col">{{ $t('Ingredient') }}</th>
								<th scope="col">{{ $t('Quantity') }}</th>
								<th scope="col">{{ $t('Unit') }}</th>
								<th scope="col">{{ $t('Main Ingredient') }}</th>
								<th scope="col">{{ $t('Delete') }}</th>
							</tr>
							</thead>
							<tbody>
							<tr v-for="(ingredient, index) in data.ingredients">
								<td>{{ ingredient.ingredient.Name }}</td>
								<td>{{ ingredient.quantity }}</td>
								<td>{{ ingredient.ingredient.Unit }}</td>
								<td>
									<div class="form-check form-check-inline">
										<input class="form-check-input" type="checkbox" v-model="ingredient.isMainIngredient" :id="'isMainIngredientCheckbox' + index">
									</div>
								</td>
								<td>
									<a class="text-dark ml-2" @click="removeSelectedIngredient(index)"><i class="fas fa-trash"></i></a>
								</td>
							</tr>
							</tbody>
						</table>
						<div class="input-group mb-3">
							<select class="custom-select" id="IngredientSelect" v-model="selectedIngredient">
								<option v-for="ingredient in ingredients" :value="ingredient">{{ ingredient.Name }}</option>
							</select>
							<input type="number" class="form-control" id="IngredientQuantity" :placeholder="$t('Quantity')" v-model="selectedQuantity">
							<div class="input-group-append">
								<label class="input-group-text" for="selectArticleType" style="width: 10em">{{ selectedIngredient.Unit }}</label>
							</div>
							<div class="btn bgGreen0 text-white ml-2" @click="selectIngredient()"><i class="fas fa-plus"></i> Add</div>
						</div>
					</div>
				</div>
			</fieldset>

			<hr class="my-5">

			<div class="form-group row">
				<div class="col text-right">
					<button type="button" class="btn bgGreen0 text-white" @click="saveArticle()"><i class="fas fa-save"></i> {{ $t('Save') }}</button>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import Summernote from './Summernote';

	export default {
		name: 'CreateArticle',
		components: {
			Summernote
		},
		data: function () {
			return {
				languages: [],
				articleTypes: [],
				ingredients: [],
				selectedIngredient: {},
				selectedQuantity: 0,
				data: {
					articleType: 0,
					translations: []
				},
				image: null,
				selectedIngredients: [],
				dishes: 0,
				youtubeLink: ''
			};
		},
		mounted: function () {
			this.addTranslation();
			this.getArticleTypes();
			this.getLanguages();
			this.getIngredients();
		},
		methods: {
			getLanguages: function () {
				this.$http.get('/api/language/')
					.then((response) => {
						this.languages = response.data;
						this.initTranslationLanguage(this.data.translations[0]);
					})
					.catch((err) => {
						console.log(err);
					});
			},
			getArticleTypes: function () {
				this.$http.get('/api/articleType/')
					.then((response) => {
						this.articleTypes = response.data;
						this.data.articleType = this.articleTypes[0].id;
					})
					.catch((err) => {
						console.log(err);
					});
			},
			getIngredients: function () {
				this.$http.get('/api/ingredient/')
					.then((response) => {
						this.ingredients = response.data;
						this.selectedIngredient = this.ingredients[0];
					})
					.catch((err) => {
						console.log(err);
					});
				// this.ingredients = [
				// 	{id: 1, Name: 'Fava', Unit: 'gr'},
				// 	{id: 2, Name: 'Fakies', Unit: 'gr'},
				// 	{id: 3, Name: 'Ntomata', Unit: 'pcs'},
				// 	{id: 4, Name: 'Aggouri', Unit: 'pcs'}
				// ];
			},
			addTranslation: function () {
				this.data.translations.push({
					language: null,
					title: null,
					content: '',
					thumbnail: null,
					releaseDateTime: {
						date: null,
						time: null
					},
					doneEditing: false
				});

				$('#ArticleContent').summernote({
					placeholder: 'Article content...',
					tabsize: 2,
					height: 300
				});
			},
			addInitializedTranslation: function () {
				this.addTranslation();
				this.initTranslation(this.data.translations[this.data.translations.length - 1]);
			},
			initTranslation: function (translation) {
				this.initTranslationLanguage(translation);
			},
			initTranslationLanguage: function (translation) {
				translation.language = this.languages[0].id;
			},
			deleteLanguage: function (index) {
				this.data.translations.splice(index, 1);
			},
			onFileChange: function (e, article) {
				var files = e.target.files || e.dataTransfer.files;
				if (!files.length) return;
				// this.createImage(files[0], article);
				var file = files[0];
				var reader = new FileReader();

				reader.onload = (e) => {
					article.thumbnail = e.target.result;
				};
				reader.readAsDataURL(file);
			},
			selectIngredient: function () {
				this.selectedIngredients.push({
					ingredient: this.selectedIngredient,
					isMainIngredient: false,
					quantity: this.selectedQuantity
				});
			},
			removeSelectedIngredient: function (index) {
				this.data.ingredients.splice(index, 1);
			},
			saveArticle: function () {
				if (this.data.articleType === 1) {
					this.data.ingredients = this.selectedIngredients;
					this.data.dishes = this.dishes;
					if (this.youtubeLink !== '') this.data.youtubeLink = this.youtubeLink;
				}
				this.$http.post('/api/newArticle/', this.data)
					.then((response) => {
						console.log(response);
					})
					.catch((err) => {
						console.log(err);
					});
			}
			// ,
			// 	getArticles: function () {
			// 		this.loading = true;
			// 		this.$http.get('/api/article/')
			// 			.then((response) => {
			// 				this.articles = response.data;
			// 				this.loading = false;
			// 			})
			// 			.catch((err) => {
			// 				this.loading = false;
			// 				console.log(err);
			// 			});
			// 	},
			// 	getArticle: function (id) {
			// 		this.loading = true;
			// 		this.$http.get('/api/article/' + id + '/', id)
			// 			.then((response) => {
			// 				this.currentArticle = {
			// 					'id': response.data.id,
			// 					'User': response.data.User,
			// 					'UploadDateTime': response.data.UploadDateTime
			// 				};
			//
			// 				// $("#editArticleModal").modal('show');
			// 				this.loading = false;
			// 			})
			// 			.catch((err) => {
			// 				this.loading = false;
			// 				console.log(err);
			// 			});
			// 	},
			// 	addArticle: function () {
			// 		this.loading = true;
			// 		this.$http.post('/api/article/', this.newArticle)
			// 			.then((response) => {
			// 				this.loading = false;
			// 				this.getArticles();
			// 			})
			// 			.catch((err) => {
			// 				this.loading = false;
			// 				console.log(err);
			// 			});
			// 	},
			// 	updateArticle: function () {
			// 		this.loading = true;
			// 		var updatedArticle = {
			// 			'id': this.currentArticle.id,
			// 			'User': this.currentArticle.User,
			// 			'UploadDateTime': this.currentArticle.UploadDateTime
			// 		};
			// 		console.log(updatedArticle);
			// 		this.$http.put('/api/article/' + this.currentArticle.id + '/', updatedArticle)
			// 			.then((response) => {
			// 				this.loading = false;
			// 				this.currentArticle = response.data;
			// 				this.getArticles();
			// 			})
			// 			.catch((err) => {
			// 				this.loading = false;
			// 				console.log(err);
			// 			});
			// 	},
			// 	deleteArticle: function (id) {
			// 		this.loading = true;
			// 		this.$http.delete('/api/article/' + id + '/')
			// 			.then((response) => {
			// 				this.loading = false;
			// 				this.getArticles();
			// 			})
			// 			.catch((err) => {
			// 				this.loading = false;
			// 				console.log(err);
			// 			});
			// 	}
		}
	};
</script>

<style scoped>

</style>
