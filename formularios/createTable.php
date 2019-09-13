<?php
setlocale(LC_TIME, 'pt_BR', 'pt_BR.utf-8', 'pt_BR.utf-8', 'portuguese');
date_default_timezone_set('America/Sao_Paulo');
$conn = new mysqli('127.0.0.1:3307', 'yazaki', 'Yazaki1234', 'yazaki');
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
function createTableIfNew($conn, $title, $fields) {
	$sqlCheckTableExistence = "SHOW TABLES LIKE '$title'";
	$queryResultArray = array();
	$queryResult = mysqli_query($conn,$sqlCheckTableExistence);
	while($resultRow = mysqli_fetch_assoc($queryResult)) {
		$queryResultArray[] = $resultRow;
	}
	if (empty($rows)){
		$sqlCreateTable = 'CREATE TABLE `yazaki`.`';
		$sqlCreateTable .= $title;
		$sqlCreateTable .='` ( `id` INT(250) NOT NULL AUTO_INCREMENT,`data` DATETIME(5) NOT NULL,';
	
		foreach($fields as $key => $value){
			$sqlCreateTable .= '`';
			$sqlCreateTable .= $key;
			$sqlCreateTable .= '`';
			$sqlCreateTable .= " VARCHAR(50) NOT NULLL DEFAULT 'Na',";
		}
		$sqlCreateTable .= 'PRIMARY KEY (`id`) ) ENGINE = MyISAM';	   
		$conn->query($sqlCreateTable);	
		
		
		$sqlCreateResultTable ='CREATE TABLE `yazaki`.`';
		$sqlCreateResultTable .=$title;
		$sqlCreateResultTable .='_resultado';
		$sqlCreateResultTable .='` ( `id` INT(250) NOT NULL AUTO_INCREMENT,`data` DATETIME(5) NOT NULL,`maximo` INT(250),`pontos` INT(250), PRIMARY KEY (`id`) ) ENGINE = MyISAM';
		$conn->query($sqlCreateResultTable);			
	} 

 }
 $fields = $_POST;
 $titulo = $_POST['titulo'];

createTableIfNew($conn,$titulo,$fields);

?>