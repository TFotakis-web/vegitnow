const basePath = 'articles/';

export default [
	{ path: basePath, name: 'ArticlesList', component: require('../components/Articles/ArticlesList').default },
	{ path: basePath + ':id/', name: 'ArticleView', component: require('../components/Articles/ArticleView').default }
];
