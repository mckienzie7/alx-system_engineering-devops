# install Flask from PIP3

exec { 'flask':
  command => 'pip3 install flask',
  cwd => 'pip3',
} 
