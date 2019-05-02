<template>
	<div v-if="ads.length" class="container pb-5">
		<div class="row justify-content-center">
			<div class="col-12 col-md-8 col-lg-6" v-for="ad in ads" :key="ad.id">
				<AdImg :ad="ad"/>
			</div>
		</div>
	</div>
</template>

<script>
	import AdImg from './AdImg';

	export default {
		name: 'HomePage',
		components: {
			AdImg
		},
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
			}
		},
		mounted: function () {
			this.getAds();
		}
	};
</script>

<style scoped>

</style>
