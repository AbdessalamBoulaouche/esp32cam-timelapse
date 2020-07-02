<?php

$url =  'http://server_ip:port/latest/latest.jpg';

$img = 'latest.jpg';

file_put_contents($img, file_get_contents($url)); 
  
?> 

<html>
	<head>
		<meta charset="utf-8">
		
		<title>ESP32Cam Timelapse</title>
		
		<style>
		h1 {text-align: center;}
		p {text-align: center;}
		div {text-align: center;}
		</style>
	</head>
	
	<body>
		<div class="message">
			<h1>Most Recent Photo</h1>
			<p>Updated every 10 minutes. Click for full size.</p>
			<a href="latest.jpg"><img src="latest.jpg" width="800"></a>
		</div>
		
		<div class="message">
			<h1>Timelapse Video</h1>
			<p>Updated with recent footage every hour.</p>
			<video width="800" height="600" controls>
				<source src="timelapse.mp4" type="video/mp4">
			</video>
	</body>
</html>
