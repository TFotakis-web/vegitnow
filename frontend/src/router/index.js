import Vue from 'vue';
import Router from 'vue-router';
import Home from '../components/Home/Home';

import Communication from '../components/Various/Communication';
import WhoWeAre from '../components/Various/WhoWeAre';
import Shop from '../components/Various/Shop';

import AdminUrls from './Admin';
import ArticleUrls from './Articles';
import RecipeUrls from './Recipes';

Vue.use(Router);

var routes = [
	{
		path: '/',
		name: 'Home',
		component: Home
	},
	{
		path: '/communication/',
		name: 'Communication',
		component: Communication
	},
	{
		path: '/who_we_are/',
		name: 'WhoWeAre',
		component: WhoWeAre
	},
	{
		path: '/shop/',
		name: 'Shop',
		component: Shop
	}
];

routes = routes.concat(AdminUrls);
routes = routes.concat(ArticleUrls);
routes = routes.concat(RecipeUrls);

export default new Router({
	mode: 'history',
	routes: routes
});
