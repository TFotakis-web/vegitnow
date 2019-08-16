<template>
	<div id="recommendedArticles" v-if="articles.length">
		<div id="ArticlesDualCard" class="d-none d-md-block" style="position: relative;">
			<a class="btn btn-circle bgGreen2 text-white" href="#articleCarouselDualCard" role="button" data-slide="prev" style="
				   font-size: 1.5rem;
				   font-family: 'AC-ScriptCondenced_unicode', sans-serif;
				   position: absolute;
				   top: 50%;
				   left: 1%;
				   z-index: 1;
				   ">
				<span aria-hidden="true"><</span>
				<span class="sr-only">Previous</span>
			</a>
			<a class="hidden btn btn-circle bgGreen2 text-white" href="#articleCarouselDualCard" role="button" data-slide="next" style="
				   font-size: 1.5rem;
				   font-family: 'AC-ScriptCondenced_unicode', sans-serif;
				   position: absolute;
				   top: 50%;
				   right: 1%;
				   z-index: 1;
				   ">
				<span aria-hidden="true">></span>
				<span class="sr-only">Next</span>
			</a>
			<h1 class="text-center" style="position: relative;top: -0.5em;margin-bottom: -1.2em;z-index: 1;">
				<router-link :to="{ name: 'ArticlesList' }" class="fgGreen0 bg-transparent">
					{{ $t('Articles') }}
				</router-link>
			</h1>
			<div class="bgGreen3 py-5" style="clip-path: polygon(5% 0%, 98% 0%, 97% 20%, 98% 70%, 96% 90%, 97.5% 95%, 98% 100%, 2% 100%, 3% 95%, 2% 80%, 2% 70%, 3% 20%, 2% 0%);">
				<div id="articleCarouselDualCard" class="carousel slide" data-ride="carousel">
					<div class="carousel-inner">
						<div v-for="(articlesPart, index) in dualArticles" class="carousel-item" :class="{ 'active': index === 0 }">
							<div class="container">
								<div class="row">
									<template v-if="noAdCards">
										<ArticleCard v-for="(article, index2) in articlesPart" :key="'dualArticleCard' + article.id" :article="article" :isLeft="index2 === 0"/>
									</template>
									<template v-else>
										<template v-for="article in articlesPart">
											<template v-if="article.hasOwnProperty('article')">
												<ArticleCard :article="article['article']" :key="'dual-article' + article['article'].id"/>
											</template>
											<template v-else>
												<AdCard :ad="article['ad']" listType="articles" :key="'dual-ad' + article['ad'].id + '-' + index"/>
											</template>
										</template>
									</template>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>

		<div id="ArticlesSingleCard" class="d-md-none" style="position: relative;">
			<a class="btn btn-circle bgGreen2 text-white" href="#articleCarouselSingleCard" role="button" data-slide="prev" style="
				   font-size: 1.5rem;
				   font-family: 'AC-ScriptCondenced_unicode', sans-serif;
				   position: absolute;
				   top: 68%;
				   left: 1%;
				   z-index: 1;
				   ">
				<span aria-hidden="true"><</span>
				<span class="sr-only">Previous</span>
			</a>
			<a class="hidden btn btn-circle bgGreen2 text-white" href="#articleCarouselSingleCard" role="button" data-slide="next" style="
				   font-size: 1.5rem;
				   font-family: 'AC-ScriptCondenced_unicode', sans-serif;
				   position: absolute;
				   top: 68%;
				   right: 1%;
				   z-index: 1;
				   ">
				<span aria-hidden="true">></span>
				<span class="sr-only">Next</span>
			</a>
			<h1 class="text-center fgGreen0" style="position: relative;top: -0.5em;margin-bottom: -1.2em;z-index: 1;">
				<router-link :to="{ name: 'ArticlesList' }" class="fgGreen0 bg-transparent">
					{{ $t('Articles') }}
				</router-link>
			</h1>
			<div class="bgGreen3 py-5" style="clip-path: polygon(5% 0%, 98% 0%, 97% 20%, 98% 70%, 96% 90%, 97.5% 95%, 98% 100%, 2% 100%, 3% 95%, 2% 80%, 2% 70%, 3% 20%, 2% 0%);">
				<div id="articleCarouselSingleCard" class="carousel slide" data-ride="carousel">
					<div class="carousel-inner">
						<div v-for="(article, index) in articles" class="carousel-item" :class="{ 'active': index === 0 }">
							<div class="container">
								<div class="row">
									<template v-if="noAdCards">
										<ArticleCard :article="article"/>
									</template>
									<template v-else>
										<template v-if="article.hasOwnProperty('article')">
											<ArticleCard :article="article['article']" :key="'single-article' + article['article'].id"/>
										</template>
										<template v-else>
											<AdCard :ad="article['ad']" listType="articles" :key="'single-ad' + article['ad'].id + '-' + index"/>
										</template>
									</template>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>

		<div v-if="location === 'home'" class="bgGreen3" style="clip-path: polygon(5% 0%, 98% 0%, 97% 20%, 98% 70%, 96% 90%, 97.5% 95%, 98% 100%, 2% 100%, 3% 95%, 2% 80%, 2% 70%, 3% 20%, 2% 0%)">
			<Ads AdType="HOME_ARTICLES"/>
		</div>
	</div>
</template>

<script>
	import ArticleCard from './ArticleCard';
	import Ads from '../Structure/Ads/HomePage';
	import AdCard from '../Structure/Ads/AdCard';

	export default {
		name: 'RecommendedArticles',
		components: {
			ArticleCard,
			Ads,
			AdCard
		},
		props: {
			currentArticleId: String,
			location: String,
			noAdCards: Boolean
		},
		data: function () {
			return {
				articleList: [],
				ads: []
			};
		},
		mounted: function () {
			this.getArticles();
			this.getAds();
		},
		methods: {
			getArticles: function () {
				this.$http.get('/api/article/?locale=' + this.$cookie.get('locale') + '&type=2&' + this.location)
					.then(response => { this.articleList = response.data; })
					.catch(this.$root.notifyAction.error);
			},
			getAds: function () {
				if (this.noAdCards) return;
				this.requestsUnsatisfied++;
				this.$http.get('/api/vegitnowad/?locale=' + this.$cookie.get('locale') + '&type=INSIDE_POST')
					.then(response => {
						this.ads = response.data;
						this.requestsUnsatisfied--;
					})
					.catch(err => {
						this.requestsUnsatisfied--;
						this.$root.notifyAction.error(err);
					});
			}
		},
		computed: {
			articles: function () {
				if (!this.currentArticleId) return this.articleList;
				let id = parseInt(this.currentArticleId);
				let filteredArticles = this.articleList.filter(function (obj) {
					return obj.id !== id;
				});
				return this.$root.combineArticlesWithAds(filteredArticles, this.ads);
			},
			dualArticles: function () {
				var arr = [];
				for (var index = 0; index < this.articles.length; index += 2) {
					var tmp = [];
					tmp.push(this.articles[index]);
					if (this.articles.length > index + 1) tmp.push(this.articles[index + 1]);
					arr.push(tmp);
				}
				return arr;
			}
		}
	};
</script>

<style scoped>
	#recommendedArticles {
		--card-title-shadow: var(--v-green3);
	}
</style>
