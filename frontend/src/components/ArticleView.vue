<template>
	<div id="articleView">
		<div id="RecipeImageAndStats" class="d-flex flex-column" style="height: 100vh;clip-path: polygon(2% 0%, 98% 0%, 97% 20%, 98% 70%, 96% 90%, 97.5% 95%, 98% 100%, 2% 100%, 3% 95%, 2% 80%, 2% 70%, 3% 20%);">
			<div class="full-box-img flex-grow-1 d-flex flex-column justify-content-end" :style="{ 'background-image': 'url(' + article.Thumbnail + ')' }">
				<div class="container">
					<h1 class="text-white w-100 text-center text-lg-left mb-4" style="text-shadow: black 0 0 20px;">{{ article.Title }}</h1>
				</div>
			</div>
			<div class="bgGreen1">
				<div class="container">
					<div class="d-lg-none py-4">
						<div class="col">
							<div class="bg-white rounded-circle mx-auto"
							     style="
								     height: 190px;
								     width: 190px;
								     background-size: cover;
								     background-repeat: inherit;
								     background-position: center center;
								     background-image: url(/static/img/karota.png);">
								<!--background-image: url({% static 'img/karota.png' %});">-->
							</div>
							<div class="dashedCircle rotating mx-auto"
							     style="height: 210px; width: 210px; margin-top: -200px; margin-left: -10px;">
							</div>
						</div>
						<div class="col text-center">
							<h2 class="fgGreen1 mt-3">{{ $t('Writes') }}:</h2>
							<p class="font-weight-bold m-0">John Papadimitriou</p>
							<hr>
							<p class="font-weight-bold m-0">
								Special Dietologist
								<br>
								Dr. University of Life
							</p>
						</div>
					</div>
					<div class="d-none d-lg-flex row py-4" style="height: 120px">
						<div class="offset-sm-3 col-sm-5 offset-md-2 col-md-4 " style="border-right: dashed 2px #327317">
							<div class="row h-100">
								<div class="col d-table h-100">
									<div class="d-table-cell align-middle">
										<h2 class="fgGreen1 text-right m-0">{{ $t('Writes') }}:</h2>
									</div>
								</div>
								<div class="col d-table h-100">
									<div class="d-table-cell align-middle">
										<p class="font-weight-bold m-0">John Papadimitriou</p>
									</div>
								</div>
							</div>
						</div>
						<div class="col-sm-3 d-table h-100">
							<div class="d-table-cell align-middle">
								<p class="font-weight-bold m-0">
									Special Dietologist
									<br>
									Dr. University of Life
								</p>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
		<div class="container d-none d-lg-block" style="position: relative; margin-top: -95px;">
			<div class="bg-white rounded-circle"
			     style="
				     height: 190px;
				     width: 190px;
				     background-size: cover;
				     background-repeat: inherit;
				     background-position: center center;
				     background-image: url(/static/img/karota.png);">
				<!--background-image: url({% static 'img/karota.png' %});">-->
			</div>
			<div class="dashedCircle rotating"
			     style="height: 210px; width: 210px; margin-top: -200px; margin-left: -10px;">
			</div>
		</div>
		<div id="Instructions" class="mt-4 mb-5 d-flex">
			<div class="container">
				<p class="m-0 text-justify">{{ article.Content }}</p>
				<p class="m-0 text-justify">Rinse each side of the raspberries with one jar of noodles.
					Pickles can be mashed up with salty carrots, also try decorateing the ricotta with water.
					Per guest prepare one cup of ice water with chopped chicken for dessert. Pork butt combines greatly with ground cauliflower.
					Chickpeas can be seasoned with al dente shrimps, also try mixing the pie with remoulade.
					Puréed rhubarb can be made dark by flavoring with joghurt.
					Try mixing the milk pork shoulders with sour cream and fish sauce, refrigerated.
					Per guest prepare twenty oz of salsa verde with mashed tofu for dessert.
					Raspberries stew has to have a minced, juicy broccoli component.
					Celery can be rubed with tangy spinach, also try seasoning the fritters with red wine.
					Flavor half a kilo of mackerel in two peaces of ice water. Chocolate combines greatly with cold chicken breasts.
					Peanut butter can be rinseed with sweet meatballs, also try whisking the smoothie with remoulade.
					Carrots cheesecake has to have a bitter, shredded sausages component.
					Per guest prepare one jar of water with roasted pumpkin seeds for dessert.
					To the aged butter add quinoa, caviar, vinegar and shredded leek.
					Large mackerel can be made fluffy by varnishing with hollandaise sauce.
					Okra can be varnished with aged apple, also try flavoring the punch with cocktail sauce.
					What’s the secret to roasted and muddy squid? Always use aromatic thyme. Chili combines greatly with sticky quinoa.
					Nachos can be enameled with warm strudel, also try covering the salad with honey.
					Mash up each side of the chicken lard with one cup of pickles.
					To the soaked cabbage add meatloaf, rhubarb, triple sec and bitter leek.
					To the thin peanut butter add meatballs, escargot, champaign and heated cauliflower.
				</p>
			</div>
		</div>
		<RecommendedArticles></RecommendedArticles>
	</div>
</template>

<script>
	import RecommendedArticles from './RecommendedArticles';

	export default {
		name: 'ArticleView',
		components: {
			RecommendedArticles
		},
		data: function () {
			return {
				id: 0,
				article: {}
			};
		},
		methods: {
			getArticleData: function () {
				this.$http.get('/api/articleContentTranslation/' + this.id + '/')
					.then((response) => {
						this.article = response.data;
					})
					.catch((err) => {
						console.log(err);
					});
			}
		},
		created: function () {
			this.id = this.$route.params.id;
		},
		mounted: function () {
			this.getArticleData();
		}
	};
</script>

<style scoped>

</style>
