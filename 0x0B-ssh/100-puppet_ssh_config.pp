#using Puppet to make changes to our configuration file

file{'identify the file':
path => '/etc/ssh/ssh_config',
line => 'IdentityFile ~/.ssh/school',
}

file{'turn off password':
path => '/etc/ssh/ssh_config',
line => 'PasswordAuthentication no',
}
