import ArticlesList from '../components/Articles/ArticlesList';
import ArticleView from '../components/Articles/ArticleView';

const basePath = '/articles/';

export default [
	{
		path: basePath,
		name: 'ArticlesList',
		component: ArticlesList
	},
	{
		path: basePath + ':id/',
		name: 'ArticleView',
		component: ArticleView
	}
];
