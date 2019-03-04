<template>
	<div id="app" class="d-flex flex-column" style="min-height: 100vh;">
		<!--<div class="flex-grow-1">-->
		<div class="d-flex flex-grow-1">
			<NavigationBar></NavigationBar>
			<router-view :key="$route.fullPath"/>
			<notifications position="bottom left"/>
		</div>
		<Footer></Footer>
	</div>
</template>

<script>
	import NavigationBar from './components/Structure/NavigationBar.vue';
	import Footer from './components/Structure/Footer.vue';

	export default {
		name: 'app',
		components: {
			NavigationBar,
			Footer
		}
	};
</script>

<style src="../static/css/bootstrap.min.css"></style>
<style src="../static/css/summernote-bs4.css"></style>
<style src="../static/fonts/fontawesome-free-5.5.0-web/css/all.css"></style>
<style src="../static/css/AlegreyaSans.css"></style>
<style src="../static/css/animate.css"></style>
<style src="../static/css/fontello.css"></style>
<style src="../static/css/colorPalette.css"></style>
<style src="../static/css/style.css"></style>

<style>
	.fade-enter-active {
		animation: fadeIn 1s ease-out;
	}

	@keyframes fadeIn {
		0% {
			opacity: 0;
		}
		100% {
			opacity: 1;
		}
	}


	.fade-leave-active {
		animation: fadeOut 0.3s ease-in;
	}

	@keyframes fadeOut {
		0% {
			opacity: 1;
		}
		100% {
			opacity: 0;
		}
	}
</style>
