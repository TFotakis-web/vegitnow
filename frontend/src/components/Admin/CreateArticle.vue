<template>
	<div id="CreateArticleComponent" class="d-flex flex-grow-1">
		<Loader v-if="requestsUnsatisfied"/>
		<div id="createArticle" v-if="!requestsUnsatisfied" class="container mb-5">
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
					<label for="ArticleLanguage" class="col-md-2 col-form-label">{{ $t('Select Language') }}:</label>
					<div class="col-md-10">
						<select class="custom-select" id="ArticleLanguage" v-model="article.language">
							<option v-for="language in $root.languages" :value="language.id">{{ language.Name }}</option>
						</select>
					</div>
				</div>

				<div :id="'ArticleTitleInput' + index" class="form-group row">
					<label for="ArticleTitle" class="col-md-2 col-form-label">{{ $t('Title') }}:</label>
					<div class="col-md-10">
						<input type="text" class="form-control" id="ArticleTitle" :placeholder="$t('Title')" v-model="article.title">
					</div>
				</div>

				<div v-if="data.articleType === 2">
					<div :id="'PreviewInput' + index" class="form-group row">
						<label for="Preview" class="col-md-2 col-form-label">Preview:</label>
						<div class="col-md-10">
							<input type="text" class="form-control" id="Preview" placeholder="Preview" v-model="article.preview">
						</div>
					</div>

					<div :id="'ArticleAuthorNameInput' + index" class="form-group row">
						<label for="AuthorName" class="col-md-2 col-form-label">Author Name:</label>
						<div class="col-md-10">
							<input type="text" class="form-control" id="AuthorName" placeholder="Author Name" v-model="article.authorName">
						</div>
					</div>

					<div :id="'ArticleAuthorProfessionInput' + index" class="form-group row">
						<label for="AuthorProfession" class="col-md-2 col-form-label">Author Profession:</label>
						<div class="col-md-10">
							<input type="text" class="form-control" id="AuthorProfession" placeholder="Author Profession" v-model="article.authorProfession">
						</div>
					</div>

					<div :id="'AuthorProfilePictureInput' + index" class="form-group row">
						<label class="col-md-2 col-form-label">{{ $t('Author Profile Picture') }}:</label>
						<div class="col-md-10">
							<ImageInput :obj="article.authorProfilePicture"/>
						</div>
					</div>
				</div>

				<div :id="'ArticleThumbnailInput' + index" class="form-group row">
					<label class="col-md-2 col-form-label">{{ $t('Thumbnail') }}:</label>
					<div class="col-md-10">
						<ImageInput :obj="article.thumbnail"/>
					</div>
				</div>

				<div :id="'ArticleContentInput' + index" class="form-group row">
					<div class="col-md-2">
						<label>{{ $t('Content') }}:</label>
					</div>
					<div class="col-md-10">
						<Summernote height="400" :model="article.content" v-on:change="value => { article.content = value }"></Summernote>
						<!-- <TipTap :value="article.content" v-on:input="value => { article.content = value }"/>-->
					</div>
				</div>

				<div :id="'ArticleReleaseDateTimeInput' + index" class="form-group row">
					<label for="ArticleReleaseDate" class="col-md-2 col-form-label">{{ $t('Release Date') }}:</label>
					<div class="col-md-10">
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

				<div :id="'ArticleOnCarouselInput' + index" class="form-check row">
					<div class="col">
						<input type="checkbox" :id="'ArticleOnCarousel' + index" class="form-check-input" v-model="article.onCarousel">
						<label class="form-check-label" :for="'ArticleOnCarousel' + index">{{ $t('Available on carousel') }}</label>
					</div>
				</div>

				<div :id="'ArticleMarkDoneEditingInput' + index" class="form-check row">
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
					<label for="YoutubeLink" class="col-md-2 col-form-label">Youtube Link:</label>
					<div class="col-md-10">
						<div class="row">
							<div class="col">
								<input type="text" class="form-control mb-3" id="YoutubeLink" placeholder="YouTube Link" v-model="youtubeLink">
							</div>
						</div>
					</div>
				</div>

				<div id="DishesInput" class="form-group row">
					<label for="Dishes" class="col-md-2 col-form-label">{{ $t('Dishes') }}:</label>
					<div class="col-md-10">
						<div class="row">
							<div class="col">
								<input type="number" class="form-control mb-3" id="Dishes" :placeholder="$t('Dishes')" v-model="dishes">
							</div>
						</div>
					</div>
				</div>

				<div id="ReadyInInput" class="form-group row">
					<label for="ReadyIn" class="col-md-2 col-form-label">{{ $t('Cooking') }}:</label>
					<div class="col-md-10">
						<div class="row">
							<div class="col">
								<input type="number" class="form-control mb-3" id="ReadyIn" :placeholder="$t('Min')" v-model="cooking">
							</div>
						</div>
					</div>
				</div>

				<div id="PreparationInput" class="form-group row">
					<label for="Preparation" class="col-md-2 col-form-label">{{ $t('Preparation') }}:</label>
					<div class="col-md-10">
						<div class="row">
							<div class="col">
								<input type="number" class="form-control mb-3" id="Preparation" :placeholder="$t('Min')" v-model="preparation">
							</div>
						</div>
					</div>
				</div>

				<div id="WaitingInput" class="form-group row">
					<label for="Waiting" class="col-md-2 col-form-label">{{ $t('Waiting')}}:</label>
					<div class="col-md-10">
						<div class="row">
							<div class="col">
								<input type="number" class="form-control mb-3" id="Waiting" :placeholder="$t('Min')" v-model="waiting">
							</div>
						</div>
					</div>
				</div>

				<fieldset id="IngredientsInput" class="form-group">
					<div class="row">
						<label class="col-form-label col-md-2 pt-0">{{ $t('Ingredients') }}:</label>
						<div class="col-md-10">
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
								<tr v-for="(ingredient, index) in selectedIngredients">
									<td>{{ ingredient.ingredient.Name }}</td>
									<td>{{ ingredient.quantity }}</td>
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
									<option v-for="ingredient in ingredientsSorted" :value="ingredient">{{ ingredient.Name }}</option>
								</select>
								<input type="number" class="form-control" id="IngredientQuantity" :placeholder="$t('Quantity')" v-model="selectedQuantity">
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
	import Loader from '../Structure/Loader';
	import ImageInput from '../Structure/ImageInput';
	import Summernote from '../Structure/Summernote';
	// import TipTap from '../Structure/TipTap';

	export default {
		name: 'CreateArticle',
		components: {
			Loader,
			ImageInput,
			Summernote
			// TipTap
		},
		data: function () {
			return {
				articleTypes: [],
				ingredients: {},
				selectedIngredient: {},
				selectedQuantity: 0,
				data: {
					articleType: 0,
					translations: []
				},
				image: null,
				selectedIngredients: [],
				dishes: null,
				cooking: null,
				preparation: null,
				waiting: null,
				youtubeLink: '',
				authorName: '',
				authorProfession: '',
				requestsUnsatisfied: 0
			};
		},
		mounted: function () {
			this.addInitializedTranslation();
			this.getArticleTypes();
			this.getIngredients();
		},
		methods: {
			getArticleTypes: function () {
				this.requestsUnsatisfied++;
				this.$http.get('/api/articleType/')
					.then(response => {
						this.articleTypes = response.data;
						this.data.articleType = this.articleTypes[0].id;
						this.requestsUnsatisfied--;
					})
					.catch(this.$root.notifyAction.error);
			},
			getIngredients: function () {
				this.requestsUnsatisfied++;
				this.$http.get('/api/ingredient/?locale=' + this.$cookie.get('locale'))
					.then(response => {
						this.ingredients = response.data;
						this.selectedIngredient = this.ingredientsSorted[0];
						this.requestsUnsatisfied--;
					})
					.catch(this.$root.notifyAction.error);
			},
			addTranslation: function () {
				this.data.translations.push({
					language: null,
					title: null,
					content: '',
					preview: '',
					thumbnail: {
						name: '',
						data: ''
					},
					authorProfilePicture: {
						name: '',
						data: ''
					},
					releaseDateTime: {
						date: null,
						time: null
					},
					onCarousel: false,
					doneEditing: false,
					authorName: '',
					authorProfession: ''
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
				// translation.language = Object.keys(this.$root.languages)[0];
				translation.language = '1';
			},
			initArticleFields: function () {
				this.selectedIngredient = {};
				this.selectedQuantity = 0;
				this.$set(this.data, 'articleType', 0);
				this.$set(this.data, 'translations', []);
				this.image = null;
				this.selectedIngredients = [];
				this.dishes = null;
				this.cooking = null;
				this.preparation = null;
				this.waiting = null;
				this.youtubeLink = '';
				this.authorName = '';
				this.authorProfession = '';

				this.addTranslation();
				this.data.articleType = this.articleTypes[0].id;
				this.initTranslationLanguage(this.data.translations[0]);
				this.selectedIngredient = this.ingredients[0];
			},
			deleteLanguage: function (index) {
				this.data.translations.splice(index, 1);
			},
			onFileChange: function (e, storeDict, key) {
				let files = e.target.files || e.dataTransfer.files;
				if (!files.length) return;
				let file = files[0];
				let reader = new FileReader();

				reader.onload = (e) => {
					this.$set(storeDict, key, e.target.result);
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
				const data = Object.assign({}, this.data);
				if (this.data.articleType === 1) {
					data.ingredients = [];
					this.selectedIngredients.forEach(function (ingredient) {
						data.ingredients.push({
							ingredientId: ingredient.ingredient.id,
							isMainIngredient: ingredient.isMainIngredient,
							quantity: ingredient.quantity
						});
					});
					data.dishes = this.dishes;
					data.cooking = this.cooking;
					data.preparation = this.preparation;
					data.waiting = this.waiting;
					data.youtubeLink = this.youtubeLink;
				}

				this.requestsUnsatisfied++;
				this.$http.post('/api/article/', data)
					.then(response => {
						this.$root.notifyAction.success();
						// this.initArticleFields();
						this.$router.push({name: this.data.articleType === 1 ? 'RecipeList' : 'ArticleList'});
						this.requestsUnsatisfied--;
					})
					.catch(err => {
						this.requestsUnsatisfied--;
						this.$root.notifyAction.errorPermanent(err);
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
