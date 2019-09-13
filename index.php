<html>
<?php  include($_SERVER['DOCUMENT_ROOT']."/template/php/header.php");?>



  <body style="margin:0px;padding:0px;overflow:hidden">
 
     <?php  include($_SERVER['DOCUMENT_ROOT']."/template/php/cabecalhoYazaki.php");?>
     <div class="list-group">
     <?php         

     $linksArray = array(
        "Formulários Moto" => "/formularios/moto",
        "Formulários Manunteção" => "/formularios/manutencao",
        "Formulários Segurança" => "/formularios/seguranca",
        "Update Raspberry Pi Screen" => "/rasp/atualizar.html",
        "Update Raspberry Pi 2 Screen" => "/rasp2/atualizar.html",
    );
     foreach ($linksArray as $key => $value){
    
    
        echo("<a href=\"./$value\" class=\"btn btn-primary\">$key</a> ");
   
     }
     
     ?>    

      </div>    
  </body>
</html>