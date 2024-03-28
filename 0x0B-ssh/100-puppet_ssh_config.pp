#using Puppet to make changes to our configuration file

file{'turn off password':
path => '/etc/ssh/ssh_config',
line => 'PasswordAuthentication no',
}

file{'identify the file':
path => '/etc/ssh/ssh_config',
line => '~/.ssh/school',
}
