<template>
	<div>
		<input type="file" @change="onFileChange($event.target.files)">
	</div>
</template>

<script>
	export default {
		name: 'ImageInput',
		props: [
			'obj'
		],
		methods: {
			onFileChange: function (files) {
				if (!files.length) return;
				let imageFile = files[0];
				if (!imageFile.type.match('image.*')) return;

				let reader = new FileReader();
				reader.onload = (e) => {
					this.$set(this.obj, 'name', imageFile.name);
					this.$set(this.obj, 'data', e.target.result);
				};
				reader.readAsDataURL(imageFile);
			}
		}
	};
</script>
