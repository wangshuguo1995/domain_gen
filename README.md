### DOMAIN GEN

###### Search for random, available, 2-word domains. Availability and price are returned.

GODADDY API Keys are required (They are free)

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
max_requests: 1500      -> max number of URLs/attempts (always printed to stdout/terminal)
write_to_file: False    -> available URLs/prices will be written to project root as JSON if set to True
  </code>
</pre>

The program will terminate when <code>max_records</code> is reached or <code>ctrl-c</code> is pressed.

<REQUIRES PYTHON3 ONLY>

<img src="https://github.com/rootVIII/domain_gen/blob/master/sc.png" alt="example1" height="675" width="950"><hr>

<ul>
    <ul>
      <li><b>Download, navigate to project root and run:</b></li>
      <li><code>pip install -e .</code></li>
      <li><b>Or install directly from Github:</b></li>
      <li><code>pip install git+https://github.com/rootVIII/tube_dream</code></li>
    </ul>
</ul>


This was developed on Ubuntu 18.04.4 LTS.
<hr>
<b>Author: James Loye Colley  04AUG2019</b><br><br>
