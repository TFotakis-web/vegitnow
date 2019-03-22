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
						<div :id="'AdminStaticPagesTranslationsAccordion' + key" class="mb-3">
							<div class="card" v-for="(translation, index) in page.data" :key="index">
								<div class="card-header" :id="'translationHeading' + index">
									<h5 class="mb-0">
										<button class="btn btn-link" data-toggle="collapse" :data-target="'#translationCollapse' + key + '-' + index" aria-expanded="false" :aria-controls="'translationCollapse' + key + '-' + index">
											{{ $root.languages[translation.Language].Name }}
										</button>
										<button type="button" class="align-middle float-right btn btn-sm bg-danger text-white" @click="removeTranslation(page, index)">
											<i class="fas fa-trash"></i>
											{{ $t('Delete') }}
										</button>
										<button type="button" class="align-middle float-right btn btn-sm bgGreen0 text-white mr-1" @click="saveTranslation(page, index)">
											<i class="fas fa-save"></i>
											{{ $t('Save') }}
										</button>
									</h5>
								</div>

								<div :id="'translationCollapse' + key + '-' + index" class="collapse" :aria-labelledby="'translationHeading' + key + '-' + index" :data-parent="'#AdminStaticPagesTranslationsAccordion' + key">
									<div class="card-body">
										<div :id="'TranslationLanguageInput' + key + '-' + index" class="form-group row">
											<label :for="'TranslationLanguage' + key + '-' + index" class="col-sm-2 col-form-label">{{ $t('Select Language') }}:</label>
											<div class="col-sm-10">
												<select class="custom-select" :id="'TranslationLanguage' + key + '-' + index" v-model="translation.Language">
													<option v-for="language in $root.languages" :value="language.id">{{ language.Name }}</option>
												</select>
											</div>
										</div>

										<div :id="'NameInput' + key + '-' + index" class="form-group row">
											<label :for="'Name' + key + '-' + index" class="col-sm-2 col-form-label">{{ $t('Static Page Name') }}:</label>
											<div class="col-sm-10">
												<input type="text" class="form-control" :id="'Name' + key + '-' + index" :placeholder="$t('Static Page Name')" v-model="translation.Name">
											</div>
										</div>

										<Summernote :id="'ContentInput' + key + '-' + index" height="400" :model="translation.Content" v-on:change="value => { translation.Content = value }"/>

										<div :id="'ListedInput' + key + '-' + index" class="form-check row">
											<div class="col">
												<input :id="'ListedCheckbox' + key + '-' + index" type="checkbox" class="form-check-input" v-model="translation['Listed']">
												<label :for="'ListedCheckbox' + key + '-' + index" class="form-check-label">Listed</label>
											</div>
										</div>

										<div :id="'PrivateInput' + key + '-' + index" class="form-check row">
											<div class="col">
												<input :id="'PrivateCheckbox' + key + '-' + index" type="checkbox" class="form-check-input" v-model="translation['Private']">
												<label :for="'PrivateCheckbox' + key + '-' + index" class="form-check-label">Private</label>
											</div>
										</div>
									</div>
								</div>
							</div>
						</div>

						<div class="form-group row">
							<div class="col text-right">
								<button type="button" class="btn btn-default" @click="addTranslation(page)"><i class="fas fa-plus"></i> {{ $t('Add Language') }}</button>
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
				staticPages: {},
				requestsUnsatisfied: 0
			};
		},
		mounted: function () {
			this.getStaticPages();
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
			fetchData: function (pageId) {
				if (this.staticPages[pageId]['fetched']) return;
				for (const translationId of Object.values(this.staticPages[pageId]['translations'])) {
					this.$http.get('/api/staticPageTranslation/' + translationId + '/')
						.then((response) => {
							this.staticPages[pageId]['data'].push(response.data);
							this.staticPages[pageId]['fetched'] = true;
						})
						.catch((err) => {
							console.log(err);
							this.$notify({
								text: this.$t('Something went wrong... Please check your connection.'),
								type: 'error'
							});
						});
				}
			},
			initializedTranslation: function (staticPageId) {
				return {
					id: -1,
					StaticPage: staticPageId,
					Language: Object.keys(this.$root.languages)[0],
					Name: '',
					Content: '',
					Listed: false,
					Private: true
				};
			},
			addStaticPage: function () {
				if (this.staticPages.hasOwnProperty('-1')) return;
				this.$set(this.staticPages, '-1', {
					Name: this.$t('New Static Page'),
					data: [this.initializedTranslation(-1)],
					fetched: true,
					id: -1
				});
			},
			addTranslation: function (page) {
				// Todo: Check if there exists translations for all available languages
				page.data.push(this.initializedTranslation(page.id));
			},
			saveTranslation: function (page, index) {
				let method = '';
				let path = '';
				if (page.data[index].id === -1) {
					method = 'post';
					path = '/api/staticPageTranslation/';
				} else {
					method = 'put';
					path = '/api/staticPageTranslation/' + page.data[index].id + '/';
				}
				this.$http[method](path, page.data[index])
					.then((response) => {
						console.log(response);
						this.getStaticPages();
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
			removeTranslation: function (page, index) {
				this.$http.delete('/api/staticPageTranslation/' + page.data[index].id + '/')
					.then((response) => {
						// page.data.splice(index, 1);
						// if (!page.data.length) delete this.staticPages[page.id];
						this.getStaticPages();
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
			}
		}
	};
</script>

<style scoped>

</style>
