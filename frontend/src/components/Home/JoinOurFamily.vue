<template>
	<div id="JoinOurFamily" class="bgGreen3 join-our-family-container">
		<div class="d-table h-100 mx-auto outerBox">
			<div class="d-table-cell align-middle position-relative">
				<div class="dashedCircle rotating"></div>

				<div class="FamilyCircle d-table">
					<div class="d-table-cell align-middle">
						<div v-if="this.$i18n.locale === 'en'">
							<h1 class="fgGreen0 e-join">Join</h1>
							<h1 class="fgGreen0 e-our">our</h1>
							<img src="/static/app/img/VegItNowLogoLeaf.svg" alt="logo" class="e-img">
							<h1 class="fgGreen0 e-family">Family</h1>
						</div>
						<div v-else>
							<h1 class="fgGreen0 g-mpes">Μπες</h1>
							<h1 class="fgGreen0 g-stin">στην</h1>
							<h1 class="fgGreen0 g-oikogeneia">ΟΙΚΟΓΕΝΕΙΑ</h1>
							<img src="/static/app/img/VegItNowLogoLeaf.svg" alt="logo" class="g-img">
							<h1 class="fgGreen0 g-mas">μας</h1>
						</div>
						<button @click="onclick()" v-scroll-to="{ el: '#mce-EMAIL' }" class="btn bgGreen2 text-white px-4 joinBtn"><span>{{ $t('Sign up') }}</span></button>
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
	/*@media (min-width: 375px) {*/
	/*	.outerBox {*/
	/*		zoom: 50% !important;*/
	/*	}*/
	/*}*/
	/**/
	/*@media (min-width: 565px) {*/
	/*	.outerBox {*/
	/*		zoom: 100% !important;*/
	/*	}*/
	/*}*/

	/*.outerBox {*/
	/*	max-width: 200px;*/
	/*max-width: calc(400px / 1.5);*/
	/*max-width: 400px;*/
	/*zoom: 45%;*/
	/*}*/

	.dashedCircle {
		height: 70vw;
		width: 70vw;
		max-height: 400px;
		max-width: 400px;
		border-radius: 50%;
		border: dashed #2d6c13;
		pointer-events: none;
		overflow: hidden;
	}

	.FamilyCircle {
		height: 70vw;
		width: 70vw;
		max-height: 400px;
		max-width: 400px;
		margin-top: -70vw;
		text-align: center;
	}

	.g-mpes {
		font-size: 10vw;
	}

	.g-stin {
		margin-top: -5vw;
		margin-left: -25vw;
		transform: rotate(-15deg);
		font-size: 6vw;
	}

	.g-oikogeneia {
		margin-top: -3vw;
		font-size: 7vw;
	}

	.g-img {
		margin-top: -38vw;
		margin-right: -55vw;
		height: 10vw;
		max-height: 60px;
	}

	.g-mas {
		margin-top: -5vw;
		margin-right: 20vw;
		transform: rotate(-15deg);
		font-size: 5vw;
		width: fit-content;
		float: right;
	}

	.joinBtn {
		border-radius: 2rem;
	}

	.joinBtn span {
		font-size: 3vw;
	}

	.e-join {
		font-size: 14vw;
	}

	.e-our {
		margin-top: -5vw;
		margin-left: -25vw;
		transform: rotate(-20deg);
		font-size: 8vw;
	}

	.e-img {
		margin-top: -25vw;
		margin-left: 25vw;
		height: 10vw;
		max-height: 60px;
	}

	.e-family {
		margin-top: -10vw;
		font-size: 10vw;
	}

	@media (min-width: 550px) {
		.FamilyCircle {
			margin-top: -400px;
		}

		.g-mpes {
			font-size: 96px;
		}

		.g-stin {
			margin-top: -35px;
			margin-left: -200px;
			transform: rotate(-15deg);
			font-size: 3rem;
		}

		.g-oikogeneia {
			margin-top: -29px;
			font-size: 3rem;
		}

		.g-img {
			margin-top: -240px;
			margin-right: -330px;
		}

		.g-mas {
			margin-top: -35px;
			margin-right: 90px;
			font-size: 2.5rem;
		}

		.joinBtn span {
			font-size: 1rem;
		}

		.e-join {
			font-size: 6rem;
		}

		.e-our {
			margin-top: -40px;
			margin-left: -136px;
			transform: rotate(-20deg);
			font-size: 3rem;
		}

		.e-img {
			margin-top: -100px;
			margin-left: 170px;
			height: 60px;
		}

		.e-family {
			margin-top: -50px;
			font-size: 4rem;
		}
	}

	.join-our-family-container {
		height: 70vh;
		clip-path: polygon(2% 0%, 98% 0%, 98.5% 20%, 97% 60%, 97% 85%, 98% 100%, 2% 100%, 3% 60%, 1.5% 20%);
	}
</style>
