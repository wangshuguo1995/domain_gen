### DOMAIN GEN

###### Search for random, available, 2-word domains. Availability and price are returned.

<b>GODADDY API Keys are required (They are free)</b>

Save them as environment variables regardless of your system.<br>
They must be named as follows:

<pre>
  <code>
GODADDY_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
GODADDY_SECRET=xxxxxxxxxxxxxxxxxxxxxxx
  </code>
</pre>


Set entries in <code>domain_gen/resources/config.yml</code> for:

<pre>
  <code>
tld: .com               -> top level domain   (.com  .org  .net  .io   etc... include the leading '.')
max_requests: 100       -> max number of URLs/attempts (always printed to stdout/terminal)
write_to_file: False    -> available URLs/prices will be written to project root as JSON if set to True
interval: 60            -> time in seconds to wait between intervals
default_word:
  use_default: True     -> True/False - if True the word will be used in each random domain test
  word: word_here       -> The word that will be paired with a random word
  position: 1           -> 1 or 2 - The position that the default word will appear.
 
 
 
If 'use_default' is True, 'word' will be used in each request at the
given 'position' (1 or 2). If 'word' is set to apple, and position
is 1, all domains found will use apple as the first word along with a
random second word for each domain.

EX: appletest.com appletuesday.com appleword.com...

Use position 2 if you want the first word to be random:

EX: catapple.com plasticapple.com outrageousapple.com
 
  </code>
</pre>


<pre>
  <code>

Unfortunatley Godaddy has API restrictions that block repeated calls in succession (after 100-150?).
Therefore Domain Gen will make requests until max_requests is reached and then sleep for 60 seconds.
The process is repeated indefinitely until <code>ctrl-c</code> is pressed.


Therefore max_requests should be left at about 100 (lots of redlines in stdout is a sign that requests
are being blocked). The interval should be set to 60 seconds or so.

These values can be 'tuned' to display as many domains as possible without error for a given interval.

  </code>
</pre>

REQUIREMENTS: any OS with Python3

USAGE: python3 domain_gen.py

<img src="https://github.com/rootVIII/domain_gen/blob/master/sc.png" alt="example1">
<hr>

Apple used as default position 1:
<img src="https://github.com/rootVIII/domain_gen/blob/master/sc2.png" alt="example2">
<hr>

Apple used as default position 2:
<img src="https://github.com/rootVIII/domain_gen/blob/master/sc3.png" alt="example3">
<hr>

No default word (random pair):
<img src="https://github.com/rootVIII/domain_gen/blob/master/sc4.png" alt="example4">
<hr>
This was developed on Ubuntu 18.04.4 LTS.
<hr>
<b>Author: James Loye Colley  04AUG2019</b><br><br>
