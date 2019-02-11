import CreateArticle from '../components/Admin/CreateArticle';
import Administration from '../components/Admin/Administration';
import AdminArticleList from '../components/Admin/AdminArticleList';
import AdminRecipeList from '../components/Admin/AdminRecipeList';
import AdminIngredientList from '../components/Admin/AdminIngredientList';

const basePath = '/s6AptmegHaGM3Ry5vdlr/admin/';

export default [
	{
		path: basePath,
		name: 'Administration',
		component: Administration
	},
	{
		path: basePath + 'createArticle/',
		name: 'CreateArticle',
		component: CreateArticle
	},
	{
		path: basePath + 'articles/',
		name: 'AdminArticleList',
		component: AdminArticleList
	},
	{
		path: basePath + 'recipes/',
		name: 'AdminRecipeList',
		component: AdminRecipeList
	},
	{
		path: basePath + 'ingredients/',
		name: 'AdminIngredientList',
		component: AdminIngredientList
	}
];
