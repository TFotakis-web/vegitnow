<template>
	<div class="d-flex flex-grow-1 text-center">
		<!--<img src="/static/app/img/VegItNowLogoLeaf.svg" alt="loader" height="40" class="loaderAnimation" style="margin: auto">-->
		<!--<object type="image/svg+xml" data="/static/app/img/VegItNowLogoLeaf.svg" height="40" class="loaderAnimation" style="margin: auto">Your browser does not support SVG</object>-->
		<svg class="loaderAnimation"
		     style="margin: auto"
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
</template>

<script>
	export default {
		name: 'Loader'
	};
</script>

<style scoped>
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
