<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"> 
	<meta name="viewport" content="width=device-width, initial-scale=1.0"> 
    <meta name="viewport" content="initial-scale=1, maximum-scale=1">
    <meta name="description" content="CSS Button Switches with Checkboxes and CSS3 Fanciness" />
    <meta name="keywords" content="css3, css-only, buttons, switch, checkbox, toggle, web design, web development" />
    <meta name="author" content="Codrops" />
    <link rel="shortcut icon" href="../favicon.ico"> 
    <link rel="stylesheet" type="text/css" href="css/style.css" />
	<link href='http://fonts.googleapis.com/css?family=Open+Sans+Condensed:700,300' rel='stylesheet' type='text/css' />
	<!-- Latest compiled and minified CSS -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
	<!-- jQuery library -->
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
	<!-- Popper JS -->
	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
	<!-- Latest compiled JavaScript -->
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<!-- Font awsome cdn -->
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" integrity="sha256-eZrrJcwDc/3uDhsdt61sL2oOBY362qM3lon1gyExkL0=" crossorigin="anonymous" />
	<!--Google fonts cdn-->
	<link href="https://fonts.googleapis.com/css2?family=Black+Ops+One&display=swap" rel="stylesheet">
	<link href="https://fonts.googleapis.com/css2?family=Audiowide&family=Black+Ops+One&display=swap" rel="stylesheet">
	<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
	<link rel="stylesheet" type="text/css" href="style.css">
    <link href='https://fonts.googleapis.com/css?family=Quantico' rel='stylesheet' type='text/css'>
    <link href='https://fonts.googleapis.com/css?family=Quantico' rel='stylesheet' type='text/css'>
</head>
  




<body>
	<section class="b container-fluid">
		<!--  NAV BAR START  -->
		<div class="nav">
	  		<img src="i_logo_final (1).png" class="img">
			<h1>DSRL</h1>
	  		<h2>ROBOT CONTROL</h2>
	  		<h3>CR19</h3>
	  	</div>	  	  		
		<!--<div class="slidecontainer">
			<input type="range" min="-100" max="0" value="0" class="range blue"/>
  			<p style="color:red;">Change Camera Size:</p>
  			<input type="range" min="1" max="100" value="50" align="center" class="slider">
  			<p style="color:red;">Change Screen Size:</p>
			  <p><p><input type="range" min="1" max="100" value="50" align="center" class="slider"></div></div>	
		-->	
		<!-- NAV BAR END -->
		<section class=" background">
			<div class="container-fluid">
				<!--<div class="row">
					<div class="col col-lg-2 ct1">
						<div class="row"> <button id="Ron" onclick="CallControl('uv.php', dumpData)" class="btn   c1"> Radiation On </button> </div>
						<div class="row"> <button id="Roff" onclick="CallControl('uvoff.php', dumpData)"  class="btn   c2"> Radiation Off</button> </div>-->
						
						<!--<div class="switch demo3">
					<input type="checkbox">
					<label><i></i></label>
				</div>-->
				
				<div class="row">
					<div class="col col-lg-3">
						<div class="row">							
							<div class="switch demo3">
								Radiation:
								<!--RADIATION BUTTON-->	
								<input type="checkbox" id="CB1" onclick="checkRad()" unchecked>
								<label><i></i></label>
							</div>
						</div>
						<div class="row" style="margin-left: 2.5em">			
							<div>
								Change Speed:
								<!-- SPEED CHANGE BUTTON-->
								<input type="range" min="0" max="9" step="1" oninput="speed(this.value)" onchange="speed(this.value)">
								<!--<div class="row"> <button id="Fon" onclick="CallControl('fan.php', dumpData)"  class="btn  btn-primary c3"> Fan  On </button></div>
								<div class="row"> <button id="Foff" onclick="CallControl('fanoff.php', dumpData)"  class="btn  btn-primary c4"> Fan Off </button></div>-->
							</div>
						</div>
						<div class="row" style="margin-left: 2.5em">			

							<div class="button button-1"  id="Odet">Object Detected</div>
						</div>
						<div class="row" style="margin-left: 2.5em">			
							<div class="button button-4"  id="Hdet">Human Detected</div>
						</div>
					</div>

					<div class="col col-lg-7">
						<!--VIDEO SECTION -->
						<div class="">
							<div class="embed-responsive embed-responsive-4by3 ">
								<!--<iframe class="embed-responsive-iteam responsive-iframe" src="http://192.168.43.225:5000"></iframe>-->
								<iframe class="embed-responsive-iteam responsive-iframe" src="<?php echo(getHostByName(getHostName()).":5000"); ?> "></iframe>
							</div>
						</div>
						<!--VIDEO SECTION ENDS-->
					</div>
					
					<div class="col col-lg-2">
						<div class="row">
							<!--WARNING PICTURE-->
							<div class="">
								<div class="row "> 
									<img src="warning1.jpeg" class="c7" > 
								</div>
							</div>
							<!--WARNING PICTURE ENDS-->
						</div>
						
						<div class="row" style="margin-top: 5em">			
							<table style="width:70%">
								<tr>
								  <td style="width:33%"> </td>
								  <td  style="width:33%"><button  id="for"  onclick="CallControl('for.php', dumpData)" class="btn btn-primary"> <span class="fa fa-2x fa-arrow-up"></span> </button></td>
								  <td  style="width:33%"> </td>
								</tr>
								<tr>
								  <td  style="width:33%"><button id="left"  onclick="CallControl('left.php', dumpData)" class="btn btn-primary"> <span class="fa fa-2x fa-arrow-left"></span> </button></td>
								  <td  style="width:33%"><button id="stop"  onclick="CallControl('stop.php', dumpData)" class="btn btn-primary"> <span class="fa fa-2x fa-circle-o"></span> </button></td>
								  <td  style="width:33%"><button id="right"  onclick="CallControl('right.php', dumpData)"  class="btn btn-primary"> <span class="fa fa-2x fa-arrow-right"></span> </button></td>
								</tr>
								<tr>
								  <td  style="width:33%"> </td>
								  <td  style="width:33%"><button id="back"  onclick="CallControl('back.php', dumpData)" class="btn btn-primary"> <span class="fa fa-2x fa-arrow-down"></span> </button></td>
								  <td  style="width:33%"> </td>
								</tr>
							</table>





					    </div>

					</div>



					</div>
				</div>

			</div>


			
			
			<!--<div class= 'r4' > <button class='fa fa-3x fa-angle-up'>  </button> </div>
			<div class= 'r3' > <button class='fa fa-3x fa-camera' ></button> </div>
			<div class= 'r5' > <button class='fa fa-3x fa-angle-down' ></button> </div>-->
	











		</section>
		

	</section>

	<script>
	function CallControl(theUrl, callback){
		var xmlHttp = new XMLHttpRequest();
		xmlHttp.onreadystatechange = function() { 
       	if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
           	callback(xmlHttp.responseText);
   		}
		xmlHttp.open("GET", theUrl, true); // true for asynchronous 
   		xmlHttp.send(null);
	}
	function dumpData(data){
		//DO nothing for now 
	}
	function speed(data){
		CallControl('speed.php?speed='+data, dumpData);

	}
	function checkRad(){
		var checkbox = document.getElementById('CB1');
  		if (checkbox.checked != true)
  		{
    			
                        CallControl('uvoff.php', dumpData);
  		}
		else{
			var audio = new Audio('uv.wav');
			audio.play();
			CallControl('uv.php', dumpData);
		}
	}
	function playIntro(){
            var audio = new Audio('intro.wav');
	    audio.play();
	}

		var xx = document.getElementById("Odet");
		xx.style.display = "none";
		var yy = document.getElementById("Hdet");
		yy.style.display = "none";
		function pirProc(data){  
			console.log("_____"+data+"_______"); 
			var x = document.getElementById("Hdet");
			if (data.indexOf("nopir") !== -1 ) {
				x.style.display = "none";
			} else {
				x.style.display = "block";
			}
		}
		function usProc(data){
			console.log("_____"+data+"_______"); 
			var y = document.getElementById("Odet");
			if (data.indexOf("nous") !== -1) {
				y.style.display = "none";
			} else {
				y.style.display = "block";
			}
		}
		function updateSensor(){
			CallControl('ultrasonic.php', usProc);
			CallControl('pir.php', pirProc);
			setTimeout(updateSensor, 1000);
		}
		playIntro();
		updateSensor();
	</script>


</body>
</html>
