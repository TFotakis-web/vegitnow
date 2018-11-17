<template>
	<footer class="text-center"
	        style="margin-top: -4em;"
	>
		<a href="{% url 'general:home' %}" class="d-inline-block"
		   style="position: relative; top: 15px; z-index: 1049"
		>
			<img src="{% static 'img/logo.png' %}" alt="Vegitnow Logo" height="40">
		</a>
		<div id="Footer" class="bg-white text-center p-5"
		     style="
	     min-height:25vh;
         clip-path: polygon(0% 10%, 2% 5%, 17% 2%, 30% 3%, 47% 0%, 78% 1%, 97% 5%, 100% 11%, 100% 100%, 0% 100%, 0% 10%);
		"
		>
			<div class="container">
				<div class="row text-center">
					<div class="col-md-3 mb-4">
						<h1 class="fgGreen0">Join our Family</h1>
					</div>
					<div class="col-md-3 mb-4">
						<form class="form-group">
							<input class="form-control mb-1" type="email" placeholder="Insert your email..." aria-label="email"
							       style="border-bottom: solid #2d6c13 2px;border-top: 0; border-left: 0; border-right: 0;">
							<button class="btn bgGreen0 text-white form-control" style="box-shadow: none" type="submit">
								<i class="icon-mail"></i> Subscribe
							</button>
						</form>
					</div>
					<div class="col-md-3 mb-4">
						<div class="container-fluid">
							<div class="row" style="font-size: 0.7rem">
								<div class="col-md-6">
									<a href="#" class="text-dark d-block">About</a>
									<a href="#" class="text-dark d-block">Donate</a>
									<a href="#" class="text-dark d-block">Jobs</a>
									<a href="#" class="text-dark d-block">Sponsors</a>
									<a href="#" class="text-dark d-block">Products</a>
								</div>
								<div class="col-md-6">
									<a href="#" class="text-dark d-block">Press Enquiries</a>
									<a href="#" class="text-dark d-block">Contact Us</a>
									<a href="#" class="text-dark d-block">Affiliate Policy</a>
								</div>
							</div>
						</div>
					</div>
					<div class="col-md-3 mb-4">
						<h1 class="fgGreen0">FOLLOW US</h1>
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
		name: 'Footer'
	}
</script>

<style scoped>

</style>
