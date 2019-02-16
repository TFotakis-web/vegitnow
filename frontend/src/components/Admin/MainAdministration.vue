<template>
	<div id="Administration" class="container mb-5 h-100">
		<div class="navbar-placeholder"></div>
		<h1 class="text-center">Main Administration</h1>
		<router-link :to="{ name: 'Administration' }" class="nav-link font-weight-bold">{{ $t('Administration') }}</router-link>
		<router-link :to="{ name: 'DatabaseAdministration' }" class="nav-link font-weight-bold">{{ $t('Database') }}</router-link>
		<router-view></router-view>
	</div>
</template>

<script>
	export default {
		name: 'Administration'
	};
</script>

<style scoped>

</style>
