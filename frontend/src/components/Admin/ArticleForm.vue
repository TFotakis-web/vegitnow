<template>
	<form v-if="article" :id="'ArticleTranslationForm' + article.id" class="row">
		<label :id="'ArticleLanguageInput' + article.id" class="label col-sm-6">{{ $t('Select Language') }}:
			<select class="custom-select" id="ArticleLanguage" v-model="article.Language">
				<option v-for="language in $root.languages" :value="language.id">{{ language.Name }}</option>
			</select>
		</label>

		<label :id="'ArticleTitleInput' + article.id" class="label col-12">{{ $t('Title') }}:
			<input type="text" class="form-control" id="ArticleTitle" :placeholder="$t('Title')" v-model="article.Title">
		</label>

		<label v-if="$parent.articleData['ArticleTypeId'] === 2" :id="'PreviewInput' + article.id" class="label col-12">Preview:
			<input type="text" class="form-control" id="Preview" placeholder="Preview" v-model="article.Preview">
		</label>

		<div :id="'ArticleAuthorInput' + article.id" v-if="$parent.articleData['ArticleTypeId'] === 2" class="col-12">
			<div class="row">
				<label :id="'AuthorNameInput' + article.id" class="label col-6">Author Name:
					<input type="text" class="form-control" id="AuthorName" placeholder="Author Name" v-model="article.AuthorName">
				</label>

				<label :id="'AuthorProfessionInput' + article.id" class="label col-6">Author Profession:
					<input type="text" class="form-control" id="AuthorProfession" placeholder="Author Profession" v-model="article.AuthorProfession">
				</label>

				<label :id="'AuthorProfilePictureInput' + article.id" class="label col-12">{{ $t('Author Profile Picture') }}:
					<ImageInput :obj="article.AuthorProfilePicture"/>
				</label>
			</div>
		</div>

		<label :id="'ArticleThumbnailInput' + article.id" class="label col-12">{{ $t('Thumbnail') }}:
			<ImageInput :obj="article.Thumbnail"/>
		</label>

		<label :id="'ArticleContentInput' + article.id" class="col-12">{{ $t('Content') }}:</label>
		<div class="col-12">
			<Summernote height="400" :model="article.Content" v-on:change="value => { article['Content'] = value }"/>
			<!-- <TipTap :value="article['Content']" v-on:input="value => { article['Content'] = value }"/>-->
		</div>

		<div :id="'ArticleReleaseDateTimeInput' + article.id" class="col-12">
			<div class="row">
				<label for="ArticleReleaseDate" class="label col-6">{{ $t('Release Date') }}:
					<input type="text" class="form-control" id="ArticleReleaseDate" :placeholder="$t('Date') + ' (dd/mm/yyyy)'" v-model="article.ReleaseDateTime.date">
				</label>
				<label for="ArticleReleaseTime" class="label col-6">{{ $t('Release Time') }}:
					<input type="text" class="form-control" id="ArticleReleaseTime" :placeholder="$t('Time') + ' (HH:MM)'" v-model="article.ReleaseDateTime.time">
				</label>
			</div>
		</div>

		<label :id="'ArticleOnCarouselInput' + article.id" class="col-12">
			<input type="checkbox" :id="'ArticleOnCarousel' + article.id" v-model="article.OnCarousel">
			{{ $t('Available on carousel') }}
		</label>

		<label :id="'ArticleMarkDoneEditingInput' + article.id" class="col-12">
			<input type="checkbox" :id="'ArticleMarkDoneEditing' + article.id" v-model="article.DoneEditing">
			{{ $t('Mark as Done Editing') }}
		</label>
	</form>
</template>

<script>
	import ImageInput from '../Structure/ImageInput';
	// import TipTap from '../Structure/TipTap';
	import Summernote from '../Structure/Summernote';

	export default {
		name: 'AdminArticleForm',
		components: {
			ImageInput,
			Summernote
			// TipTap
		},
		props: [
			'article'
		]
	};
</script>

<style scoped>

</style>
