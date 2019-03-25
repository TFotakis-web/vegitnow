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

		<div :id="'ArticleAuthorInput' + article.id" v-if="article['ArticleTypeId'] === 2" class="col-12">
			<div class="row">
				<label :id="'AuthorNameInput' + article.id" class="label col-6">Author Name:
					<input type="text" class="form-control" id="AuthorName" placeholder="Author Name" v-model="article.AuthorName">
				</label>

				<label :id="'AuthorProfessionInput' + article.id" class="label col-6">Author Profession:
					<input type="text" class="form-control" id="AuthorProfession" placeholder="Author Profession" v-model="article.AuthorProfession">
				</label>

				<label :id="'AuthorProfilePictureInput' + article.id" class="label col-12">{{ $t('Author Profile Picture') }}:
					<span class="custom-file">
						<label class="custom-file-label" :for="'AuthorProfilePicture' + article.id">{{ $t('Choose file') }}</label>
						<input type="file" class="custom-file-input" :id="'AuthorProfilePicture' + article.id" @change="onFileChange($event, article, 'AuthorProfilePicture')">
					</span>
				</label>
			</div>
		</div>


		<label :id="'ArticleThumbnailInput' + article.id" class="label col-12">{{ $t('Thumbnail') }}:
			<span class="custom-file">
				<label class="custom-file-label" :for="'ArticleThumbnail' + article.id">{{ $t('Choose file') }}</label>
				<input type="file" class="custom-file-input" :id="'ArticleThumbnail' + article.id" @change="onFileChange($event, article, 'Thumbnail')">
			</span>
		</label>

		<label :id="'ArticleContentInput' + article.id" class="col-12">{{ $t('Content') }}:
			<Summernote height="400" :model="article.Content" v-on:change="value => { article['Content'] = value }"/>
		</label>

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
	import Summernote from '../Various/Summernote';

	export default {
		name: 'AdminArticleForm',
		components: {
			Summernote
		},
		props: [
			'article'
		],
		methods: {
			onFileChange: function (e, storeDict, key) {
				let files = e.target.files || e.dataTransfer.files;
				if (!files.length) return;
				let file = files[0];
				let reader = new FileReader();

				reader.onload = (e) => {
					this.$set(storeDict, key, e.target.result);
				};
				reader.readAsDataURL(file);
			}
		}
	};
</script>

<style scoped>

</style>
