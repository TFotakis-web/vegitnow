<template>
	<froala :tag="'textarea'" :config="config" v-model="model"/>
</template>

<script>
	import VueFroala from 'vue-froala-wysiwyg';
	// Require Froala Editor js file.
	require('../../../node_modules/froala-editor/js/froala_editor.pkgd.min.js');
	require('../../../node_modules/froala-editor/js/plugins.pkgd.min');
	require('../../../node_modules/froala-editor/js/languages/el.js');

	// Require Froala Editor css files.
	require('../../../node_modules/froala-editor/css/froala_editor.pkgd.min.css');
	require('../../../node_modules/froala-editor/css/plugins.pkgd.min.css');
	require('../../../node_modules/froala-editor/css/froala_style.min.css');

	export default {
		name: 'FroalaEditor',
		components: {
			VueFroala
		},
		props: {
			model: {
				required: true
			},
			height: {
				type: String,
				default: '150'
			}
		},
		data: function () {
			return {
				config: {
					language: this.$i18n.locale === 'en' ? '' : 'el',
					height: this.height,
					// zIndex: 9990,
					// toolbarInline: true,
					toolbarSticky: false,
					toolbarButtons: [
						'fullscreen', 'bold', 'italic', 'underline', 'strikeThrough', 'subscript',
						'superscript', '|', 'fontFamily', 'fontSize', 'color', 'inlineStyle',
						'paragraphStyle', '|', 'paragraphFormat', 'align', 'formatOL', 'formatUL',
						'outdent', 'indent', 'quote', '-', 'insertLink', 'insertImage', 'insertVideo',
						'insertFile', 'insertTable', '|', 'emoticons', 'specialCharacters', 'insertHR',
						'selectAll', 'clearFormatting', '|', 'print', 'help', 'html', '|', 'undo', 'redo'
					]
				}
			};
		}
	};
</script>

<style scoped>

</style>
