file { 'identify the file':
path => '/etc/ssh/ssh_config',
line => '~/.ssh/school',
}

file { 'turn off password':
path => '/etc/ssh/ssh_config',
line => 'PasswordAuthentication no',
}
