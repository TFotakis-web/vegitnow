<template>
	<div class="col-12 col-lg-6 mb-3" :class="{'article-card-bordered': isLeft }">
		<div class="row">
			<div class="col-6">
				<h4>{{ article.Title }}</h4>
				<hr class="fgGreen1" style="border-top: dashed 2px;">
				<p style="font-size: 0.8em;">{{ article.Preview }}</p>
			</div>
			<div class="col-6 d-table">
				<div class="d-table-cell align-middle">
					<div class="full-screen-img" style="height: 160px;" :style="{ 'background-image': 'url(' + article.Thumbnail + ')' }"></div>
				</div>
			</div>
		</div>
		<div class="row py-4">
			<router-link :to="{ name: 'ArticleView', params: { id: article.id }}" class="btn px-4 bgGreen0 text-white text-uppercase font-weight-bold mx-auto" style="border-radius: 2rem;">{{ $t('Read more') }}</router-link>
		</div>
	</div>
</template>

<script>
	export default {
		name: 'ArticleCard',
		props: [
			'article',
			'isLeft'
		]
	};
</script>

<style scoped>
	.article-card-bordered {
		border-right: dashed 2px #327317;
	}
</style>
