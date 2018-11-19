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

<style>
</style>
