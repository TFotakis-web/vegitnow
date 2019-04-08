<template>
	<textarea class="form-control"></textarea>
</template>

<script>
	export default {
		props: {
			model: {
				required: true
			},
			height: {
				type: String,
				default: '150'
			}
		},
		mounted: function () {
			const vm = this;
			const config = {
				height: this.height,
				toolbar: [
					['style', ['style']],
					['font', ['bold', 'italic', 'underline', 'superscript', 'subscript', 'strikethrough', 'clear']],
					['fontname', ['fontname']],
					['fontsize', ['fontsize']],
					['color', ['color']],
					['para', ['ul', 'ol', 'paragraph']],
					['height', ['height']],
					['table', ['table']],
					['insert', ['link', 'picture', 'video', 'hr']],
					['view', ['fullscreen', 'codeview']],
					['help', ['help']]
				],
				url: {
					language: '/static/summernote/lang/summernote-en-US.min.js',
					upload_attachment: '/summernote/upload_attachment/'
				},
				callbacks: {
					onInit: function () {
						$(vm.$el).summernote('code', vm.model);
					},
					onChange: function () {
						vm.$emit('change', $(vm.$el).summernote('code'));
					},
					onBlur: function () {
						vm.$emit('change', $(vm.$el).summernote('code'));
					}
				}
			};
			$(this.$el).summernote(config);
		},
		beforeDestroy: function () {
			$(this.$el).summernote('destroy');
		}
	};
</script>
