import RecipesList from '../components/Recipes/RecipesList';
import RecipeView from '../components/Recipes/RecipeView';

const basePath = 'recipes/';

export default [
	{
		path: basePath,
		name: 'RecipesList',
		component: RecipesList
	},
	{
		path: basePath + ':id/',
		name: 'RecipeView',
		component: RecipeView
	}
];
