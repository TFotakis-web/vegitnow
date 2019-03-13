let app = new Vue({
	el: '#createArticle',
	delimiters: ['[[', ']]'],
	data: {
		languages: [],
		articleTypes: [],
		title: null,
		ingredients: [
			{id: 1, Name: 'Fava'},
			{id: 2, Name: 'Fakies'},
			{id: 3, Name: 'Ntomata'},
			{id: 4, Name: 'Aggouri'},
		],
		selectedIngredients: [],
		selectedIngredient: null,
		content: null,
		releaseDate: null,
		releaseTime: null,
		doneEditing: false,

		articles: [],
		loading: false,
		currentArticle: {},
		message: null,
		newArticle: {
			"UploadDateTime": null,
			"User": null
		},
	},
	mounted: function () {
		this.getArticleTypes();
		this.getLanguages();
	},
	methods: {
		getArticleTypes: function () {
			this.$http.get('/api/articleType/')
				.then((response) => {
					this.articleTypes = response.data;
				})
				.catch((err) => {
					console.log(err);
				})
		},
		getLanguages: function () {
			this.$http.get('/api/language/')
				.then((response) => {
					this.languages = response.data;
				})
				.catch((err) => {
					console.log(err);
				})
		},
		selectIngredient: function () {
			this.selectedIngredients.push({
				ingredient: this.selectedIngredient,
				isMainIngredient: false,
				quantity: 0
			});
		},
		removeSelectedIngredient: function (index) {
			this.selectedIngredients.splice(index, 1);
		},
		getArticles: function () {
			this.loading = true;
			this.$http.get('/api/article/')
				.then((response) => {
					this.articles = response.data;
					this.loading = false;
				})
				.catch((err) => {
					this.loading = false;
					console.log(err);
				})
		},
		getArticle: function (id) {
			this.loading = true;
			this.$http.get('/api/article/' + id + '/', id)
				.then((response) => {
					this.currentArticle = {
						'id': response.data.id,
						'User': response.data.User,
						'UploadDateTime': response.data.UploadDateTime
					};

					$("#editArticleModal").modal('show');
					this.loading = false;
				})
				.catch((err) => {
					this.loading = false;
					console.log(err);
				})
		},
		addArticle: function () {
			this.loading = true;
			this.$http.post('/api/article/', this.newArticle)
				.then((response) => {
					this.loading = false;
					this.getArticles();
				})
				.catch((err) => {
					this.loading = false;
					console.log(err);
				})
		},
		updateArticle: function () {
			this.loading = true;
			var updatedArticle = {
				'id': this.currentArticle.id,
				'User': this.currentArticle.User,
				'UploadDateTime': this.currentArticle.UploadDateTime
			};
			console.log(updatedArticle);
			this.$http.put('/api/article/' + this.currentArticle.id + '/', updatedArticle)
				.then((response) => {
					this.loading = false;
					this.currentArticle = response.data;
					this.getArticles();
				})
				.catch((err) => {
					this.loading = false;
					console.log(err);
				})
		},
		deleteArticle: function (id) {
			this.loading = true;
			this.$http.delete('/api/article/' + id + '/')
				.then((response) => {
					this.loading = false;
					this.getArticles();
				})
				.catch((err) => {
					this.loading = false;
					console.log(err);
				})
		}
	}
});

Vue.component('todo-item', {
	props: ['todo'],
	template: '<li>[[ todo.Name ]]</li>'
});