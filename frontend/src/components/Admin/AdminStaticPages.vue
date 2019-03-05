<template>
	<div id="AdminStaticPages" class="mb-5 h-100 w-100" v-if="!requestsUnsatisfied">
		<div id="AdminStaticPagesAccordion" class="container mb-3">
			<div class="card" v-for="(page, key) in staticPages">
				<div class="card-header" :id="'heading' + key">
					<h5 class="mb-0">
						<button @click="fetchData(key)" class="btn btn-link" data-toggle="collapse" :data-target="'#collapse' + key" aria-expanded="false" :aria-controls="'collapse' + key">
							{{ page.Name }}
						</button>
					</h5>
				</div>

				<div :id="'collapse' + key" class="collapse" :aria-labelledby="'heading' + key" data-parent="#AdminStaticPagesAccordion">
					<div class="card-body">
						<div id="AdminStaticPagesTranslationsAccordion" class="mb-3">
							<div class="card" v-for="translation in page.data" :key="translation.id">
								<div class="card-header" :id="'translationHeading' + translation.id">
									<h5 class="mb-0">
										<button class="btn btn-link" data-toggle="collapse" :data-target="'#translationCollapse' + translation.id" aria-expanded="false" :aria-controls="'translationCollapse' + translation.id">
											{{ languages[translation.Language].Name }}
										</button>
										<button type="button" class="align-middle float-right btn btn-sm bg-danger text-white" @click="deleteTranslation(translation.id)">
											<i class="fas fa-trash"></i>
											{{ $t('Delete') }}
										</button>
										<button type="button" class="align-middle float-right btn btn-sm bgGreen0 text-white mr-1" @click="saveTranslation(translation.id)">
											<i class="fas fa-save"></i>
											{{ $t('Save') }}
										</button>
									</h5>
								</div>

								<div :id="'translationCollapse' + translation.id" class="collapse" :aria-labelledby="'translationHeading' + translation.id" data-parent="#AdminStaticPagesTranslationsAccordion">
									<div class="card-body">
										<div :id="'TranslationLanguageInput' + translation.id" class="form-group row">
											<label :for="'TranslationLanguage' + translation.id" class="col-sm-2 col-form-label">{{ $t('Select Language') }}:</label>
											<div class="col-sm-10">
												<select class="custom-select" :id="'TranslationLanguage' + translation.id" v-model="translation.Language">
													<option v-for="language in languages" :value="language.id">{{ language.Name }}</option>
												</select>
											</div>
										</div>

										<div :id="'NameInput' + translation.id" class="form-group row">
											<label :for="'Name' + translation.id" class="col-sm-2 col-form-label">{{ $t('Static Page Name') }}:</label>
											<div class="col-sm-10">
												<input type="text" class="form-control" :id="'Name' + translation.id" :placeholder="$t('Static Page Name')" v-model="translation.Name">
											</div>
										</div>

										<Summernote :id="'ContentInput' + translation.id" height="400" :model="translation.Content" v-on:change="value => { translation.Content = value }"/>

										<div :id="'ListedInput' + translation.id" class="form-check row">
											<div class="col">
												<input :id="'ListedCheckbox' + translation.id" type="checkbox" class="form-check-input" v-model="translation['listed']">
												<label :for="'ListedCheckbox' + translation.id" class="form-check-label">Listed</label>
											</div>
										</div>

										<div :id="'PrivateInput' + translation.id" class="form-check row">
											<div class="col">
												<input :id="'PrivateCheckbox' + translation.id" type="checkbox" class="form-check-input" v-model="translation['private']">
												<label :for="'PrivateCheckbox' + translation.id" class="form-check-label">Private</label>
											</div>
										</div>
									</div>
								</div>
							</div>
						</div>

						<div class="form-group row">
							<div class="col text-right">
								<button type="button" class="btn btn-default" @click="addInitializedTranslation()"><i class="fas fa-plus"></i> {{ $t('Add Language') }}</button>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>

		<div id="AddStaticPageInput" class="container">
			<button type="button" class="btn bgGreen0 text-white" @click="addStaticPage()"><i class="fas fa-plus"></i> {{ $t('Add Static Page') }}</button>
		</div>
	</div>
</template>

<script>
	import Summernote from '../Various/Summernote';

	export default {
		name: 'AdminStaticPages',
		components: {
			Summernote
		},
		data: function () {
			return {
				staticPages: [],
				languages: {},
				requestsUnsatisfied: 0
			};
		},
		mounted: function () {
			this.getStaticPages();
			this.getLanguages();
		},
		methods: {
			getStaticPages: function () {
				this.requestsUnsatisfied++;
				this.$http.get('/api/staticPage/')
					.then((response) => {
						this.staticPages = response.data;
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
			getLanguages: function () {
				this.requestsUnsatisfied++;
				this.$http.get('/api/language/')
					.then((response) => {
						this.languages = response.data;
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
			fetchData: function (pageId) {
				this.$http.get('/api/staticPage/' + pageId + '/')
					.then((response) => {
						this.staticPages[pageId] = response.data;
					})
					.catch((err) => {
						console.log(err);
					});
			},
			saveStaticPage: function (key) {
				this.$http.patch('/api/staticPage/' + key + '/', this.staticPages[key])
					.then((response) => {
						console.log(response);
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
			}
		}
	};
</script>

<style scoped>

</style>
