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

REQUIREMENTS: Python3

<img src="https://github.com/rootVIII/domain_gen/blob/master/sc.png" alt="example1" height="675" width="700"><hr>

This was developed on Ubuntu 18.04.4 LTS.
<hr>
<b>Author: James Loye Colley  04AUG2019</b><br><br>
