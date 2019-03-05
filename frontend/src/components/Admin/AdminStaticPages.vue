<template>
	<div id="AdminStaticPages" class="mb-5 h-100 w-100" v-if="!requestsUnsatisfied">
		<div id="accordion" class="container">
			<div class="card" v-for="(page, key) in staticPages">
				<div class="card-header" :id="'heading' + key">
					<h5 class="mb-0">
						<button @click="fetchData(key)" class="btn btn-link" data-toggle="collapse" :data-target="'#collapse' + key" aria-expanded="false" :aria-controls="'collapse' + key">
							{{ page.Name }}
						</button>
					</h5>
				</div>

				<div :id="'collapse' + key" class="collapse" :aria-labelledby="'heading' + key" data-parent="#accordion">
					<div class="card-body">
						<div>
							<h5 v-if="languages[page.Language]">{{ languages[page.Language].Name }}</h5>
							<div class="mb-3" v-if="page.Content !== ''">
								<Summernote height="400" :model="page.Content" v-on:change="value => { page.Content = value }"/>
							</div>
							<div class="form-group row">
								<div class="col text-right">
									<button type="button" class="btn bgGreen0 text-white" @click="saveStaticPage(key)"><i class="fas fa-save"></i> {{ $t('Save') }}</button>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
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
