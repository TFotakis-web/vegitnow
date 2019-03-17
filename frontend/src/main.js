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
// var VueCookie = Vue.require('vue-cookie');

Vue.use(VueResource);
Vue.use(Notifications);
Vue.use(VueCookie);
Vue.use(VueScrollTo);

Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
	el: '#app',
	router,
	i18n,
	template: '<App/>',
	components: {App}
});

function getCookie (name) {
	var cookieValue = null;
	if (document.cookie && document.cookie !== '') {
		var cookies = document.cookie.split(';');
		for (var i = 0; i < cookies.length; i++) {
			var cookie = jQuery.trim(cookies[i]);
			// Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) === (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}

Vue.http.headers.common['X-CSRFToken'] = getCookie('csrftoken');
Vue.http.headers.common['locale'] = getCookie('locale');
