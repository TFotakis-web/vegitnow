<template>
	<div>
		<div class="navbar-placeholder"></div>
		<div class="container">
			<div v-html="page.Content"></div>
		</div>
	</div>
</template>

<script>
	export default {
		name: 'StaticPage',
		data: function () {
			return {
				id: this.$route.params.id,
				page: {}
			};
		},
		mounted: function () {
			this.getStaticPageContent();
		},
		methods: {
			getStaticPageContent: function () {
				this.$http.get('/api/staticPage/' + this.id + '/')
					.then((response) => {
						this.page = response.data;
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
