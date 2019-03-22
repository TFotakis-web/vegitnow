import CreateArticle from '../components/Admin/CreateArticle';
import Administration from '../components/Admin/Administration';
import ArticleList from '../components/Admin/ArticleList';
import RecipeList from '../components/Admin/RecipeList';
import IngredientList from '../components/Admin/IngredientList';
import MainAdministration from '../components/Admin/MainAdministration';
import StaticPages from '../components/Admin/StaticPages';

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
						name: 'ArticleList',
						component: ArticleList
					},
					{
						path: basePath + 'admin/recipes/',
						name: 'RecipeList',
						component: RecipeList
					},
					{
						path: basePath + 'admin/ingredients/',
						name: 'IngredientList',
						component: IngredientList
					},
					{
						path: basePath + 'admin/staticPages/',
						name: 'StaticPages',
						component: StaticPages
					}
				]
			}
		]
	}
];
