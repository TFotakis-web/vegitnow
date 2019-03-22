<template>
	<div id="AdminArticleEditAccordion">
		<div class="card mb-1" v-for="(article, index) in articleTranslations">
			<div class="card-header" :id="'heading' + index">
				<h5 class="mb-0">
					<button class="btn btn-link" data-toggle="collapse" :data-target="'#collapse' + index" aria-expanded="false" :aria-controls="'collapse' + index">
						{{ $root.languages[article.Language].Name }}
					</button>
					<!--<button type="button" class="align-middle float-right btn btn-sm bg-danger text-white" @click="removeTranslation()">-->
						<!--<i class="fas fa-trash"></i>-->
						<!--{{ $t('Delete') }}-->
					<!--</button>-->
					<!--<button type="button" class="align-middle float-right btn btn-sm bgGreen0 text-white mr-1" @click="saveTranslation()">-->
						<!--<i class="fas fa-save"></i>-->
						<!--{{ $t('Save') }}-->
					<!--</button>-->
				</h5>
			</div>

			<div :id="'collapse' + index" class="collapse" :aria-labelledby="'heading' + index" data-parent="#AdminArticleEditAccordion">
				<div class="card-body">
					<AdminArticleForm :article="article"/>
				</div>
			</div>
		</div>
		<button type="button" class="btn btn-primary" @click="addTranslation()"><i class="fas fa-plus"></i> {{ $t('Add Language') }}</button>
	</div>
</template>

<script>
	import AdminArticleForm from '../Admin/AdminArticleForm';

	export default {
		name: 'AdminArticleAccordion',
		components: {
			AdminArticleForm
		},
		props: ['articleTranslations']
	};
</script>

<style scoped>

</style>
