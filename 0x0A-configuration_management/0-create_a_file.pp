# Create a file in /tmp

file{'school':
path => '/tmp/school',
mode => '0744',
content => 'I love Puppet',
group => 'www-data',
owner => 'www-data',
ensure => 'present',
}
