// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
// import App from './App';
import router from './router';
import VueResource from 'vue-resource';
import {i18n} from './plugins/i18n';
import Notifications from 'vue-notification';
import VueCookie from 'vue-cookie';
import VueScrollTo from 'vue-scrollto';
import VueHead from 'vue-head';
import {toGreeklish} from 'greek-utils';

Vue.use(VueResource);
Vue.use(Notifications);
Vue.use(VueCookie);
Vue.use(VueScrollTo);
Vue.use(VueHead);

Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
	el: '#app',
	router,
	i18n,
	// template: '<App/>',
	// components: {App},
	template: '<router-view/>',
	// components: {App},
	data: function () {
		let vm = this;
		return {
			notifyAction: {
				error: err => {
					console.log(err);
					this.$notify({
						text: this.$t('Something went wrong... Please check your connection.'),
						type: 'error'
					});
				},
				errorPermanent: err => {
					console.log(err);
					this.$notify({
						text: this.$t('Something went wrong... Please check your connection.'),
						type: 'error',
						duration: -1
					});
				},
				success: () => {
					this.$notify({
						text: this.$t('Saved successfully!'),
						type: 'success'
					});
				}
			},
			headData: {
				defaultMetaDict: {
					GeneralDescription: {name: 'description', content: 'All about vegan foods, drinks and lifestyle.', id: 'metaDescription'},
					GeneralKeywords: {name: 'keywords', content: 'Vegan, food, drink, lifestyle, nutrition', id: 'metaKeywords'},
					GooglePlusName: {itemprop: 'name', content: 'VegItNow', id: 'metaGooglePlusName'},
					GooglePlusDescription: {itemprop: 'description', content: 'All about vegan foods, drinks and lifestyle.', id: 'metaGooglePlusDescription'},
					GooglePlusImage: {itemprop: 'image', content: 'https://vegitnow.com/static/app/img/VegItNowLogoSocial.png', id: 'metaGooglePlusImage'},
					TwitterCard: {name: 'twitter:card', content: 'summary', id: 'metaTwitterCard'},
					TwitterSite: {name: 'twitter:site', content: '@VegItNow', id: 'metaTwitterSite'},
					TwitterTitle: {name: 'twitter:title', content: 'VegItNow', id: 'metaTwitterTitle'},
					TwitterDescription: {name: 'twitter:description', content: 'All about vegan foods, drinks and lifestyle.', id: 'metaTwitterDescription'},
					TwitterCreator: {name: 'twitter:creator', content: '@VegItNow', id: 'metaTwitterCreator'},
					TwitterImage: {name: 'twitter:image:src', content: 'https://vegitnow.com/static/app/img/VegItNowLogoSocial.png', id: 'metaTwitterImage'},
					OpenGraphTitle: {property: 'og:title', content: 'VegItNow Tzanis', id: 'metaOpenGraphTitle'},
					OpenGraphType: {property: 'og:type', content: 'article', id: 'metaOpenGraphType'},
					OpenGraphUrl: {property: 'og:url', content: 'https://vegitnow.com', id: 'metaOpenGraphUrl'},
					OpenGraphImage: {property: 'og:image', content: 'https://vegitnow.com/static/app/img/VegItNowLogoSocial.png', id: 'metaOpenGraphImage'},
					OpenGraphDescription: {property: 'og:description', content: 'All about vegan foods, drinks and lifestyle.', id: 'metaOpenGraphDescription'},
					OpenGraphSiteName: {property: 'og:site_name', content: 'VegItNow', id: 'metaOpenGraphSiteName'},
					OpenGraphPublishedTime: {property: 'article:published_time', content: '', id: 'metaOpenGraphPublishedTime'},
					OpenGraphModifiedTime: {property: 'article:modified_time', content: '', id: 'metaOpenGraphModifiedTime'},
					OpenGraphSection: {property: 'article:section', content: '', id: 'metaOpenGraphSection'},
					OpenGraphTag: {property: 'article:tag', content: '', id: 'metaOpenGraphTag'},
					OpenGraphAdmins: {property: 'fb:admins', content: '', id: 'metaOpenGraphAdmins'}
				},
				defaultMeta: () => Object.values(vm.$root.headData.defaultMetaDict),
				defaultHead: {
					title: '',
					meta: function () { return vm.$root.headData.defaultMeta(); }
				},
				updateMeta: function (dict) {
					let res = JSON.parse(JSON.stringify(vm.$root.headData.defaultMetaDict));
					for (const key in dict) {
						res[key].content = dict[key];
					}
					return Object.values(res);
				}
			},
			languages: {},
			adTypes: {
				HOME_JOIN_OUR_FAMILY: 'Home: Join Our Family',
				HOME_ARTICLES: 'Home: Articles',
				HOME_RECIPES: 'Home: Recipes',
				INSIDE_POST: 'Inside: Post'
			},
			requestsUnsatisfied: 0
		};
	},
	mounted: function () {
		this.getLanguages();
	},
	methods: {
		getLanguages: function () {
			this.requestsUnsatisfied++;
			this.$http.get('/api/language/')
				.then(response => {
					this.languages = response.data;
					this.requestsUnsatisfied--;
				})
				.catch(this.$root.notifyAction.error);
		},
		toGreeklish,
		combineArticlesWithAds: function (articleList, ads) {
			const probability = 0.5;
			const insertEveryNArticles = 3;

			let arr = [];
			let adIndex = 0;
			let articleIndex = 0;
			for (const article of articleList) {
				arr.push({ article: article });
				articleIndex++;
				// if (ads.length) {
				if (articleIndex % insertEveryNArticles === 0 && Math.random() <= probability && ads.length) {
					arr.push({ ad: ads[adIndex] });
					adIndex = (adIndex + 1) % ads.length;
				}
			}
			return arr;
		}
	}
});

Vue.http.headers.common['X-CSRFToken'] = VueCookie.get('csrftoken');
Vue.http.headers.common['locale'] = VueCookie.get('locale');
