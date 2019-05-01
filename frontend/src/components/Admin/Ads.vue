<template>
	<div id="AdminAds" class="mb-5 h-100 w-100" v-if="!requestsUnsatisfied">
		<div id="AddAdInput" class="container mb-3">
			<button type="button" class="btn bgGreen0 text-white" @click="addAd()"><i class="fas fa-plus"></i> {{ $t('Add a new Ad') }}</button>
		</div>

		<div id="AdminAdsAccordion" class="container">
			<div class="card" v-for="(ad, key) in ads">
				<div class="card-header" :id="'heading' + key">
					<h5 class="mb-0">
						<button class="btn btn-link" data-toggle="collapse" :data-target="'#collapse' + key" aria-expanded="false" :aria-controls="'collapse' + key">
							{{ ad.Name }}
						</button>

						<button type="button" class="align-middle float-right btn btn-sm bg-danger text-white" @click="removeAd(ad, key)">
							<i class="fas fa-trash"></i>
							{{ $t('Delete') }}
						</button>

						<button type="button" class="align-middle float-right btn btn-sm bgGreen0 text-white mr-1" @click="saveAd(ad)">
							<i class="fas fa-save"></i>
							{{ $t('Save') }}
						</button>
					</h5>
				</div>

				<div :id="'collapse' + key" class="collapse" :aria-labelledby="'heading' + key" data-parent="#AdminAdsAccordion">
					<div class="card-body">
						<div :id="'AdminAdsTranslationsAccordion' + key" class="mb-3">
							<div :id="'NameInput' + key" class="form-group row">
								<label :for="'Name' + key" class="col-sm-2 col-form-label">{{ $t('Name') }}:</label>
								<div class="col-sm-10">
									<input type="text" class="form-control" :id="'Name' + key" :placeholder="$t('Name')" v-model="ad.Name">
								</div>
							</div>

							<div :id="'AdTypeInput' + key" class="form-group row">
								<label :for="'AdType' + key" class="col-sm-2 col-form-label">{{ $t('Type') }}:</label>
								<div class="col-sm-10">
									<select class="custom-select" :id="'AdType' + key" v-model="ad.AdType">
										<option v-for="(adType, adTypeKey) in $root.adTypes" :value="adTypeKey">{{ adType }}</option>
									</select>
								</div>
							</div>

							<div :id="'TargetClicksInput' + key" class="form-group row">
								<label :for="'TargetClicks' + key" class="col-sm-2 col-form-label">{{ $t('Target Clicks') }}:</label>
								<div class="col-sm-2">
									<input type="number" class="form-control" :id="'TargetClicks' + key" :placeholder="$t('Target Clicks')" v-model="ad.TargetClicks">
								</div>

								<label :for="'CurrentClicks' + key" class="col-sm-3 col-form-label">{{ $t('Current Clicks') }}: {{ ad.Clicks }}</label>
							</div>

							<div :id="'AdReleaseDateTimeInput' + ad.id" class="form-group row">
								<label for="AdReleaseDate" class="label col-6">{{ $t('Release Date') }}:
									<input type="text" class="form-control" id="AdReleaseDate" :placeholder="$t('Date') + ' (dd/mm/yyyy)'" v-model="ad.ReleaseDateTime.date">
								</label>
								<label for="AdReleaseTime" class="label col-6">{{ $t('Release Time') }}:
									<input type="text" class="form-control" id="AdReleaseTime" :placeholder="$t('Time') + ' (HH:MM)'" v-model="ad.ReleaseDateTime.time">
								</label>
							</div>

							<div :id="'AdRemoveDateTimeInput' + ad.id" class="form-group row">
								<label for="AdRemoveDate" class="label col-6">{{ $t('Remove Date') }}:
									<input type="text" class="form-control" id="AdRemoveDate" :placeholder="$t('Date') + ' (dd/mm/yyyy)'" v-model="ad.RemoveDateTime.date">
								</label>
								<label for="AdRemoveTime" class="label col-6">{{ $t('Remove Time') }}:
									<input type="text" class="form-control" id="AdRemoveTime" :placeholder="$t('Time') + ' (HH:MM)'" v-model="ad.RemoveDateTime.time">
								</label>
							</div>

							<div class="card" v-for="(translation, index) in ad.Translations" :key="index">
								<div class="card-header" :id="'translationHeading' + index">
									<h5 class="mb-0">
										<button class="btn btn-link" data-toggle="collapse" :data-target="'#translationCollapse' + key + '-' + index" aria-expanded="false" :aria-controls="'translationCollapse' + key + '-' + index">
											{{ $root.languages[translation.Language].Name }}
										</button>
										<button type="button" class="align-middle float-right btn btn-sm bg-danger text-white" @click="removeTranslation(ad, translation, index)">
											<i class="fas fa-trash"></i>
											{{ $t('Delete') }}
										</button>
									</h5>
								</div>

								<div :id="'translationCollapse' + key + '-' + index" class="collapse" :aria-labelledby="'translationHeading' + key + '-' + index" :data-parent="'#AdminAdsTranslationsAccordion' + key">
									<div class="card-body">
										<div :id="'TranslationLanguageInput' + key + '-' + index" class="form-group row">
											<label :for="'TranslationLanguage' + key + '-' + index" class="col-sm-2 col-form-label">{{ $t('Select Language') }}:</label>
											<div class="col-sm-10">
												<select class="custom-select" :id="'TranslationLanguage' + key + '-' + index" v-model="translation.Language">
													<option v-for="language in $root.languages" :value="language.id">{{ language.Name }}</option>
												</select>
											</div>
										</div>

										<div :id="'LinkInput' + key + '-' + index" class="form-group row">
											<label :for="'Link' + key + '-' + index" class="col-sm-2 col-form-label">{{ $t('Link') }}:</label>
											<div class="col-sm-10">
												<input type="text" class="form-control" :id="'Link' + key + '-' + index" :placeholder="$t('Link')" v-model="translation.Link">
											</div>
										</div>

										<div :id="'ImageInput' + key + '-' + index" class="form-group row">
											<label :id="'Image' + key + '-' + index" class="label col-12">{{ $t('Image') }}:
												<ImageInput :obj="translation.Image"/>
											</label>
										</div>
									</div>
								</div>
							</div>
						</div>

						<div class="form-group row">
							<div class="col text-right">
								<button type="button" class="btn btn-default" @click="addTranslation(ad)"><i class="fas fa-plus"></i> {{ $t('Add Language') }}</button>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import ImageInput from '../Structure/ImageInput';

	export default {
		name: 'Ads',
		components: {
			ImageInput
		},
		data: function () {
			return {
				ads: [],
				requestsUnsatisfied: 0
			};
		},
		methods: {
			getAds: function () {
				this.requestsUnsatisfied++;
				this.$http.get('/api/vegitnowad/?admin')
					.then(response => {
						this.ads = response.data;
						this.requestsUnsatisfied--;
					})
					.catch(this.$root.notifyAction.error);
			},
			addAd: function () {
				let ad = {
					'id': -1,
					'Name': 'New Ad',
					'AdType': Object.keys(this.$root.adTypes)[0],
					'Clicks': 0,
					'TargetClicks': 0,
					'ReleaseDateTime': {
						'date': '',
						'time': ''
					},
					'RemoveDateTime': {
						'date': '',
						'time': ''
					},
					'Translations': []
				};
				this.addTranslation(ad);
				this.ads.unshift(ad);
			},
			addTranslation: function (ad) {
				let translation = {
					'id': -1,
					'Language': Object.keys(this.$root.languages)[0],
					'Image': {
						name: '',
						data: ''
					},
					'Link': ''
				};
				ad.Translations.push(translation);
			},
			saveAd: function (ad) {
				let method = '';
				let path = '';
				if (ad.id === -1) {
					method = 'post';
					path = '/api/vegitnowad/';
				} else {
					method = 'put';
					path = '/api/vegitnowad/' + ad.id + '/';
				}
				this.$http[method](path, ad)
					.then(response => {
						this.$root.notifyAction.success();
					})
					.catch(this.$root.notifyAction.error);
			},
			removeAd: function (ad, index) {
				if (ad.id === -1) {
					this.ads.splice(index, 1);
					this.$notify({
						text: this.$t('Deleted successfully!'),
						type: 'success'
					});
					return;
				}
				this.$http.delete('/api/vegitnowad/' + ad.id + '/')
					.then(response => {
						this.ads.splice(index, 1);
						this.$notify({
							text: this.$t('Deleted successfully!'),
							type: 'success'
						});
					})
					.catch(this.$root.notifyAction.error);
			},
			removeTranslation: function (ad, translation, index) {
				if (translation.id === -1) {
					this.ads.splice(index, 1);
					this.$notify({
						text: this.$t('Deleted successfully!'),
						type: 'success'
					});
					return;
				}
				this.$http.delete('/api/vegitnowad/' + ad.id + '/?translationId=' + translation.id)
					.then(response => {
						ad.Translations.splice(index, 1);
						this.$notify({
							text: this.$t('Deleted successfully!'),
							type: 'success'
						});
					})
					.catch(this.$root.notifyAction.error);
			}

		},
		mounted: function () {
			this.getAds();
		}
	};
</script>

<style scoped>

</style>
