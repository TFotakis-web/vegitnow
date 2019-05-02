<template>
	<a :href="ad.Link" @mousedown="countUp(ad.id)" target="_blank" rel="noopener" class="d-inline-block">
		<img :src="ad.Image" :alt="ad.Image" class="img-fluid" style="max-height: 250px">
	</a>
</template>

<script>
	export default {
		name: 'AdImg',
		props: {
			ad: {
				type: Object,
				default: {}
			}
		},
		methods: {
			countUp: function () {
				this.$http.get('/api/vegitnowad/?id=' + this.ad.id);
			}
		}
	};
</script>

<style scoped>

</style>
