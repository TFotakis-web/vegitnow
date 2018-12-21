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
			let config = {
				height: this.height
			};
			let vm = this;
			config.callbacks = {
				onInit: function () {
					$(vm.$el).summernote('code', vm.model);
				},
				onChange: function () {
					vm.$emit('change', $(vm.$el).summernote('code'));
				},
				onBlur: function () {
					vm.$emit('change', $(vm.$el).summernote('code'));
				}
			};
			$(this.$el).summernote(config);
		}
	};
</script>
