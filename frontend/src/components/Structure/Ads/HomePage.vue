<template>
	<div v-if="ads.length" class="container py-5">
		<div class="row justify-content-center">
			<div class="col-12 col-md-8 col-lg-6" v-for="ad in ads" :key="ad.id">
				<a :href="ad.Link" @mousedown="countUp(ad.id)" target="_blank" rel="noopener" class="d-inline-block">
					<img :src="ad.Image" :alt="ad.Image" class="img-fluid">
				</a>
			</div>
		</div>
	</div>
</template>

<script>
	export default {
		name: 'HomePage',
		props: {
			AdType: {
				type: String,
				default: ''
			}
		},
		data: function () {
			return {
				ads: []
			};
		},
		methods: {
			getAds: function () {
				this.$http.get('/api/vegitnowad/?locale=' + this.$cookie.get('locale') + '&type=' + this.AdType)
					.then(response => {
						this.ads = response.data;
					})
					.catch(this.$root.notifyAction.error);
			},
			countUp: function (id) {
				this.$http.get('/api/vegitnowad/?id=' + id);
			}
		},
		mounted: function () {
			this.getAds();
		}
	};
</script>

<style scoped>

</style>
