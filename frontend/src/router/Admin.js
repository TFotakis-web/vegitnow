import CreateArticle from '../components/Admin/CreateArticle';
import Administration from '../components/Admin/Administration';
import ArticleList from '../components/Admin/ArticleList';
import RecipeList from '../components/Admin/RecipeList';
import IngredientList from '../components/Admin/IngredientList';
import MainAdministration from '../components/Admin/MainAdministration';
import StaticPages from '../components/Admin/StaticPages';

const basePath = 's6AptmegHaGM3Ry5vdlr/';
export { basePath as adminBasePath };

export default [
	{
		path: basePath,
		name: 'MainAdministration',
		component: MainAdministration,
		children: [
			{
				path: 'database/',
				name: 'DatabaseAdministration',
				pathToRegexpOptions: {strict: true}
				// component: MainAdministration
			},
			{
				path: 'admin/',
				name: 'Administration',
				component: Administration,
				children: [
					{
						path: 'createArticle/',
						name: 'CreateArticle',
						component: CreateArticle
					},
					{
						path: 'articles/',
						name: 'ArticleList',
						component: ArticleList
					},
					{
						path: 'recipes/',
						name: 'RecipeList',
						component: RecipeList
					},
					{
						path: 'ingredients/',
						name: 'IngredientList',
						component: IngredientList
					},
					{
						path: 'staticPages/',
						name: 'StaticPages',
						component: StaticPages
					}
				]
			}
		]
	}
];
