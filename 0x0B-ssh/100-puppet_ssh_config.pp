#using Puppet to make changes to our configuration file

file_line{'identify the file':
path => '/etc/ssh/ssh_config',
line => '~/.ssh/school',
}

file_line{'turn off password':
path => '/etc/ssh/ssh_config',
line => 'PasswordAuthentication no',
}
