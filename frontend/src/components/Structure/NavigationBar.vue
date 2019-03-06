<template>
	<div id="navigationBar">
		<nav class="navbar navbar-expand-md navbar-light bg-white fixed-top d-md-none">
			<div class="container">
				<router-link :to="{ name: 'Home' }">
					<img src="/static/img/logo.png" alt="Vegitnow Logo" height="40">
				</router-link>
				<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
					<span class="navbar-toggler-icon"></span>
				</button>
				<div class="collapse navbar-collapse" id="navbarNav">
					<ul class="navbar-nav">
						<li class="nav-item">
							<router-link :to="{ name: 'RecipesList' }" class="nav-link font-weight-bold">{{ $t('Recipes') }}</router-link>
						</li>
						<li class="nav-item">
							<router-link :to="{ name: 'ArticlesList' }" class="nav-link font-weight-bold">{{ $t('Articles') }}</router-link>
						</li>
						<!--<li class="nav-item">-->
							<!--<router-link :to="{ name: 'WhoWeAre' }" class="nav-link font-weight-bold">{{ $t('Who we are') }}</router-link>-->
						<!--</li>-->
						<!--<li class="nav-item">-->
							<!--<router-link :to="{ name: 'Communication' }" class="nav-link font-weight-bold">{{ $t('Communication') }}</router-link>-->
						<!--</li>-->
						<!--<li class="nav-item">-->
							<!--<router-link :to="{ name: 'Shop' }" class="nav-link">-->
								<!--<div class="vegShop-btn">-->
									<!--<span>VEG SHOP</span>-->
								<!--</div>-->
							<!--</router-link>-->
						<!--</li>-->
						<li class="nav-item">
							<a @click="changeLanguage()" class="nav-link">
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
						<router-link :to="{ name: 'Home' }" class="navbar-brand">
							<img src="/static/img/logo.png" alt="Vegitnow Logo" height="40">
						</router-link>
					</div>
					<div class="flex-grow-1">
						<ul class="navbar-nav w-100 justify-content-center">
							<li class="nav-item">
								<router-link :to="{ name: 'RecipesList' }" class="nav-link font-weight-bold">{{ $t('Recipes') }}</router-link>
							</li>
							<li class="nav-item">
								<router-link :to="{ name: 'ArticlesList' }" class="nav-link font-weight-bold">{{ $t('Articles') }}</router-link>
							</li>
							<!--<li class="nav-item">-->
								<!--<router-link :to="{ name: 'WhoWeAre' }" class="nav-link font-weight-bold">{{ $t('Who we are') }}</router-link>-->
							<!--</li>-->
							<!--<li class="nav-item">-->
								<!--<router-link :to="{ name: 'Communication' }" class="nav-link font-weight-bold">{{ $t('Communication') }}</router-link>-->
							<!--</li>-->
						</ul>
					</div>
					<div class="">
						<ul class="navbar-nav justify-content-end" style="position: relative; top: 2rem;">
							<!--<li class="nav-item">-->
								<!--<router-link :to="{ name: 'Shop' }" class="nav-link">-->
									<!--<div class="vegShop-btn">-->
										<!--<span>VEG SHOP</span>-->
									<!--</div>-->
								<!--</router-link>-->
							<!--</li>-->
							<li class="nav-item">
								<a @click="changeLanguage()" class="nav-link">
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
		created: function () {
			let locale = this.$cookie.get('locale');
			if (locale) {
				this.$i18n.locale = locale === '1' ? 'en' : 'gr';
			} else {
				this.$cookie.set('locale', this.$i18n.locale === 'en' ? 1 : 2);
			}
		},
		methods: {
			changeLanguage: function () {
				this.$i18n.locale = this.$i18n.locale === 'en' ? 'gr' : 'en';
				this.$cookie.set('locale', this.$i18n.locale === 'en' ? 1 : 2);
				this.$router.go();
			}
		}
	};
</script>

<style scoped>

</style>
