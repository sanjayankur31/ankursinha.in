I saw the code of DEATH in action!
##################################
:date: 2009-11-22 04:09
:author: ankur
:category: Tech
:tags: Linux
:slug: i-saw-the-code-of-death-in-action

For those who aren't aware,

su -

rm -rf \*

is referred to as the code of death. Really needless to explain why.
Well, I had never thought I'd see it happen, but I did. Not exactly the
above mentioned commands, but as another lethal variant:

su -

mv /\* /somedir

How and when? I was hanging out on #fedora when this dude said he needed
help. A fellow admin to his remote server had typed in the above
commands (there was lag and something something). Anyhow, so, you do the
math. We tried making a shell script to move everything back. OH! but
wait! you can only use built in shell commands. Makes it way more
tougher, doesn't it? I couldn't fix it, but I did learn some stuff
trying to.

Sent the dude to #bash, where an excellent fellow, who REALLY knew his
stuff, helped out. He compiled an executable using static linking (so it
wouldn't want the moved libs) and placed it in the dir using tcp or
something (This part I know nothing about). Since you couldn't use chmod
anymore, they overwrote an already executable binary (sorry unrar). The
file moved everything back to where it was supposed to be. This din't
come about as trivially as it sounds.

Sounds simple eh? Trust me, isn't. At least wasn't for me.

So, a close experience of the code of death. Lesson learnt : Root is
dangerous !!
