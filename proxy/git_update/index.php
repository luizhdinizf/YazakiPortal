<?php

// Use in the “Post-Receive URLs” section of your GitHub repo.


shell_exec( ‘cd /var/www/drupalsites/git-repo/ && git reset –hard HEAD && git pull’ );

?>