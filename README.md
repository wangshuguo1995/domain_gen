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
  </code>
</pre>

The program will terminate when <code>max_records</code> is reached or <code>ctrl-c</code> is pressed.

REQUIREMENTS: Python3

<img src="https://github.com/rootVIII/domain_gen/blob/master/sc.png" alt="example1" height="675" width="725"><hr>

This was developed on Ubuntu 18.04.4 LTS.
<hr>
<b>Author: James Loye Colley  04AUG2019</b><br><br>
