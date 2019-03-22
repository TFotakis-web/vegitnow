<template>
	<form v-if="article" :id="'ArticleTranslationForm' + article.id">
		<div :id="'ArticleLanguageInput' + article.id" class="form-group">
			<label for="ArticleLanguage" class="label">{{ $t('Select Language') }}:</label>
			<select class="custom-select" id="ArticleLanguage" v-model="article.Language">
				<option v-for="language in $root.languages" :value="language.id">{{ language.Name }}</option>
			</select>
		</div>

		<div :id="'ArticleTitleInput' + article.id" class="form-group">
			<label for="ArticleTitle" class="label">{{ $t('Title') }}:</label>
			<input type="text" class="form-control" id="ArticleTitle" :placeholder="$t('Title')" v-model="article.Title">
		</div>

		<div :id="'ArticleAuthorNameInput' + article.id" class="form-group">
			<label for="AuthorName" class="label">Author Name:</label>
			<input type="text" class="form-control" id="AuthorName" placeholder="Author Name" v-model="article.AuthorName">
		</div>

		<div :id="'ArticleAuthorProfessionInput' + article.id" class="form-group">
			<label for="AuthorProfession" class="label">Author Profession:</label>
			<input type="text" class="form-control" id="AuthorProfession" placeholder="Author Profession" v-model="article.AuthorProfession">
		</div>

		<div :id="'AuthorProfilePictureInput' + article.id" class="form-group">
			<label class="label">{{ $t('Author Profile Picture') }}:</label>
			<div class="custom-file">
				<label class="custom-file-label" :for="'AuthorProfilePicture' + article.id">{{ $t('Choose file') }}</label>
				<input type="file" class="custom-file-input" :id="'AuthorProfilePicture' + article.id" @change="onFileChange($event, article, 'authorProfilePicture')">
			</div>
		</div>

		<div :id="'ArticleThumbnailInput' + article.id" class="form-group">
			<label class="label">{{ $t('Thumbnail') }}:</label>
			<div class="custom-file">
				<label class="custom-file-label" :for="'ArticleThumbnail' + article.id">{{ $t('Choose file') }}</label>
				<input type="file" class="custom-file-input" :id="'ArticleThumbnail' + article.id" @change="onFileChange($event, article, 'thumbnail')">
			</div>
		</div>

		<div :id="'ArticleContentInput' + article.id" class="form-group">
			<label>{{ $t('Content') }}:</label>
			<Summernote height="400" :model="article.Content" v-on:change="value => { article['Content'] = value }"/>
		</div>

		<div :id="'ArticleReleaseDateTimeInput' + article.id" class="form-group">
			<label for="ArticleReleaseDate" class="label">{{ $t('Release Date') }}:</label>
			<div class="row">
				<div class="col">
					<input type="text" class="form-control mb-3" id="ArticleReleaseDate" :placeholder="$t('Date') + ' (dd/mm/yyyy)'" v-model="article.ReleaseDateTime.date">
				</div>
				<div class="col">
					<input type="text" class="form-control" id="ArticleReleaseTime" :placeholder="$t('Time') + ' (HH:MM)'" v-model="article.ReleaseDateTime.time">
				</div>
			</div>
		</div>

		<div :id="'ArticleOnCarouselInput' + article.id" class="form-check">
			<input type="checkbox" :id="'ArticleOnCarousel' + article.id" class="form-check-input" v-model="article.OnCarousel">
			<label class="form-check-label" :for="'ArticleOnCarousel' + article.id">{{ $t('Available on carousel') }}</label>
		</div>

		<div :id="'ArticleMarkDoneEditingInput' + article.id" class="form-check">
			<input type="checkbox" :id="'ArticleMarkDoneEditing' + article.id" class="form-check-input" v-model="article.DoneEditing">
			<label class="form-check-label" :for="'ArticleMarkDoneEditing' + article.id">{{ $t('Mark as Done Editing') }}</label>
		</div>
	</form>
</template>

<script>
	import Summernote from '../Various/Summernote';

	export default {
		name: 'AdminArticleForm',
		components: {
			Summernote
		},
		props: [
			'article'
		]
	};
</script>

<style scoped>

</style>
