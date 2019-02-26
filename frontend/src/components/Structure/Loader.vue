<template>
	<div class="d-flex flex-grow-1">
		<div class="d-flex flex-grow-1 text-center">
			<img src="/static/img/v.png" alt="loader" height="40" class="loaderAnimation" style="margin: auto">
		</div>
	</div>
</template>

<script>
	export default {
		name: 'Loader'
	};
</script>

<style scoped>
	.loaderAnimation {
		-webkit-animation-iteration-count: infinite;
		animation-iteration-count: infinite;
		-webkit-animation-duration: 1s;
		animation-duration: 1s;
		-webkit-animation-fill-mode: both;
		animation-fill-mode: both;
		webkit-animation-name: loaderPulse;
		animation-name: loaderPulse;
	}

	@keyframes loaderPulse {
		0% {
			-webkit-transform: scale3d(1, 1, 1);
			transform: scale3d(1, 1, 1);
		}
		50% {
			-webkit-transform: scale3d(1.05, 1.05, 1.05);
			transform: scale3d(1.2, 1.2, 1.2);
		}
		100% {
			-webkit-transform: scale3d(1, 1, 1);
			transform: scale3d(1, 1, 1);
		}
	}
</style>
