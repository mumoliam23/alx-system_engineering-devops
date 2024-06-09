# Puppet manifest to fix Apache 500 error
exec { 'fix-wordpress':
  command => '/ust/bin/fix-wordpress.sh',
  path    => ['/bin', '/usr/bin'],
  }
