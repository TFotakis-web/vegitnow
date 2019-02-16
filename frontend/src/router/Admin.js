import CreateArticle from '../components/Admin/CreateArticle';
import Administration from '../components/Admin/Administration';
import AdminArticleList from '../components/Admin/AdminArticleList';
import AdminRecipeList from '../components/Admin/AdminRecipeList';
import AdminIngredientList from '../components/Admin/AdminIngredientList';
import MainAdministration from '../components/Admin/MainAdministration';

const basePath = '/s6AptmegHaGM3Ry5vdlr/';

export default [
	{
		path: basePath,
		name: 'MainAdministration',
		component: MainAdministration,
		children: [
			{
				path: basePath + 'database/',
				name: 'DatabaseAdministration',
				pathToRegexpOptions: {strict: true}
				// component: MainAdministration
			},
			{
				path: basePath + 'admin/',
				name: 'Administration',
				component: Administration,
				children: [
					{
						path: basePath + 'admin/createArticle/',
						name: 'CreateArticle',
						component: CreateArticle
					},
					{
						path: basePath + 'admin/articles/',
						name: 'AdminArticleList',
						component: AdminArticleList
					},
					{
						path: basePath + 'admin/recipes/',
						name: 'AdminRecipeList',
						component: AdminRecipeList
					},
					{
						path: basePath + 'admin/ingredients/',
						name: 'AdminIngredientList',
						component: AdminIngredientList
					}
				]
			}
		]
	}
];
