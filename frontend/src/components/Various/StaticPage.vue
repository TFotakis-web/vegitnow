<template>
	<div class="d-flex flex-grow-1">
		<Loader v-if="requestsUnsatisfied"/>
		<div v-if="!requestsUnsatisfied" class="flex-grow-1">
			<div class="navbar-placeholder"></div>
			<div class="container">
				<div v-html="page.Content"></div>
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
				this.$http.get('/api/staticPage/' + this.id + '/')
					.then((response) => {
						this.page = response.data;
						this.requestsUnsatisfied--;
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
