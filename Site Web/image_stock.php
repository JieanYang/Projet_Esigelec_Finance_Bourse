<!DOCTYPE html>
<html>

<?php
session_start();
$_SESSION['choix_action']='Korian'
?>


<head>
	<meta charset="utf-8">
	<title>page_action</title>

	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
	<script src='http://d3js.org/d3.v3.min.js' charset="utf-8"></script>
    <script src='https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.7.0/underscore-min.js' charset="utf-8"></script>


    <link rel=stylesheet href="image_stock.css" type="text/css" media=screen>

</head>
<!-- <?php
// $a=array("red","green");
// array_push($a,"blue","yellow");
// print_r($a);
?> -->
<body class="container">
	<div class="row"><?php echo $_SESSION['choix_action'];?></div>
	<div class="row">
		<div class="col-sm-8">
			<div id="image_stock"></div>
			<?php

			$choix_action = $_SESSION['choix_action'];

			$mysqli = new mysqli('localhost','root','','bdd_if');

			$query = "select * from ressources where nom_action = '$choix_action' order by date_action";
			$result = mysqli_query($mysqli, $query);

			$file = fopen('./data/aapl.csv', 'w');
			$labels = array("Date","Volume","Close");
			fputcsv($file, $labels);
			// fwrite($file, "Date\tVolume\tClose\t");
			// fwrite($file, "Date\tVolume\tClose\t");
			if(!$result){
		    	echo "La requête a échoué:".$mysqli->error;
				exit;
		    }elseif($result -> num_rows ==0){
		    	echo '<p>Aucun resultat :</p>';
		    }else{
		    	$array_date = array("date");
		    	$array_volume = array();
		    	$array_dernier = array();
		    	$i=0;
		    	while($tuple=$result->fetch_assoc()){
		    		$i++;
		    		echo $tuple['nom_action'].'||';
		    		echo $tuple['date_action'].'||';
		    		echo $tuple['dernier'].'||';
		    		echo $tuple['volume'];
		    		$BNA = $tuple['BNA'];
		    		$Dividende = $tuple['Dividende'];
		    		$Rendement = $tuple['Rendement'];
		    		$PER = $tuple['PER'];
		    		echo '<br>';
					// $list_action = array($tuple['date_action'], $tuple['dernier'], $tuple['volume']);
					$list_action = array(date('d/m/Y', strtotime($tuple['date_action'])) , $tuple['dernier'], $tuple['volume']);
					// echo explode(' ' ,$list_action[0]);
					// var_dump($list_action);
					// echo explode(' ', $tuple['date_action']);

					fputcsv($file, $list_action);
		    	}
		    }

		    mysqli_close($mysqli);
		    fclose($file);
			?>
		</div>
		<div class="col-sm-4">

			<table class="table">
			  <thead>
			    <tr>
			      <th scope="col">Cotation</th>
			      <th scope="col"></th>
			    </tr>
			  </thead>
			  <tbody>
			    <tr>
			      <th scope="row">BNA</th>
			      <td id="BNA"><?php echo $BNA;?></td>
			    </tr>
			    <tr>
			      <th scope="row">Dividende</th>
			      <td id="Dividende"><?php echo $Dividende;?></td>
			    </tr>
			    <tr>
			      <th scope="row">Rendement</th>
			      <td id="Rendement"><?php echo $Rendement;?></td>
			    </tr>
			    <tr>
			      <th scope="row">PER</th>
			      <td id="PER"><?php echo $PER;?></td>
			    </tr>
			  </tbody>
			</table>
		</div>
	</div>



	<script src="image_stock.js"></script>
</body>
</html>