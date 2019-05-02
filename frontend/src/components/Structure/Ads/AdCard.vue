<template>
	<div class="col-12 col-lg-6 mb-3 text-center" :class="[this.listType === 'recipes'? 'col-xl-4' : '']">
		<AdImg :ad="ad"/>
	</div>
</template>

<script>
	import AdImg from './AdImg';

	export default {
		name: 'AdCard',
		components: {
			AdImg
		},
		props: {
			ad: {
				type: Object,
				default: {}
			},
			listType: {
				type: String,
				default: ''
			}
		}
	};
</script>

<style scoped>

</style>
