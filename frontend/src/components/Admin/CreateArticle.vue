<template>
	<div id="CreateArticleComponent" class="mb-5 h-100 w-100">
		<!--<div class="navbar-placeholder"></div>-->
		<div id="createArticle" class="container mb-5">
			<!--<h1 class="text-center">{{ $t('Create Article') }}</h1>-->
			<div id="ArticleTypeInput" class="input-group mb-3" style="width: fit-content">
				<div class="input-group-prepend">
					<label class="input-group-text" for="selectArticleType">{{ $t('Create a new') }}</label>
				</div>
				<select class="custom-select" id="selectArticleType" v-model="data.articleType">
					<option v-for="articleType in articleTypes" :value="articleType.id">{{ articleType.Name }}</option>
				</select>
			</div>

			<form id="ArticleTranslations" class="pb-3" v-for="(article, index) in data.translations">
				<div :id="'ArticleLanguageInput' + index" class="form-group row">
					<label for="ArticleLanguage" class="col-sm-2 col-form-label">{{ $t('Select Language') }}:</label>
					<div class="col-sm-10">
						<select class="custom-select" id="ArticleLanguage" v-model="article.language">
							<option v-for="language in languages" :value="language.id">{{ language.Name }}</option>
						</select>
					</div>
				</div>

				<div :id="'ArticleTitleInput' + index" class="form-group row">
					<label for="ArticleTitle" class="col-sm-2 col-form-label">{{ $t('Title') }}:</label>
					<div class="col-sm-10">
						<input type="text" class="form-control" id="ArticleTitle" :placeholder="$t('Title')" v-model="article.title">
					</div>
				</div>

				<!--<div :id="'ArticlePreviewInput' + index" v-if="data.articleType === 2" class="form-group row">-->
					<!--<label for="ArticlePreview" class="col-sm-2 col-form-label">Preview</label>-->
					<!--<div class="col-sm-10">-->
						<!--<input type="text" class="form-control" id="ArticlePreview" placeholder="Preview" v-model="article.preview">-->
					<!--</div>-->
				<!--</div>-->

				<div v-if="data.articleType === 2">
					<div :id="'ArticleAuthorNameInput' + index" class="form-group row">
						<label for="AuthorName" class="col-sm-2 col-form-label">Author Name:</label>
						<div class="col-sm-10">
							<input type="text" class="form-control" id="AuthorName" placeholder="Author Name" v-model="article.authorName">
						</div>
					</div>

					<div :id="'ArticleAuthorProfessionInput' + index" class="form-group row">
						<label for="AuthorProfession" class="col-sm-2 col-form-label">Author Profession:</label>
						<div class="col-sm-10">
							<input type="text" class="form-control" id="AuthorProfession" placeholder="Author Profession" v-model="article.authorProfession">
						</div>
					</div>
				</div>

				<div :id="'ArticleThumbnailInput' + index" class="form-group row">
					<label class="col-sm-2 col-form-label">{{ $t('Thumbnail') }}:</label>
					<div class="col-sm-10">
						<div class="custom-file">
							<label class="custom-file-label" :for="'ArticleThumbnail' + index">{{ $t('Choose file') }}</label>
							<input type="file" class="custom-file-input" :id="'ArticleThumbnail' + index" @change="onFileChange($event, article)">
						</div>
					</div>
				</div>

				<div :id="'ArticleContentInput' + index" class="form-group row">
					<div class="col-sm-2">
						<label>{{ $t('Content') }}:</label>
					</div>
					<div class="col-sm-10">
						<Summernote height="400" :model="article.content" v-on:change="value => { article.content = value }"></Summernote>
					</div>
				</div>

				<div :id="'ArticleReleaseDateTimeInput' + index" class="form-group row">
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

				<div :id="'ArticleMarkDoneEditing' + index" class="form-check row">
					<div class="col">
						<input type="checkbox" :id="'ArticleMarkDoneEditing' + index" class="form-check-input" v-model="article.doneEditing">
						<label class="form-check-label" :for="'ArticleMarkDoneEditing' + index">{{ $t('Mark as Done Editing') }}</label>
					</div>
				</div>

				<div :id="'ArticleDeleteTranslationInput' + index" class="form-group row">
					<div class="col">
						<button type="button" class="btn bgGreen0 text-white" @click="deleteLanguage(index)"><i class="fas fa-trash"></i> {{ $t('Delete') }}</button>
					</div>
				</div>
			</form>

			<div id="AddLanguageInput" class="form-group row">
				<div class="col">
					<button type="button" class="btn bgGreen0 text-white" @click="addInitializedTranslation()"><i class="fas fa-plus"></i> {{ $t('Add Language') }}</button>
				</div>
			</div>

			<div v-if="data.articleType === 1">
				<hr class="my-5">

				<div id="YoutubeLinkInput" class="form-group row">
					<label for="YoutubeLink" class="col-sm-2 col-form-label">Youtube Link:</label>
					<div class="col-sm-10">
						<div class="row">
							<div class="col">
								<input type="text" class="form-control mb-3" id="YoutubeLink" placeholder="YouTube Link" v-model="youtubeLink">
							</div>
						</div>
					</div>
				</div>

				<div id="DishesInput" class="form-group row">
					<label for="Dishes" class="col-sm-2 col-form-label">{{ $t('Dishes') }}:</label>
					<div class="col-sm-10">
						<div class="row">
							<div class="col">
								<input type="number" class="form-control mb-3" id="Dishes" :placeholder="$t('Dishes')" v-model="dishes">
							</div>
						</div>
					</div>
				</div>

				<div id="ReadyInInput" class="form-group row">
					<label for="ReadyIn" class="col-sm-2 col-form-label">{{ $t('Ready in') }} (minutes):</label>
					<div class="col-sm-10">
						<div class="row">
							<div class="col">
								<input type="number" class="form-control mb-3" id="ReadyIn" :placeholder="$t('Ready in')" v-model="readyIn">
							</div>
						</div>
					</div>
				</div>

				<fieldset id="IngredientsInput" class="form-group">
					<div class="row">
						<label class="col-form-label col-sm-2 pt-0">{{ $t('Ingredients') }}:</label>
						<div class="col-sm-10">
							<table class="table text-center" v-if="ingredients.length!==0">
								<thead>
								<tr>
									<th scope="col">{{ $t('Ingredient') }}</th>
									<th scope="col">{{ $t('Quantity') }}</th>
									<!--<th scope="col">{{ $t('Unit') }}</th>-->
									<th scope="col">{{ $t('Main Ingredient') }}</th>
									<th scope="col">{{ $t('Delete') }}</th>
								</tr>
								</thead>
								<tbody>
								<tr v-for="(ingredient, index) in selectedIngredients">
									<td>{{ ingredient.ingredient.Name }}</td>
									<td>{{ ingredient.quantity }}</td>
									<!--<td>{{ ingredient.ingredient.Unit }}</td>-->
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
								<!--<div class="input-group-append">-->
								<!--<label class="input-group-text" for="selectArticleType" style="width: 10em">{{ selectedIngredient.Unit }}</label>-->
								<!--</div>-->
								<div class="btn bgGreen0 text-white ml-2" @click="selectIngredient()"><i class="fas fa-plus"></i> Add</div>
							</div>
						</div>
					</div>
				</fieldset>
			</div>
			<hr class="my-5">

			<div id="SaveInput" class="form-group row">
				<div class="col text-right">
					<button type="button" class="btn bgGreen0 text-white" @click="saveArticle()"><i class="fas fa-save"></i> {{ $t('Save') }}</button>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import Summernote from '../Various/Summernote';

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
				readyIn: 0,
				youtubeLink: '',
				authorName: '',
				authorProfession: ''
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
			},
			addTranslation: function () {
				this.data.translations.push({
					language: null,
					title: null,
					// preview: null,
					content: '',
					thumbnail: null,
					releaseDateTime: {
						date: null,
						time: null
					},
					doneEditing: false,
					authorName: '',
					authorProfession: ''
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
				this.selectedIngredients.splice(index, 1);
			},
			saveArticle: function () {
				var data = Object.assign({}, this.data);
				if (this.data.articleType === 1) {
					data.ingredients = [];
					this.selectedIngredients.forEach(function (ingredient) {
						data.ingredients.push({
							ingredientId: ingredient.ingredient.id,
							isMainIngredient: ingredient.isMainIngredient,
							quantity: ingredient.quantity
						});
					});
					// data.ingredients = this.selectedIngredients;
					data.dishes = this.dishes;
					data.readyIn = this.readyIn;
					data.youtubeLink = this.youtubeLink;
				}
				// console.log(data);
				this.$http.post('/api/newArticle/', data)
					.then((response) => {
						console.log(response);
					})
					.catch((err) => {
						console.log(err);
					});
			}
		}
	};
</script>

<style scoped>

</style>
