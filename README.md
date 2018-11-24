# atthackbrno

Name:           atthackbrno
Version:        1.1
Summary:        Traffic simulator with AI
URL:            https://github.com/Lukkra211/atthackbrno/
Source0:        https://github.com/Lukkra211/atthackbrno.git
LICENCE:        MIT

Requires:       numpy
Requires:       itertools
Requires:       pygame
Requires:       yaml
Requires:       click
Requires:       time
Requires:       python3

%description
Traffic simulator using AI to optimalization traffic. For simulating we use celluar authomat.
As AI we use genethic algorithm with neural network. For GUI is used module pygame.

%files
LICENCE.txt
README.md
trafficAI/
trafficAI/automata.py  
trafficAI/control.py  
trafficAI/genetics.py  
trafficAI/graphic.py  
trafficAI/main.py  
trafficAI/map
trafficAI/map/first.yaml


