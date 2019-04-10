// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import App from './App';
import router from './router';
import VueResource from 'vue-resource';
import {i18n} from './plugins/i18n';
import Notifications from 'vue-notification';
import VueCookie from 'vue-cookie';
import VueScrollTo from 'vue-scrollto';
import VueHead from 'vue-head';

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
	template: '<App/>',
	components: {App},
	data: function () {
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
			languages: {},
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
		}
	}
});

let getCookie = name => {
	let cookieValue = null;
	if (document.cookie && document.cookie !== '') {
		const cookies = document.cookie.split(';');
		for (let i = 0; i < cookies.length; i++) {
			const cookie = jQuery.trim(cookies[i]);
			// Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) === (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
};

Vue.http.headers.common['X-CSRFToken'] = getCookie('csrftoken');
Vue.http.headers.common['locale'] = getCookie('locale');
