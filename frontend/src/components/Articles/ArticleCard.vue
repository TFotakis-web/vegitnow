<template>
	<div class="col-12 col-md-6 mb-3">
		<router-link class="v-link-no-underline v-underline-card-title" :to="routerUrl" style="color: inherit; ">
			<div class="card border-0 bg-transparent">
				<div class="card-body position-relative">
					<div class="full-screen-img position-absolute mt-3" style="height: 160px; width:160px; right: 0; z-index:1" :style="{ 'background-image': 'url(' + article.Thumbnail + ')' }"></div>
					<div style="position: relative; z-index: 2; min-height: 170px">
						<h3 class="v-card-title v-card-title-shadow">{{ article.Title }}</h3>
						<span class="v-icon v-icon-card-line fgGreen1-as-bg position-relative d-block mb-3" style="height: 1.5rem; width: 18rem; z-index: 10"></span>
						<p class="col-8" style="font-size: 0.8em;">{{ article.Preview }}</p>
					</div>
				</div>
			</div>
		</router-link>
	</div>
</template>

<script>
	export default {
		name: 'ArticleCard',
		props: [
			'article',
		],
		data: function () {
			return {
				routerUrl: {
					name: 'ArticleView',
					params: {id: this.article.id},
					query: {
						title: this.$root.toGreeklish(this.article.Title).replace(/ /g, '-')
					}
				}
			};
		}
	};
</script>

<style scoped>

</style>
