const basePath = 'ingredients/';

export default [
	{ path: basePath, name: 'IngredientsList', component: require('../components/Ingredients/IngredientsList').default },
	{ path: basePath + ':id/', name: 'IngredientView', component: require('../components/Ingredients/IngredientView').default }
];
