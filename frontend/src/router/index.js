import Vue from 'vue';
import Router from 'vue-router';
import VueCookies from 'vue-cookie';
import {i18n} from '../plugins/i18n';
import {adminBasePath} from './Admin';

Vue.use(Router);

let routes = [
	{path: '', name: 'Home', component: require('../components/Home/Home').default},
	{path: 'staticPage/:id/', name: 'StaticPage', component: require('../components/Various/StaticPage').default}
];

routes = routes.concat(require('./Admin').default);
routes = routes.concat(require('./Articles').default);
routes = routes.concat(require('./Recipes').default);
routes = routes.concat(require('./Ingredients').default);

let redirectFunc = function () {
	let locale = VueCookies.get('locale');
	if (locale) {
		i18n.locale = locale === '1' ? 'en' : 'gr';
	} else {
		VueCookies.set('locale', i18n.locale === 'en' ? 1 : 2);
	}
	return i18n.locale + location.pathname;
};

let redirects = [
	{path: '/recipes*', redirect: redirectFunc},
	{path: '/articles*', redirect: redirectFunc},
	{path: '/ingredients*', redirect: redirectFunc},
	{path: '/staticPage*', redirect: redirectFunc},
	{path: '/' + adminBasePath + '*', redirect: redirectFunc}
];

routes = redirects.concat([
	{path: '', redirect: redirectFunc},
	{path: '/:lang', component: require('../components/Structure/App').default, children: routes}
]);

const router = new Router({
	mode: 'history',
	routes: routes,
	scrollBehavior: function (to, from, savedPosition) {
		if (savedPosition) {
			return savedPosition;
		}
		return {x: 0, y: 0};
	},
	linkActiveClass: 'active'
});
export default router;

Vue.use(require('vue-analytics').default, {
	id: 'UA-136306065-1',
	router
});
