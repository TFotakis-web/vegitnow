<template>
	<div class="d-flex flex-grow-1 mb-5">
		<Loader v-if="requestsUnsatisfied"/>
		<div v-if="!requestsUnsatisfied" class="flex-grow-1">
			<div class="navbar-placeholder"></div>
			<div class="container">
				<div class="htmlRenderer" v-html="page.Content"></div>
			</div>
		</div>
	</div>
</template>

<script>
	import Loader from '../Structure/Loader';

	export default {
		name: 'StaticPage',
		components: {
			Loader
		},
		data: function () {
			return {
				id: this.$route.params.id,
				page: {},
				requestsUnsatisfied: 0
			};
		},
		mounted: function () {
			this.getStaticPageContent();
		},
		methods: {
			getStaticPageContent: function () {
				this.requestsUnsatisfied++;
				this.$http.get('/api/staticPage/' + this.id + '/?locale=' + this.$cookie.get('locale'))
					.then(response => {
						this.page = response.data;
						this.requestsUnsatisfied--;
					})
					.catch((err) => {
						console.log(err);
						this.$notify({
							text: this.$t('Something went wrong... Please check your connection.'),
							type: 'error'
						});
						this.$router.push({name: 'Home'});
					});
			}
		}
	};
</script>

<style scoped>

</style>
