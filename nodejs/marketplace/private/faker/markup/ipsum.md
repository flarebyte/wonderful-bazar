
Paragraphs are separated by a blank line.

2nd paragraph. *Italic*, **bold**, `monospace`. Itemized lists
look like:

  * this one
  * that one
  * the other one

Note that -- not considering the asterisk -- the actual text
content starts at 4-columns in.


Here's a numbered list:

 1. first thing
 2. second thing
 3. third thing

Note again how the actual text starts at 4 columns in (4
characters from the left side). Here's a code sample:

    # If this makes it to 10, hold onto your hats.
    for i in 1 .. 10 { do-something(i) }

As you probably guessed, indented 4 spaces. By the way, instead of
indenting the block, you can use delimited blocks, if you like:

~~~~
define foobar() {
    print "Welcome to flavor country!";
}
~~~~

(which makes copying & pasting easier). You can optionally mark
the delimited block for Pandoc to syntax highlight it:

~~~~{.python}
import time
Quick, count to ten!
for i in range(10):
    # (but not *too* quick)
    time.sleep(0.5)
    print i
print "Ready or not, here I come!"
~~~~


Now a nested list:

 1. First, get these ingredients:

      * carrots
      * celery
      * lentils

 2. Boil some water.

 3. Dump everything in the pot and follow this algorithm:

        find wooden spoon
        uncover pot
        stir
        cover pot
        balance wooden spoon precariously on pot handle
        wait 10 minutes
        goto first step (or shut off burner when done)

Isn't it nice how text always lines up on 4-space indents?
Here's a link to [a website](http://foo.bar). Here's a link
to a [local doc](local-doc.html).

Tables look like this:

size  material      color
----  ------------  ------------
9     leather       brown
10    hemp canvas   natural
11    glass         transparent

Table: Shoes, their sizes, and what they're made of

(The above is the caption for the table.) Here's a definition
list:

apples
  : Good for making applesauce.
oranges
  : Citrus!
tomatoes
  : There's no 'e' in tomatoe.

Again, text is indented 4 spaces. (Alternately, put blank lines in
between each of the above definition list lines to spread things
out more.)