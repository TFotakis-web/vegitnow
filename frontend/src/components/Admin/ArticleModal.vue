<template>
	<div class="modal fade" id="articleEditModal" tabindex="-1" role="dialog" aria-labelledby="articleEditModal" aria-hidden="true">
		<div class="modal-dialog modal-lg" role="document">
			<div class="modal-content">
				<div class="modal-header">
					<h5 class="modal-title" id="articleEditModalLabel">{{ $t('Edit') }}</h5>
					<button type="button" class="close" data-dismiss="modal" aria-label="Close">
						<span aria-hidden="true">&times;</span>
					</button>
				</div>
				<div class="modal-body">
					<ArticleAccordion v-if="article" :articleData="article"/>
				</div>
				<div class="modal-footer">
					<button @click="deleteArticle(articleId)" type="button" class="btn btn-danger text-white" data-dismiss="modal"><i class="fas fa-trash"></i> {{ $t('Delete') }}</button>
					<button @click="saveArticle()" type="button" class="btn bgGreen0 text-white">{{ $t('Save') }}</button>
					<button type="button" class="btn btn-secondary" data-dismiss="modal">{{ $t('Close') }}</button>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import ArticleAccordion from './ArticleAccordion';

	export default {
		name: 'AdminArticleModal',
		components: {
			ArticleAccordion
		},
		props: [
			'articleId'
		],
		data: function () {
			return {
				article: {}
			};
		},
		methods: {
			getArticleData: function (id) {
				this.$http.get('/api/article/' + id + '/?edit')
					.then(response => { this.article = response.data; })
					.catch(this.$root.notifyAction.error);
			},
			deleteArticle: function (id) {
				this.$http.delete('/api/article/' + id + '/')
					.then(response => {
						this.$parent.getArticles();
					})
					.catch(this.$root.notifyAction.error);
			},
			saveArticle: function () {
				this.$http.put('/api/article/' + this.articleId + '/', this.article)
					.then(response => {
						this.$root.notifyAction.success();
					})
					.catch(this.$root.notifyAction.error);
			}
		},
		watch: {
			articleId: function (newVal, oldVal) {
				this.getArticleData(this.articleId);
			}
		}
	};
</script>

<style scoped>

</style>
