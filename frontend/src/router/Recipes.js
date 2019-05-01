const basePath = 'recipes/';

export default [
	{ path: basePath, name: 'RecipesList', component: require('../components/Recipes/RecipesList').default },
	{ path: basePath + ':id/', name: 'RecipeView', component: require('../components/Recipes/RecipeView').default }
];
