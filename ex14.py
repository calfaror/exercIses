from sys import argv

script, user_name, color = argv
donut = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(donut)

print "Where do you live %s?" % user_name
lives = raw_input(donut)

print "What kind of computer do you have?"
computer = raw_input(donut)

print "what is %s your favorite color?" % color
color = raw_input(donut)

print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer. 
And you like %r. Nice.
""" % (likes, lives, computer, color)