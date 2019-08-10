<template>
	<div id="MainAdministration" class="d-flex flex-column flex-grow-1">
		<div class="container my-3">
			<ul class="nav nav-tabs">
				<li class="nav-item">
					<router-link :to="{ name: 'Administration' }" class="nav-link">{{ $t('Administration') }}</router-link>
				</li>
				<li class="nav-item">
					<a href="/s6AptmegHaGM3Ry5vdlr/database/" class="nav-link">{{ $t('Database') }}</a>
				</li>
			</ul>
		</div>
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
