var app = new Vue({
	el: '#starting',
	delimiters: ['${', '}'],
	data: {
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
		this.getArticles();
	},
	methods: {
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