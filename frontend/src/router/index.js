import Vue from 'vue';
import Router from 'vue-router';
import VueAnalytics from 'vue-analytics';
import Home from '../components/Home/Home';

// import Communication from '../components/Various/Communication';
// import WhoWeAre from '../components/Various/WhoWeAre';
// import Shop from '../components/Various/Shop';

import AdminUrls from './Admin';
import ArticleUrls from './Articles';
import RecipeUrls from './Recipes';
import StaticPage from '../components/Various/StaticPage';

Vue.use(Router);

var routes = [
	{
		path: '/',
		name: 'Home',
		component: Home
	},
	{
		path: '/staticPage/:id/',
		name: 'StaticPage',
		component: StaticPage
	}
];

routes = routes.concat(AdminUrls);
routes = routes.concat(ArticleUrls);
routes = routes.concat(RecipeUrls);

const router = new Router({
	mode: 'history',
	routes: routes,
	scrollBehavior: function (to, from, savedPosition) {
		if (savedPosition) {
			return savedPosition;
		}
		return {x: 0, y: 0};
	}
});
export default router;

Vue.use(VueAnalytics, {
	id: 'UA-136306065-1',
	router
});
