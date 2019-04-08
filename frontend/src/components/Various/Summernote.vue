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
				fontSizes: ['8', '9', '10', '11', '12', '14', '16', '18', '24', '36', '48', '64', '82', '150'],
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
					},
					onImageUpload: function (files) {
						for (const file of files) {
							let formData = new FormData();
							formData.append('files', file);
							vm.$http.post('/summernote/upload_attachment/', formData)
								.then(response => {
									$.each(response.data.files, function (index, file) {
										$(vm.$el).summernote('insertImage', file.url);
									});
								})
								.catch(err => {
									console.log(err);
									if (err.body.message) alert(err.body.message);
								});
						}
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
