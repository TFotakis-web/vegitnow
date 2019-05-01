const basePath = 's6AptmegHaGM3Ry5vdlr/';
export { basePath as adminBasePath };

export default [
	{
		path: basePath,
		name: 'MainAdministration',
		component: require('../components/Admin/MainAdministration').default,
		children: [
			{ path: 'database/', name: 'DatabaseAdministration', pathToRegexpOptions: {strict: true} },
			{
				path: 'admin/',
				name: 'Administration',
				component: require('../components/Admin/Administration').default,
				children: [
					{ path: 'createArticle/', name: 'CreateArticle', component: require('../components/Admin/CreateArticle').default },
					{ path: 'articles/', name: 'ArticleList', component: require('../components/Admin/ArticleList').default },
					{ path: 'recipes/', name: 'RecipeList', component: require('../components/Admin/RecipeList').default },
					{ path: 'ingredients/', name: 'IngredientList', component: require('../components/Admin/IngredientList').default },
					{ path: 'staticPages/', name: 'StaticPages', component: require('../components/Admin/StaticPages').default },
					{ path: 'ads/', name: 'Ads', component: require('../components/Admin/Ads').default }
				]
			}
		]
	}
];
