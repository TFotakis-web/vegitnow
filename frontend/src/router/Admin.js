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
					{ path: 'createArticle/', name: 'AdminCreateArticle', component: require('../components/Admin/CreateArticle').default },
					{ path: 'articles/', name: 'AdminArticlesList', component: require('../components/Admin/ArticleList').default },
					{ path: 'recipes/', name: 'AdminRecipesList', component: require('../components/Admin/RecipeList').default },
					{ path: 'ingredients/', name: 'AdminIngredientsList', component: require('../components/Admin/IngredientList').default },
					{ path: 'staticPages/', name: 'AdminStaticPages', component: require('../components/Admin/StaticPages').default },
					{ path: 'ads/', name: 'AdminAds', component: require('../components/Admin/Ads').default }
				]
			}
		]
	}
];
