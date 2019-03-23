<template>
	<div id="JoinOurFamily" class="bgGreen3" style="height:70vh; clip-path: polygon(2% 0%, 98% 0%, 98.5% 20%, 97% 60%, 97% 85%, 98% 100%, 2% 100%, 3% 60%, 1.5% 20%);">
		<div class="d-table h-100 mx-auto outerBox">
			<div class="d-table-cell align-middle position-relative">
				<div class="dashedCircle rotating"></div>
				<div class="FamilyCircle d-table">
					<div class="d-table-cell align-middle">
						<div v-if="this.$i18n.locale === 'en'">
							<h1 class="fgGreen0" style="font-size: 6rem">Join</h1>
							<h1 class="fgGreen0" style="margin-top: -40px;margin-left: -136px;transform: rotate(-20deg);font-size: 3rem;">our</h1>
							<img src="/static/img/VegItNowLogoLeaf.svg" alt="logo" style="margin-top: -100px;margin-left: 170px;height: 60px;">
							<h1 class="fgGreen0" style="margin-top: -50px; font-size: 4rem">Family</h1>
						</div>
						<div v-else>
							<h1 class="fgGreen0" style="font-size: 6rem">Μπες</h1>
							<h1 class="fgGreen0" style="margin-top: -0.7em;margin-left: -3em;transform: rotate(-15deg);font-size: 3rem;">στην</h1>
							<h1 class="fgGreen0" style="margin-top: -0.5em;font-size: 2.5rem;">ΟΙΚΟΓΕΝΕΙΑ</h1>
							<img src="/static/img/VegItNowLogoLeaf.svg" alt="logo" style="margin-top: -175px;margin-right: -205px;height: 60px;">
							<h1 class="fgGreen0" style="margin-top: -1.3em;margin-right: -4em;transform: rotate(-15deg);font-size: 3rem;">μας</h1>
						</div>
						<button @click="onclick()" v-scroll-to="{ el: '#mce-EMAIL' }" class="btn bgGreen2 text-white px-4" style="border-radius: 2rem;">{{ $t('Sign up') }}</button>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	export default {
		name: 'JoinOurFamily',
		methods: {
			onclick: function () {
				$('#mce-EMAIL').focus();
			}
		}
	};
</script>

<style scoped>
	@media (min-width: 375px) {
		.outerBox {
			zoom: 80% !important;
		}
	}

	@media (min-width: 565px) {
		.outerBox {
			zoom: 100% !important;
		}
	}

	.outerBox {
		max-width: 400px;
		zoom: 60%;
	}

	.FamilyCircle {
		height: 400px;
		width: 400px;
		margin-top: -400px;
		text-align: center;
	}

	@-webkit-keyframes rotating /* Safari and Chrome */
	{
		from {
			-webkit-transform: rotate(0deg);
			-o-transform: rotate(0deg);
			transform: rotate(0deg);
		}
		to {
			-webkit-transform: rotate(360deg);
			-o-transform: rotate(360deg);
			transform: rotate(360deg);
		}
	}

	@keyframes rotating {
		from {
			-ms-transform: rotate(0deg);
			-moz-transform: rotate(0deg);
			-webkit-transform: rotate(0deg);
			-o-transform: rotate(0deg);
			transform: rotate(0deg);
		}
		to {
			-ms-transform: rotate(360deg);
			-moz-transform: rotate(360deg);
			-webkit-transform: rotate(360deg);
			-o-transform: rotate(360deg);
			transform: rotate(360deg);
		}
	}

	.rotating {
		-webkit-animation: rotating 60s linear infinite;
		-moz-animation: rotating 60s linear infinite;
		-ms-animation: rotating 60s linear infinite;
		-o-animation: rotating 60s linear infinite;
		animation: rotating 60s linear infinite;
	}

	.dashedCircle {
		height: 400px;
		width: 400px;
		border-radius: 50%;
		border: dashed #2d6c13;
		pointer-events: none;
		overflow: hidden;
	}
</style>
