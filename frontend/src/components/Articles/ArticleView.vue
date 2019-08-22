<template>
	<div id="articleView" class="d-flex flex-grow-1">
		<Loader v-if="requestsUnsatisfied"/>
		<div v-if="!requestsUnsatisfied" class="flex-grow-1">
			<div id="RecipeImageAndStats" class="d-flex flex-column h-100-minus-navbar box-clip-path1">
				<div class="full-box-img flex-grow-1 d-flex flex-column justify-content-end" :style="{ 'background-image': 'url(' + article.Thumbnail + ')' }">
					<div class="container">
						<h1 class="text-white w-100 text-center text-lg-left mb-4" style="text-shadow: black 0 0 20px;">{{ article.Title }}</h1>
					</div>
				</div>
				<div class="bgGreen1">
					<div class="container">
						<div class="d-lg-none py-4">
							<div class="col">
								<div class="author-thumbnail mx-auto">
									<div class="dashedCircle v-border rotating"></div>
									<div class="authorProfilePictureCircle">
										<div class="bg-white rounded-circle mx-auto authorProfilePicture" :style="{ 'background-image': 'url(' + article.AuthorProfilePicture + ')' }"></div>
									</div>
								</div>
							</div>
							<div v-if="article['AuthorName']" class="col text-center">
								<h2 class="fgGreen1 mt-3">{{ $t('Writes') }}:</h2>
								<p class="font-weight-bold m-0">{{ article['AuthorName'] }}</p>
								<div v-if="article['AuthorProfession']">
									<hr>
									<p class="font-weight-bold m-0">
										{{ article['AuthorProfession'] }}
										<!--Special Dietologist-->
										<!--<br>-->
										<!--Dr. University of Life-->
									</p>
								</div>
							</div>
						</div>
						<div class="d-none d-lg-flex row py-4" style="height: 120px">
							<!--							<div ">-->
							<div v-if="article['AuthorName']" class="offset-sm-3 col-sm-5 offset-md-2 col-md-4 ">
								<div class="row h-100">
									<div class="col d-table h-100">
										<div class="d-table-cell align-middle">
											<h2 class="fgGreen1 text-right m-0">{{ $t('Writes') }}:</h2>
										</div>
									</div>
									<div class="col d-table h-100">
										<div class="d-table-cell align-middle">
											<p class="font-weight-bold m-0">{{ article['AuthorName'] }}</p>
										</div>
									</div>
								</div>
							</div>
							<div v-if="article['AuthorProfession'] && article['AuthorName']" class="col-sm-3 d-table h-100" style="border-left: dashed 2px var(--v-green6)">
								<div class="d-table-cell align-middle">
									<p class="font-weight-bold m-0">
										{{ article['AuthorProfession'] }}
										<!--Special Dietologist-->
										<!--<br>-->
										<!--Dr. University of Life-->
									</p>
								</div>
							</div>
							<!--							</div>-->
						</div>
					</div>
				</div>
			</div>
			<div class="container d-none d-lg-block" style="position: relative; margin-top: -95px; height: 210px">
				<div class="bg-white rounded-circle authorProfilePicture" :style="{ 'background-image': 'url(' + article.AuthorProfilePicture + ')' }"></div>
				<div class="dashedCircle v-border rotating" style="height: 210px; width: 210px; margin-top: -200px; margin-left: -10px;"></div>
			</div>
			<div id="ArticleContent" class="mt-4 d-flex">
				<div class="container">
					<div class="htmlRenderer" v-html="article.Content"></div>
				</div>
			</div>
			<div class="container mt-3 mb-5 text-center">
				<span v-if="article.ReleaseDateTime"><i>{{ $t('Published on') }}: {{ article.ReleaseDateTime.date }}</i></span>
			</div>
			<RecommendedArticles :current-article-id="id"/>
		</div>
	</div>
</template>

<script>
	import RecommendedArticles from './RecommendedArticles';
	import Loader from '../Structure/Loader';

	export default {
		name: 'ArticleView',
		components: {
			RecommendedArticles,
			Loader
		},
		data: function () {
			return {
				id: this.$route.params['id'].toString(),
				article: {},
				requestsUnsatisfied: 0
			};
		},
		methods: {
			getArticleData: function () {
				this.requestsUnsatisfied++;
				this.$http.get('/api/article/' + this.id + '/?locale=' + this.$cookie.get('locale'))
					.then(response => {
						this.article = response.data;
						this.$emit('updateHead');
						this.requestsUnsatisfied--;
						this.$router.push('?title=' + this.$root.toGreeklish(this.article.Title).replace(/ /g, '-'));
					})
					.catch((err) => {
						console.log(err);
						this.$notify({
							text: this.$t('Something went wrong... Please check your connection.'),
							type: 'error'
						});
						this.$router.push({name: 'ArticlesList'});
					});
			}
		},
		mounted: function () {
			this.getArticleData();
		},
		head: {
			title: function () {
				return this.article.Title ? {inner: this.article.Title} : '';
			},
			meta: function () {
				return this.$root.headData.updateMeta({
					GeneralDescription: this.article.Preview,
					// GeneralKeywords: '',
					GooglePlusName: this.article.Title,
					GooglePlusDescription: this.article.Preview,
					GooglePlusImage: location.origin + this.article.Thumbnail,
					// TwitterCard: '',
					// TwitterSite: '',
					TwitterTitle: this.article.Title,
					TwitterDescription: this.article.Preview,
					TwitterCreator: this.article.AuthorName || '',
					TwitterImage: location.origin + this.article.Thumbnail,
					OpenGraphTitle: this.article.Title,
					OpenGraphType: 'article',
					OpenGraphUrl: location.href,
					OpenGraphImage: location.origin + this.article.Thumbnail,
					OpenGraphDescription: this.article.Preview
					// ,
					// OpenGraphSiteName: '',
					// OpenGraphPublishedTime: '',
					// OpenGraphModifiedTime: '',
					// OpenGraphSection: '',
					// OpenGraphTag: '',
					// OpenGraphAdmins: ''
				});
			}
		}
	};
</script>

<style scoped>
	#articleView {
		--v-dashed-circle-size: 210px;
		--v-dashed-circle-padding: 10px;
	}

	.authorProfilePicture {
		height: calc(var(--v-dashed-circle-size) - 2 * var(--v-dashed-circle-padding));
		width: calc(var(--v-dashed-circle-size) - 2 * var(--v-dashed-circle-padding));
		background-size: cover;
		background-repeat: inherit;
		background-position: center center;
	}

	.authorProfilePictureCircle {
		margin-top: calc(var(--v-dashed-circle-padding) - var(--v-dashed-circle-size))
	}

	.dashedCircle {
		height: var(--v-dashed-circle-size);
		width: var(--v-dashed-circle-size);
		border-radius: 50%;
		pointer-events: none;
		overflow: hidden;
	}

	.author-thumbnail {
		height: var(--v-dashed-circle-size);
		width: var(--v-dashed-circle-size);
	}
</style>
