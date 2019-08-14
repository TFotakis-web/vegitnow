<template>
	<div id="navigationBar">
		<nav class="navbar navbar-expand-md navbar-light bg-white fixed-top d-md-none">
			<div class="container">
				<router-link :to="{ name: 'Home' }" data-toggle="collapse" data-target=".navbar-collapse.show">
					<img src="/static/app/img/VegItNowLogo.svg" alt="Vegitnow Logo" height="40">
				</router-link>
				<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
					<span class="navbar-toggler-icon"></span>
				</button>
				<div class="collapse navbar-collapse" id="navbarNav">
					<ul class="navbar-nav">
						<li class="nav-item">
							<router-link :to="{ name: 'RecipesList' }" class="nav-link font-weight-bold" data-toggle="collapse" data-target=".navbar-collapse.show">{{ $t('Recipes') }}</router-link>
						</li>
						<li class="nav-item">
							<router-link :to="{ name: 'ArticlesList' }" class="nav-link font-weight-bold" data-toggle="collapse" data-target=".navbar-collapse.show">{{ $t('Articles') }}</router-link>
						</li>
						<li class="nav-item">
							<a @click="changeLanguage()" class="nav-link" data-toggle="collapse" data-target=".navbar-collapse.show">
								<div class="locale-btn">
									<span>{{ this.$i18n.locale === 'en' ? 'GR' : 'EN' }}</span>
								</div>
							</a>
						</li>
					</ul>
				</div>
			</div>
		</nav>

		<nav class="navbar navbar-light bg-white fixed-top navbar-expand-md flex-nowrap d-none d-md-flex">
			<div class="container">
				<div class="d-flex w-100 align-items-center">
					<div class="">
						<router-link :to="{ name: 'Home' }" class="navbar-brand" data-toggle="collapse" data-target=".navbar-collapse.show">
							<img src="/static/app/img/VegItNowLogo.svg" alt="Vegitnow Logo" height="40">
						</router-link>
					</div>
					<div class="flex-grow-1">
						<ul class="navbar-nav w-100 justify-content-center">
							<li class="nav-item">
								<router-link :to="{ name: 'RecipesList' }" class="nav-link font-weight-bold" data-toggle="collapse" data-target=".navbar-collapse.show">{{ $t('Recipes') }}</router-link>
							</li>
							<li class="nav-item">
								<router-link :to="{ name: 'ArticlesList' }" class="nav-link font-weight-bold" data-toggle="collapse" data-target=".navbar-collapse.show">{{ $t('Articles') }}</router-link>
							</li>
						</ul>
					</div>
					<div class="">
						<ul class="navbar-nav justify-content-end" style="position: relative; top: 2rem;">
							<li class="nav-item">
								<a @click="changeLanguage()" class="nav-link" data-toggle="collapse" data-target=".navbar-collapse.show">
									<div class="locale-btn">
										<span>{{ this.$i18n.locale === 'en' ? 'GR' : 'EN' }}</span>
									</div>
								</a>
							</li>
						</ul>
					</div>
				</div>
			</div>
		</nav>
	</div>
</template>

<script>
	export default {
		name: 'NavigationBar',
		methods: {
			changeLanguage: function () {
				this.$i18n.locale = this.$i18n.locale === 'en' ? 'gr' : 'en';
				this.$cookie.set('locale', this.$i18n.locale === 'en' ? 1 : 2);
				let path = this.$route.fullPath;
				if (this.$route.params.lang === 'gr') {
					path = path.replace('/gr/', '/en/');
				} else {
					path = path.replace('/en/', '/gr/');
				}
				this.$router.push({'path': path});
			}
		}
	};
</script>

<style scoped>
	.locale-btn {
		cursor: pointer;
		display: inline-block;
		width: 40px;
		height: 40px;
		line-height: 40px;
		text-align: center;
		background-color: var(--v-green2);
		clip-path: polygon(0% 46%, 12% 13%, 10% 1%, 31% 0%, 58% 2%, 77% 1%, 93% 10%, 100% 33%, 97% 65%, 84% 92%, 74% 100%, 45% 100%, 34% 97%, 22% 100%, 9% 92%);
	}

	.locale-btn span {
		margin: auto;
		font-weight: bold;
		color: white;
	}

	.navbar-toggler {
		border: 0;
	}
</style>
