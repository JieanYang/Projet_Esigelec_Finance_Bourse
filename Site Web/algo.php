<?php

    $bdd = mysqli_connect('localhost','root','','bdd_if');//personnaliser selon ta base de données
    //$reponse = mysqli_query($bdd,"SELECT * FROM ressources WHERE nom_action = 'Sopra Steria Group' ORDER BY date");
    // $query = "select * from ressources where nom_action = 'Sopra Steria Group' order by date_action ASC";
    $query = "select * from ressources where nom_action = 'L_oreal' order by date_action DESC";
    $reponse = mysqli_query($bdd, $query);

	$i=0;
	while(true){
		$row = $reponse -> fetch_array(MYSQLI_ASSOC);
		$data[$i]=$row;
		$i++;

		if (!$row){
		    break;
		}
	}
	// echo $i;
	// print_r($data);
	// echo "<br>";
	// print_r($data[21]);
	// echo "<br>";
	// print_r($data[21]['dernier']);


	//récupération des données dans des arrays
	for ($j=0; $j<(count($data)-1); $j++){
		$dernier[$j] = $data[$j]['dernier'];
		$haut[$j] = $data[$j]['haut'];
		$bas[$j] = $data[$j]['bas'];
		// echo $j;
	}
	// print_r($dernier);
	// echo"<br>";
	echo "<br>haut and bas";
	print_r($haut);
	echo"<br>";
	print_r($bas);

	//calcul des K sur 14 jours
	// detect max and min for 14 days
	
	for($j=0;$j<(count($dernier)-14);$j++) {
		for($i=(0+$j);$i<=(14+$j);$i++) {
			if($i==(0+$j)){
				$max_14[$j] = $haut[$i];
				$min_14[$j] = $bas[$i];
			}else{
				if($max_14[$j] < $haut[$i])
					$max_14[$j] = $haut[$i];
				if($min_14[$j] > $bas[$i])
					$min_14[$j] = $bas[$i];
			}
		}
	}
	echo "<br>max and min for 14 days";
	echo"<br>";
	print_r($max_14);
	echo"<br>";
	print_r($min_14);

	for($i=0;$i<count($max_14);$i++) {
		$k[$i] = 100*($dernier[$i]-$min_14[$i])/($max_14[$i]-$min_14[$i]);
	}
	echo"<br>";
	echo "<br>K index";
	echo"<br>";
	print_r($k);

    
    // calcul du stochastiques et des résistances, à exécuter tous les jours (au lancement par exemple)
    
    if($k[0]>80){
        $instruction = -5;//stochastique sort de la zone de sur-achat (vente)
    }
    else{
        if($k[0]<20){
            $instruction = 5;//stochastique sort de la zone de sur-vente (signal d'achat)
        }
        else{
            $instruction =0;
        }
    }
    echo "<br>first juge";
    echo "<br>".$instruction."<br>";


    if ($instruction==5)
    	echo "ACHETER";
    elseif ($instruction==-5)
    	echo "VENDRE";
    else
    	echo "NE RIEN FAIRE";


    // ??????????????????????????????????????
    //calcul des pivots
    // $pivot=($bas[0]+$haut[0]+$dernier[0])/3;
    // //calcul de la résistance
    // $R1=(2*$pivot)-$bas[0];
    // //calcul du support
    // $S1=(2*$pivot)-$haut[0];

    // //interprétation de la resistance et du support
    // if($dernier[0]>$R1){
    //     $instruction = $instruction+5;
    //     echo "<br>second juge +5";
    // }
    // if($dernier[0]<$S1){
    //     $instruction = $instruction-5;
    //     echo "<br>second juge -5 ";
    // }

    // echo "<br>".$instruction."<br>";
    
    // // arbitrage
    // if($instruction >5){
    //     echo "ACHETER";
    // }
    // else{
    //     if($instruction <=5){
    //         echo "VENDRE";
    //     }
    //     else{
    //         echo "NE RIEN FAIRE";
    //     }
    // }

 
?>