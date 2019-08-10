<template>
	<div id="app" class="d-flex flex-column" style="min-height: 100vh;">
		<div v-if="$root.requestsUnsatisfied" class="centered-block">
			<!--<object type="image/svg+xml" data="/static/app/img/VegItNowLogoLeaf.svg" height="40" class="loaderAnimation">-->
			<!--Your browser does not support SVG-->
			<!--</object>-->
			<!--<img src="/static/app/img/VegItNowLogoLeaf.svg" alt="loader" height="40" class="loaderAnimation">-->
			<svg class="loaderAnimation"
			     width="40"
			     height="40"
			     version="1.1"
			     viewBox="0 0 996.70183 934.07611"
			     xml:space="preserve"
			     xmlns="http://www.w3.org/2000/svg"
			     xmlns:cc="http://creativecommons.org/ns#"
			     xmlns:dc="http://purl.org/dc/elements/1.1/"
			     xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
				<metadata>
					<rdf:RDF>
						<cc:Work rdf:about="">
							<dc:format>image/svg+xml</dc:format>
							<dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage"/>
							<dc:title/>
						</cc:Work>
					</rdf:RDF>
				</metadata>
				<g transform="matrix(1.0375 0 0 1.0375 -13.108 -20.517)" stroke-width="8.973">
					<path d="m13.221 173.43c148.06 18.843 272.78 76.271 380.46 176.77 118.44-241.37 316.75-335.59 579.66-330.21-8.0757 26.022-12.562 47.557-20.638 67.298-84.347 208.17-218.94 379.56-384.94 527.62-8.973 8.0757-13.46 26.022-12.562 38.584 4.4865 56.53 8.973 113.06-13.46 166.9-26.022 61.017-87.936 102.29-154.34 99.601-37.687-1.7946-66.401-21.535-87.936-52.044-105.88-146.26-192.92-302.39-245.86-475.57-17.946-57.427-27.816-118.44-39.481-177.67-2.6919-12.562-0.8973-25.125-0.8973-41.276z" fill="#2f6d35"/>
					<path d="m393.68 605.04c-12.562-52.044-61.017-97.806-54.736-163.31 0.8973-12.562-8.973-26.919-13.46-40.379-2.6919 0-4.4865 0.89731-7.1784 0.89731v61.017c-84.347-108.57-256.63-267.4-296.11-274.58 63.709 69.092 129.21 139.98 199.2 216.25-21.535-1.7946-31.406-2.6919-51.146-4.4865 14.357 10.768 21.535 17.946 29.611 21.535 43.968 19.741 67.298 53.838 80.757 99.601 15.254 49.352 30.508 98.703 52.044 146.26 6.2811 14.357 29.611 22.433 46.66 29.611 5.3838 1.7946 18.843-8.973 23.33-17.049 41.276-76.271 82.552-152.54 122.93-229.71 31.406-61.017 70.887-112.16 132.8-145.36 22.433-12.562 43.071-29.611 64.606-44.865-0.8973-1.7946-1.7946-4.4865-2.6919-6.2811-22.433 6.2811-43.968 12.562-69.99 18.843 74.476-87.936 161.51-153.44 264.7-198.3-56.53 13.46-113.96 27.816-164.21 54.736-50.249 26.919-92.422 67.298-133.7 97.806 0 0 1.7946-9.8704 2.6919-18.843-1.7946 0-2.6919-0.8973-4.4865-0.8973-72.682 131.9-148.06 265.6-221.63 397.51z" fill="#fff"/>
				</g>
			</svg>
		</div>

		<div class="d-flex flex-grow-1" v-if="!$root.requestsUnsatisfied">
			<NavigationBar/>
			<notifications class="m-1" position="top center"/>
			<router-view :key="$route.path" class="navbar-placeholder"/>
		</div>
		<Footer v-if="!$root.requestsUnsatisfied" :key="$route.fullPath"/>
	</div>
</template>

<script>
	import NavigationBar from './NavigationBar.vue';
	import Footer from './Footer.vue';
	import Loader from './Loader';

	export default {
		name: 'app',
		components: {
			NavigationBar,
			Footer,
			Loader
		},
		created: function () {
			let lang = this.$route.params.lang;
			if (!lang) return;
			if (Object.keys(this.$i18n.messages).includes(lang)) {
				this.$i18n.locale = lang;
				this.$cookie.set('locale', this.$i18n.locale === 'en' ? 1 : 2);
				return;
			}
			this.$router.push({path: '/' + this.$i18n.locale + '/'});
			// let userLang = navigator.language || navigator.userLanguage;
			// if (userLang && userLang.match('el')) this.$i18n.locale = 'gr';
			// this.$cookie.set('locale', this.$i18n.locale === 'en' ? 1 : 2);
		},
		head: function () {
			return this.$root.headData.defaultHead;
		}
	};
</script>

<!--<style src="static/app/css/bootstrap.min.css"></style>-->
<!--<style src="static/app/css/summernote-bs4.css"></style>-->
<!--<style src="static/app/fonts/fontawesome-free-5.5.0-web/css/all.css"></style>-->
<!--<style src="static/app/css/AlegreyaSans.css"></style>-->
<!--<style src="static/app/css/animate.css"></style>-->
<!--<style src="static/app/css/fontello.css"></style>-->
<!--<style src="static/app/css/colorPalette.css"></style>-->
<!--<style src="static/app/css/style.css"></style>-->
<style scoped>
	.centered-block {
		position: absolute;
		left: 50%;
		top: 50%;
		transform: translate(-50%, -50%);
		-webkit-transform: translate(-50%, -50%);
	}

	.loaderAnimation {
		-webkit-animation-iteration-count: infinite;
		animation-iteration-count: infinite;
		-webkit-animation-duration: 1s;
		animation-duration: 1s;
		-webkit-animation-fill-mode: both;
		animation-fill-mode: both;
		webkit-animation-name: loaderPulse;
		animation-name: loaderPulse;
	}

	@keyframes loaderPulse {
		0% {
			-webkit-transform: scale3d(1, 1, 1);
			transform: scale3d(1, 1, 1);
		}
		50% {
			-webkit-transform: scale3d(1.05, 1.05, 1.05);
			transform: scale3d(1.2, 1.2, 1.2);
		}
		100% {
			-webkit-transform: scale3d(1, 1, 1);
			transform: scale3d(1, 1, 1);
		}
	}
</style>

<style>
	.bgGreen0 {
		background-color: #2d6c13;
	}

	.bgGreenTrans0 {
		background-color: rgba(44, 107, 18, 0.75);
	}

	.bgGreen1 {
		background-color: #b6e4a2;
	}

	.bgGreen2 {
		background-color: #3da313;
	}

	.bgGreen3 {
		background-color: #d4f4c6;
	}

	.bgGreen4 {
		background-color: #e9f9e3;
	}

	.fgGreen0 {
		color: #316e17 !important;
	}

	.fgGreen1 {
		color: #327317 !important;
	}

	.fgGreen1-as-bg {
		background: #327317 !important;
	}

	.fgGray0 {
		color: #282828 !important;
	}

	.fgGray1 {
		color: #434343 !important;
	}

	body {
		background-color: #fafafa;
	}

	.dropdown-menu {
		font-size: 0.8rem;
	}

	.bg-light-gray {
		background-color: #fafafa;
	}

	.navbar-toggler {
		border: 0;
	}

	.full-screen-img {
		height: 100vh;
		background-repeat: inherit;
		background-position: center center;
		background-size: cover;
	}

	.full-box-img {
		background-repeat: inherit;
		background-position: center center;
		background-size: cover;
	}

	.carousel-blur {
		-webkit-filter: blur(50px);
		-moz-filter: blur(50px);
		-o-filter: blur(50px);
		-ms-filter: blur(50px);
		filter: blur(50px);
	}

	@media (min-width: 767px) {
		.navbar-placeholder {
			margin-top: 72px !important;
		}
	}

	.navbar-placeholder {
		/*height: 100px;*/
		/*background: #fafafa;*/
		/*margin-bottom: 20px;*/
		margin-top: 56px;
	}

	@media (min-width: 767px) {
		.h-100-minus-navbar {
			height: calc(100vh - 72px) !important;
		}
	}

	.h-100-minus-navbar {
		height: calc(100vh - 56px);
	}

	.hr-red {
		border-top: 1px solid #3da313;
	}

	.hr-black {
		border-top: 1px solid rgba(0, 0, 0, 0.1);
	}

	.hr-white {
		border-top: 1px solid white;
	}

	.bg-dark {
		background-color: #212121;
		color: white;
	}

	.btn-circle {
		height: 45px;
		width: 45px;
		border: 1px solid rgba(0, 0, 0, 0.4);
		border-radius: 100%;
	}

	@media (max-width: 576px) {
		.border-top-sm {
			border-top: 1px solid rgba(0, 0, 0, 0.125);
		}
	}

	@media (max-width: 768px) {
		.border-top-md {
			border-top: 1px solid rgba(0, 0, 0, 0.125);
		}
	}

	@media (max-width: 992px) {
		.border-top-lg {
			border-top: 1px solid rgba(0, 0, 0, 0.125);
		}
	}

	.navbar-social {
		transition: .5s;
	}

	.navbar-social:hover {
		color: #3da313 !important;
	}

	.dropdown-menu {
		background-color: #3da313;
		color: white !important;
	}

	.dropdown-menu a {
		color: white;
	}

	.navbar-item-vertical-offset {
		position: static;
	}

	@media (min-width: 768px) {
		.navbar-item-vertical-offset {
			position: absolute;
			top: 25px;
		}
	}

	.flex-basis-fix {
		flex-basis: 0;
	}

	@media (min-width: 768px) {
		.flex-basis-fix {
			flex-basis: auto;
		}
	}

	.vegShop-btn {
		display: inline-block;
		width: 100px;
		height: 40px;
		line-height: 40px;
		text-align: center;
		background-color: #3da313;
		clip-path: polygon(0% 58%, 15% 1%, 21% 0%, 28% 9%, 49% 1%, 80% 3%, 85% 1%, 100% 44%, 91% 100%, 85% 95%, 79% 97%, 19% 93%, 16% 98%, 11% 98%);
	}

	.vegShop-btn span {
		margin: auto;
		font-weight: bold;
		color: white;
	}

	.locale-btn {
		cursor: pointer;
		display: inline-block;
		width: 40px;
		height: 40px;
		line-height: 40px;
		text-align: center;
		background-color: #3da313;
		clip-path: polygon(0% 46%, 12% 13%, 10% 1%, 31% 0%, 58% 2%, 77% 1%, 93% 10%, 100% 33%, 97% 65%, 84% 92%, 74% 100%, 45% 100%, 34% 97%, 22% 100%, 9% 92%);
	}

	.locale-btn span {
		margin: auto;
		font-weight: bold;
		color: white;
	}

	@font-face {
		font-family: 'AC-ScriptCondenced_unicode';
		src: url('../../static/app/fonts/AC-ScriptCondenced_unicode.ttf') format('truetype')
	}

	h1, h2, h3, h4, h5, h6 {
		font-family: 'AC-ScriptCondenced_unicode', sans-serif;
		/*letter-spacing: 0.1em;*/
	}

	p {
		font-family: 'AlegreyaSans', sans-serif;
	}

	.sans {
		font-family: 'AC-ScriptCondenced_unicode', sans-serif;
		/*letter-spacing: 0.1em;*/
	}

	.btn {
		font-family: 'AlegreyaSans', sans-serif;
		font-weight: bold;
	}

	.btn-shadow {
		-webkit-box-shadow: 0 2px 0 0 rgba(45, 108, 19, 1), 0 4px 0 0 rgba(255, 255, 255, 1);
		-moz-box-shadow: 0 2px 0 0 rgba(45, 108, 19, 1), 0 4px 0 0 rgba(255, 255, 255, 1);
		box-shadow: 0 2px 0 0 rgba(45, 108, 19, 1), 0 4px 0 0 rgba(255, 255, 255, 1);
	}

	.animateClass {
		clip-path: polygon(20% 0%, 0% 0%, 0% 50%, 0% 80%, 0% 100%, 50% 100%, 80% 100%, 100% 100%, 100% 50%, 100% 0%, 80% 0%, 50% 0%);
		transition: -webkit-clip-path 0.2s;
	}

	.animateClass:hover {
		clip-path: polygon(20% 0%, 0% 20%, 30% 50%, 0% 80%, 20% 100%, 50% 70%, 80% 100%, 100% 80%, 70% 50%, 100% 20%, 80% 0%, 50% 30%);
	}

	.fade-enter-active {
		animation: fadeIn 1s ease-out;
	}

	@keyframes fadeIn {
		0% {
			opacity: 0;
		}
		100% {
			opacity: 1;
		}
	}


	.fade-leave-active {
		animation: fadeOut 0.3s ease-in;
	}

	@keyframes fadeOut {
		0% {
			opacity: 1;
		}
		100% {
			opacity: 0;
		}
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
		/*background-color: black;*/
		-webkit-animation: rotating 60s linear infinite;
		-moz-animation: rotating 60s linear infinite;
		-ms-animation: rotating 60s linear infinite;
		-o-animation: rotating 60s linear infinite;
		animation: rotating 60s linear infinite;
	}

	.htmlRenderer img {
		margin: 10px !important;
		max-width: 100% !important;
		height: auto !important;
	}

	.htmlRenderer iframe {
		max-width: 100% !important;
		position: relative !important;
		display: block !important;
		padding: 0 !important;
		overflow: hidden !important;
	}

	.htmlRenderer p[style*="text-align: center" i] iframe {
		margin: auto !important;
	}


	.v-icon-clock {
		mask: url(/static/app/img/icons/clock.svg?v1.0);
	}

	.v-icon-ingredients {
		mask: url(/static/app/img/icons/ingredients.svg?v1.0);
	}

	.v-icon-portions {
		mask: url(/static/app/img/icons/portions.svg?v1.0);
	}

	.v-icon {
		display: inline-block;
		width: 2rem;
		height: 2rem;
		mask-size: cover;
	}

	.box-clip-path1 {
		clip-path: polygon(2% 0%, 98% 0%, 97% 20%, 98% 70%, 96% 90%, 97.5% 95%, 98% 100%, 2% 100%, 3% 95%, 2% 80%, 2% 70%, 3% 20%);
	}

	.box-clip-path2 {
		clip-path: polygon(0% 10%, 2% 5%, 17% 2%, 30% 3%, 47% 0%, 78% 1%, 97% 5%, 100% 11%, 100% 100%, 0% 100%, 0% 10%);
	}

	.router-link-active {
		color: #495057;
		background-color: #fff;
		border-color: #dee2e6 #dee2e6 #fff !important;
	}

	.bg-blur{
		backdrop-filter: blur(4px);
	}
</style>
