#kills a process through a KILLmenow file
exec { 'killmenow':
	command  => '/usr/bin/pkill killmenow',
	provider => 'shell',
	returns  => [0, 1],
}
