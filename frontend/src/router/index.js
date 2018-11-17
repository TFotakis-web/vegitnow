import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import RecipesList from '@/components/RecipesList'
import RecipeView from '@/components/RecipeView'
import ArticlesList from '@/components/ArticlesList'
import ArticleView from '@/components/ArticleView'
import Communication from '@/components/Communication'
import WhoWeAre from '@/components/WhoWeAre'

Vue.use(Router);

export default new Router({
	mode: 'history',
	routes: [
		{
			path: '/',
			name: 'Home',
			component: Home
		},
		{
			path: '/recipes/',
			name: 'RecipesList',
			component: RecipesList
		},
		{
			path: '/articles/',
			name: 'ArticlesList',
			component: ArticlesList
		},
		{
			path: '/recipes/:id/',
			name: 'RecipeView',
			component: RecipeView
		},
		{
			path: '/articles/:id/',
			name: 'ArticleView',
			component: ArticleView
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
		}
	]
})
