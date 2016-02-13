# This commands are not to do the real scan
# Instead, the list of commands can identify a good zombie system.

use auxiliary/scanner/ip/ipidseq
set RHOSTS 10.10.10.0/24
set THREADS 25
show options
run