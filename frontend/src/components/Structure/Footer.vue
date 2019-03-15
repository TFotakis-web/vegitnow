<template>
	<footer class="text-center" style="margin-top: -4em;">
		<router-link :to="{ name: 'Home' }" class="d-inline-block" style="position: relative; top: 15px; z-index: 1049">
			<img src="/static/img/VegItNowLogoSticker.svg" alt="Vegitnow Logo" height="40">
		</router-link>
		<div id="Footer" class="bg-white text-center pt-5"
		     style="
	     /*min-height:25vh;*/
         clip-path: polygon(0% 10%, 2% 5%, 17% 2%, 30% 3%, 47% 0%, 78% 1%, 97% 5%, 100% 11%, 100% 100%, 0% 100%, 0% 10%);
		"
		>
			<div class="container">
				<div class="row text-center">
					<div class="col-md-3 mb-4">
						<h1 class="fgGreen0">{{ $t('Join our Family') }}</h1>
					</div>
					<div class="col-md-3 mb-4">
						<form class="form-group">
							<input class="form-control mb-1" type="email" :placeholder="$t('Insert your email') + '...'" aria-label="email"
							       style="border-bottom: solid #2d6c13 2px;border-top: 0; border-left: 0; border-right: 0;">
							<button class="btn bgGreen0 text-white form-control" style="box-shadow: none" type="submit">
								<i class="icon-mail"></i> {{ $t('Subscribe') }}
							</button>
						</form>
					</div>
					<div class="col-md-3 mb-4">
						<div class="container-fluid">
							<div class="row" style="font-size: 0.7rem">
								<div v-for="(column, index) in columnedStaticPages" :key="index" class="col-md-6">
									<router-link class="text-dark d-block" :to="{ name: 'StaticPage', params: { id: page.id }}" :key="page.id" v-for="page in column">{{ page['Name'] }}</router-link>
								</div>
							</div>
						</div>
					</div>
					<div class="col-md-3 mb-4">
						<h1 class="fgGreen0">{{ $t('Follow us') }}</h1>
						<h1>
							<a class="fgGreen0" href="#"><span class="icon-facebook"></span></a>
							<a class="fgGreen0" href="#"><span class="icon-instagram"></span></a>
						</h1>
					</div>
				</div>
			</div>
		</div>
	</footer>
</template>

<script>
	export default {
		name: 'Footer',
		data: function () {
			return {
				staticPages: {}
			};
		},
		mounted: function () {
			this.getStaticPages();
		},
		methods: {
			getStaticPages: function () {
				this.$http.get('/api/staticPage/?locale=' + this.$cookie.get('locale'))
					.then((response) => {
						this.staticPages = response.data;
					})
					.catch((err) => {
						console.log(err);
						this.$notify({
							text: this.$t('Something went wrong... Please check your connection.'),
							type: 'error'
						});
					});
			}
		},
		computed: {
			currentLanguageStaticPages: function () {
				return this.staticPages['1'];
			},
			columnedStaticPages: function () {
				let data = [];
				let column = [];
				let count = 0;

				for (const staticPage of Object.values(this.staticPages)) {
					if (count % 5 === 0) {
						if (count) data.push(column);
						column = [];
					}
					column.push(staticPage);
					count++;
				}
				if (column.length) data.push(column);
				return data;
			}
		}
	};
</script>

<style scoped>

</style>
