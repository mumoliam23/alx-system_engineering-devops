# Puppet manifest to fix Apache 500 error
exec { 'fix-error':
  command => '/bin/sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/var/www/html/wp-settings.php',
}
