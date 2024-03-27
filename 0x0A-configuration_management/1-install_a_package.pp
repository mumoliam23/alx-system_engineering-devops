# Define a resource class for managing pip packages
class pip::package { 
  $name;
  $version;

  # Ensure pip3 is available
  require => Package['python3-pip'];

  # Use pip3 to install the package
  exec { "install-${name}"
    command => "/usr/bin/pip3 install ${name}==${version}",
  }

  # Refresh the package manager cache after installation
  exec { "update_cache_${name}"
    command => "/usr/bin/pip3 cache update",
    refreshonly => true,
  }
}

# Install Flask package with version 2.1.0
pip::package { 
  name => 'Flask',
  version => '2.1.0',
}

