<template>
	<div id="Administration" class="mb-5 h-100">
		<div class="navbar-placeholder"></div>
		<div class="container">
			<div class="row">
				<!--<h1 class="text-center">Main Administration</h1>-->
				<router-link :to="{ name: 'Administration' }" class="col text-right">{{ $t('Administration') }}</router-link>
				<router-link :to="{ name: 'DatabaseAdministration' }" class="col">{{ $t('Database') }}</router-link>
			</div>
		</div>
		<hr>
		<router-view/>
	</div>
</template>

<script>
	export default {
		name: 'Administration'
	};
</script>

<style scoped>

</style>
