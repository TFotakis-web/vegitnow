<template>
	<div id="app" class="d-flex flex-column" style="min-height: 100vh;">
		<div class="flex-grow-1">
			<NavigationBar></NavigationBar>
			<router-view></router-view>
		</div>
		<Footer></Footer>
	</div>
</template>

<script>
	import NavigationBar from './components/NavigationBar.vue';
	import Footer from './components/Footer.vue';

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
