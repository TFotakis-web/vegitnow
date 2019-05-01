<template>
	<div id="MainAdministration" class="d-flex flex-column flex-grow-1">
		<div class="navbar-placeholder"></div>
		<div class="container">
			<div class="row">
				<!--<h1 class="text-center">Main Administration</h1>-->
				<router-link :to="{ name: 'Administration' }" class="col text-right">{{ $t('Administration') }}</router-link>
<!--				<router-link :to="{ name: 'DatabaseAdministration' }" class="col" target="_blank">{{ $t('Database') }}</router-link>-->
				<a href="s6AptmegHaGM3Ry5vdlr/database/" class="col">{{ $t('Database') }}</a>
			</div>
		</div>
		<hr>
		<router-view/>
	</div>
</template>

<script>
	export default {
		name: 'Administration',
		head: {
			title: function () {
				return {
					inner: this.$t('Administration')
				};
			},
			meta: function () {
				return this.$root.headData.defaultMeta();
			}
		}
	};
</script>

<style scoped>

</style>
