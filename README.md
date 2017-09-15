<h1> am-i-pwned </h1>
<ul>
Python script that takes a file of e-mails and searches varius engines to tell you if it has been leaked online.
</ul>

<h3> Installation </h3>
        git clone https://github.com/unix121/am-i-pwned
        cd am-i-pwned/source_code
        chmod +x am-i-pwned.py

<h3> Usage </h3>
        ./am-i-pwned.py /path/to/email/file

<h3> Example </h3>
<ul>
First (if you don't already have) create a file that contains the emails you want to search for:
        $ cd /$HOME/Documents/
        $ touch emails
        $ vim emails
        (add the emails , one at each line)

Example file:
        $ cat emails
        example1@mail.com
        example2@mail.com
        example3@mail.com

Locate the script:
        $ cd /$HOME/path/to/script
        $ ./am-i-pwned.py /path/to/emails
</ul>
