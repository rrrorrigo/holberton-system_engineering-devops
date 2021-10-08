# Sky is the limit, let's bring that limit higher
exec { 'fixing':
  path     => '/usr/bin:/usr/sbin:/bin',
  provider => shell,
  notify   => Service['nginx'],
  command  => 'sed -i \'/ULIMIT=/c\ULIMIT="-n 4069"\' /etc/default/nginx'
}
service { 'nginx' :
  ensure => 'running',
  enable => true
}