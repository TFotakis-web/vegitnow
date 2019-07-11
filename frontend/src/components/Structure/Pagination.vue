<template>
	<div class="row mb-3">
		<div class="col-sm-9 col-lg-10 text-center text-sm-left">
			<a class="mx-3 ml-sm-0 mr-sm-3" style="cursor: pointer" v-for="i in pagesGroup" @click="setPage(i - 1)" v-bind:class="{'fgGreen0 font-weight-bold': i - 1 === page, 'text-dark': i - 1 !== page}">{{ i }}</a>
			<hr class="fgGreen1 mt-0" style="border-top: 2px dashed;">
		</div>
		<div class="col-sm-3 col-lg-2 text-center text-sm-right">
			<button @click="pagedown()" class="btn btn-circle bgGreen2 text-white mr-2" style="font-size: 1.5rem; font-family: 'AC-ScriptCondenced_unicode', sans-serif;">
				<span aria-hidden="true"><</span>
				<span class="sr-only">Previous</span>
			</button>
			<button @click="pageup()" class="hidden btn btn-circle bgGreen2 text-white" style="font-size: 1.5rem; font-family: 'AC-ScriptCondenced_unicode', sans-serif;">
				<span aria-hidden="true">></span>
				<span class="sr-only">Next</span>
			</button>
		</div>
	</div>
</template>

<script>
	export default {
		name: 'Pagination',
		props: {
			items: {
				type: Array,
				default: []
			},
			itemsPerPage: {
				type: Number,
				default: 1
			}
		},
		data: function () {
			return {
				page: -1,
				pagesInRow: 5,
				pagesGroup: []
			};
		},
		methods: {
			pageup: function () {
				let newPage = this.page + 1 >= this.pagesLen ? this.pagesLen - 1 : this.page + 1;
				this.setPage(newPage);
			},
			pagedown: function () {
				let newPage = this.page - 1 < 0 ? 0 : this.page - 1;
				this.setPage(newPage);
			},
			setPage: function (pageNum) {
				if (!this.items.length) return;
				if (pageNum < 0 || pageNum >= this.pagesLen) {
					pageNum = 0;
				}
				this.page = pageNum;
				this.$router.replace({query: {page: pageNum + 1}});
				this.$parent.pageItems = this.items.slice(this.page * this.itemsPerPage, (this.page + 1) * this.itemsPerPage);
				let startingPage = this.page - Math.floor(this.pagesInRow / 2);
				if (startingPage < 0) {
					startingPage = 0;
				} else if (startingPage > this.pagesLen - this.pagesInRow) {
					startingPage = this.pagesLen - this.pagesInRow;
				}
				this.pagesGroup = [];
				for (let i = startingPage; i < startingPage + this.pagesInRow && i < this.pagesLen; i++) {
					this.pagesGroup.push(i + 1);
				}
			}
		},
		computed: {
			pagesLen: function () {
				let len = this.items.length / this.itemsPerPage;
				len = Math.ceil(len);
				return len;
			}
		},
		created: function () {
			let page = parseInt(this.$route.query.page) - 1 || 0;
			this.setPage(page);
		}
	};
</script>

<style scoped>

</style>
