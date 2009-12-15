#!/usr/bin/python
#
# Peteris Krumins (peter@catonmat.net)
# http://www.catonmat.net  --  good coders code, great reuse
#
# The new catonmat.net website. See this post for more info:
# http://www.catonmat.net/blog/50-ideas-for-the-new-catonmat-website/
#
# Code is licensed under GNU GPL license.
#

class Quote(object):
    def __init__(self, quote, author):
        self.quote = quote
        self.author = author

    def __repr__(self):
        return "<quote by %s>" % self.author

# TODO:
# http://stackoverflow.com/questions/58640/great-programming-quotes

quotes = (
    Quote("Person who say it cannot be done should not interrupt person doing it.", "Chinese Proverb"),
    Quote("Being an expert in XML is like being an expert in comma-separated values.", "Terence Parr"),
    Quote("The error message is God.", "mjd"),
    Quote("If you lie to the compiler, it will get its revenge.", "Henry Spencer"), 
    Quote("Trying to outsmart a compiler defeats much of the purpose of using one.", "Kernighan & Plauger"), 
    Quote("It's hard enough to find an error in your code when you're looking for it; it's even harder when you've assumed your code is error-free.", "Steve McConnell"), 
    Quote("If builders built buildings the way programmers wrote programs, then the first woodpecker that came along would destroy civilisation.", "Gerald Weinberg"), 
    Quote("Programming can be fun, so can cryptography; however they should not be combined.", "Kreitzberg and Shneiderman"), 
    Quote("Once a new technology starts rolling, if you're not part of the steamroller, you're part of the road.", "Stewart Brand"), 
    Quote("The truth does not change according to our ability to stomach it.", "Flannery O'Connor"), 
    Quote("Let us change our traditional attitude to the construction of programs. Instead of imagining that our main task is to instruct a computer what to to, let us concentrate rather on explaining to human beings what we want a computer to do.", "Donald Knuth"), 
    Quote("Beware of bugs in the above code; I have only proved it correct, not tried it.", "Donald Knuth"), 
    Quote("Computers are good at following instructions, but not at reading your mind.", "Donald Knuth"), 
    Quote("The designer of a new system must not only be the implementor and the first large-scale user; the designer should also write the first user manual.", "Donald Knuth"), 
    Quote("Any inaccuracies in this index may be explained by the fact that it has been sorted with the help of a computer.", "Donald Knuth"), 
    Quote("TeX has found at least one bug in every Pascal compiler it's been run on, I think, and at least two in every C compiler.", "Donald Knuth"), 
    Quote("The process of preparing programs for a digital computer is especially attractive, not only because it can be economically and scientifically rewarding, but also because it can be an aesthetic experience much like composing poetry or music.", "Donald Knuth"), 
    Quote("You're bound to be unhappy if you optimize everything.", "Donald Knuth"), 
    Quote("These machines have no common sense; they have not yet learned to 'think,' and they do exactly as they are told, no more and no less. This fact is the hardest concept to grasp when one first tries to use a computer.", "Donald Knuth"), 
    Quote("We should forget about small efficiencies, say about 97% of the time: premature optimization is the root of all evil.", "Donald Knuth"), 
    Quote("Good code is its own best documentation. As you're about to add a comment, ask yourself, 'How can I improve the code so that this comment isn't needed?' Improve the code and then document it to make it even clearer.", "Steve McConnell"), 
    Quote("The trouble with the world is that the stupid are cocksure and the intelligent are full of doubt.", "Bertrand Russell"), 
    Quote("A charlatan makes obscure what is clear; a thinker makes clear what is obscure.", "Hugh Kingsmill"), 
    Quote("Unformed people delight in the gaudy and in novelty. Cooked people delight in the ordinary.", "Erik Naggum"), 
    Quote("An organisation that treats its programmers as morons will soon have programmers that are willing and able to act like morons only.", "Bjarne Stroustrup"), 
    Quote("Measuring programming progress by lines of code is like measuring aircraft building progress by weight.", "Bill Gates"), 
    Quote("The first 90% of the code accounts for the first 90% of the development time. The remaining 10% of the code accounts for the other 90% of the development time.", "Tom Cargill"), 
    Quote("Before software can be reusable it first has to be usable.", "Ralph Johnson"), 
    Quote("Programmers are in a race with the Universe to create bigger and better idiot-proof programs, while the Universe is trying to create bigger and better idiots. So far the Universe is winning.", "Anon"), 
    Quote("Two things are infinite: the universe and human stupidity; and I'm not sure about the universe.", "Albert Einstein"), 
    Quote("Just because the standard provides a cliff in front of you, you are not necessarily required to jump off it.", "Norman Diamond"), 
    Quote("But in our enthusiasm, we could not resist a radical overhaul of the system, in which all of its major weaknesses have been exposed, analyzed, and replaced with new weaknesses.", "Bruce Leverett"), 
    Quote("The best performance improvement is the transition from the nonworking state to the working state ", "John Ousterhout"), 
    Quote("Real computer scientists despise the idea of actual hardware. Hardware has limitations, software doesn't. It's a real shame that Turing machines are so poor at I/O.", "Anon"), 
    Quote("There are only two industries that refer to their customers as 'users'.", "Edward Tufte"), 
    Quote("Debugging a Direct3D application can be challenging.", "Microsoft's Direct3D Immediate Mode overview."), 
    Quote("There are two ways to write error-free programs; only the third works.", "Alan J. Perlis"), 
    Quote("To many managers, getting rid of the arrogant, undisciplined, over-paid, technology-obsessed, improperly-dressed programmers would appear to be a significant added benefit.", "Bjarne Stroustrup"), 
    Quote("I did say something along the lines of 'C makes it easy to shoot yourself in the foot; C++ makes it harder, but when you do, it blows your whole leg off.' ", "Bjarne Stroustrup"), 
    Quote("I have always wished that my computer would be as easy to use as my telephone. My wish has come true. I no longer know how to use my telephone.", "Bjarne Stroustrup"), 
    Quote("The most important single aspect of software development is to be clear about what you are trying to build.", "Bjarne Stroustrup"), 
    Quote("If you think your management doesn't know what it's doing or that your organisation turns out low-quality software crap that embarrasses you, then leave.", "Edward Yourdon"), 
    Quote("Most of you are familiar with the virtues of a programmer. There are three, of course: laziness, impatience, and hubris.", "Larry Wall"), 
    Quote("It has been said that the great scientific disciplines are examples of giants standing on the shoulders of other giants. It has also been said that the software industry is an example of midgets standing on the toes of other midgets.", "Alan Cooper"), 
    Quote("The road to wisdom? Well its plain and simple to express: Err and err and err again,	but less and less and less.", "Piet Hein"), 
    Quote("There are perhaps 5% of the population that simply *can't* think. There are another 5% who *can*, and *do*. The remaining 90% *can* think, but *don't*.", "R. A. Heinlein"), 
    Quote("Lord, give us the wisdom to utter words that are gentle and tender, for tomorrow we may have to eat them.", "Sen. Morris Udall"), 
    Quote("Do not worry about your difficulties in mathematics, I assure you that mine are greater.", "Einstein"), 
    Quote("Computers are useless. They can only give you answers.", "Pablo Picasso"), 
    Quote("Theory is when you know something, but it doesn't work. Practice is when something works, but you don't know why. Programmers combine theory and practice: Nothing works and they don't know why.", "unknown"), 
    Quote("I really hate this damned machine. I wish that they would sell it. It never does quite what I want. But only what I tell it.", "A Programmer's Lament"), 
    Quote("UNIX is simple. It just takes a genius to understand its simplicity.", "Dennis Ritchie"), 
    Quote("When someone says, 'I want a programming language in which I need only say what I want done,' give him a lollipop.", "Alan Perlis"), 
    Quote("For every complex problem there is an answer that is clear, simple, and wrong.", "H L Mencken"), 
    Quote("One of the main causes of the fall of the Roman Empire was that, lacking zero, they had no way to indicate successful termination of their C programs.", "Robert Firth"), 
    Quote("Haste is of the devil. Slowness is of God.", "H L Mencken"), 
    Quote("If the code and the comments disagree, then both are probably wrong.", "Norm Schryer"), 
    Quote("Good programmers use their brains, but good guidelines save us having to think out every case.", "Francis Glassborow"), 
    Quote("Never ascribe to malice that which is adequately explained by incompetence ", "Napoleon Bonaparte"), 
    Quote("Sufficiently advanced incompetence is indistinguishable from malice.", "unknown"), 
    Quote("And the users exclaimed with a laugh and a taunt: 'It's just what we asked for but not what we want.' ", "unknown"), 
    Quote("Some problems are so complex that you have to be highly intelligent and well informed just to be undecided about them.", "Laurence J. Peter"), 
    Quote("The Six Phases of a Project: Enthusiasm, Disillusionment, Panic, Search for the Guilty, Punishment of the Innocent, Praise for non-participants.", "unknown"), 
    Quote("Those who cannot remember the past are condemned to repeat it.", "George Santayana"), 
    Quote("Fashion is something barbarous, for it produces innovation without reason and imitation without benefit.", "George Santayana"), 
    Quote("For a sucessful technology, honesty must take precedence over public relations for nature cannot be fooled.", "Richard Feynman"), 
    Quote("The inside of a computer is as dumb as hell but it goes like mad! ", "Richard Feynman"), 
    Quote("A most important, but also most elusive, aspect of any tool is its influence on the habits of those who train themselves in its use. If the tool is a programming language this influence is, whether we like it or not, an influence on our thinking habits.", "Edsger Dijkstra"), 
    Quote("To iterate is human, to recurse divine.", "L. Peter Deutsch"), 
    Quote("There's no sense being exact about something if you don't even know what you're talking about.", "John von Neumann"), 
    Quote("Anyone who considers arithmetical methods of producing random numbers is, of course, in a state of sin.", "John von Neumann"), 
    Quote("There are two ways of constructing a software design. One way is to make it so simple that there are obviously no deficiencies. And the other way is to make it so complicated that there are no obvious deficiencies.", "C.A.R. Hoare"), 
    Quote("The cost of adding a feature isn't just the time it takes to code it. The cost also includes the addition of an obstacle to future expansion. The trick is to pick the features that don't fight each other.", "John Carmack"), 
    Quote("You can't have great software without a great team, and most software teams behave like dysfunctional families.", "Jim McCarthy"), 
    Quote("Even if you're on the right track, you'll get run over if you just sit there.", "Will Rogers"), 
    Quote("That's the thing about people who think they hate computers. What they really hate is lousy programmers.", "Larry Niven"), 
    Quote("That's the thing about people who think they hate computers. What they really hate is lousy programmers.", "Jerry Pournelle"), 
    Quote("Trying to get into the details seems to be a religious issue -- nearly everybody is convinced that every style but their own is ugly and unreadable. Leave out the 'but their own' and they're probably right...", "Jerry Coffin on indentation"), 
    Quote("When you start off by telling those who disagree with you that they are not merely in error but in sin, how much of a dialogue do you expect?", "Thomas Sowell"), 
    Quote("Einstein argued that there must be simplified explanations of nature, because God is not capricious or arbitrary. No such faith comforts the software engineer.", "Fred Brooks, Jr."), 
    Quote("Incompetents invariably make trouble for people other than themselves.", "Larry McMurtry"), 
    Quote("A notation is important for what it leaves out.", "Joseph Stoy"), 
    Quote("As we said in the preface to the first edition, C 'wears well as one's experience with it grows.' With a decade more experience, we still feel that way.", "Brian Kernighan and Dennis Ritchie"), 
    Quote("A mathematician is a machine for turning coffee into theorems.", "Paul Erdos"), 
    Quote("PHP is a minor evil perpetrated and created by incompetent amateurs, whereas Perl is a great and insidious evil, perpetrated by skilled but perverted professionals.", "Jon Ribbens"), 
    Quote("Simplicity is prerequisite for reliability.", "Edsger W.Dijkstra"), 
    Quote("I've finally learned what 'upward compatible' means. It means we get to keep all our old mistakes.", "Dennie van Tassel"), 
    Quote("Exceptions relieve the programmer of tedious writing boilerplate code -- without removing the semantics of said code -- and they allow the programmer to arrange the code so that error handling code is more separate from the main program logic.", "Herb Sutter"), 
    Quote("It is difficult to get a man to understand something when his salary depends on his not understanding it.", "Upton Sinclair"), 
    Quote("Some people, when confronted with a problem, think 'I know, I'll use regular expressions.' Now they have two problems.", "Jamie Zawinski"), 
    Quote("The behavior of any bureaucratic organization can best be understood by assuming that it is controlled by a secret cabal of its enemies.", "Robert Conquest's Second Law of Politics"), 
    Quote("Power is the ability to control things, moral authority is the ability to change things ", "Jim Wallis"), 
    Quote("The open secrets of good design practice include the importance of knowing what to keep whole, what to combine, what to separate, and what to throw away.", "Kevlin Henny"), 
    Quote("Rules of Optimization: Rule 1: Don't do it. Rule 2 (for experts only): Don't do it yet.", "M.A. Jackson"), 
    Quote("More computing sins are committed in the name of efficiency (without necessarily achieving it) than for any other single reason - including blind stupidity.", "W.A. Wulf"), 
    Quote("The best is the enemy of the good.", "Voltaire"), 
    Quote("There's a fine line between being on the leading edge and being in the lunatic fringe.", "Frank Armstrong"), 
    Quote("The pessimist complains about the wind; the optimist expects it to change; the realist adjusts the sails.", "William Arthur Ward"), 
    Quote("Good judgement comes from experience, and experience comes from bad judgement.", "Fred Brooks"), 
    Quote("Plan to throw one away, you will anyhow.", "Fred Brooks"), 
    Quote("If you plan to throw one away, you will throw away two.", "Craig Zerouni"), 
    Quote("Learning is not compulsory. Neither is survival.", "W. Edwards Deming"), 
    Quote("C++ tries to guard against Murphy, not Machiavelli.", "Damian Conway"), 
    Quote("I have always found that plans are useless, but planning is indispensable.", "Dwight Eisenhower"), 
    Quote("We are tied down to a language which makes up in obscurity what it lacks in style.", "Tom Stoppard"), 
    Quote("They always say time changes things, but you actually have to change them yourself.", "Andy Warhol"), 
    Quote("We only acknowledge small faults in order to make it appear that we are free from great ones.", "La Rochefoucauld"), 
    Quote("Most software today is very much like an Egyptian pyramid with millions of bricks piled on top of each other, with no structural integrity, but just done by brute force and thousands of slaves.", "Alan Kay"), 
    Quote("We all agree on the necessity of compromise. We just can't agree on when it's necessary to compromise.", "Larry Wall"), 
    Quote("Perl is another example of filling a tiny, short-term need, and then being a real problem in the longer term.", "Alan Kay"), 
    Quote("The competent programmer is fully aware of the strictly limited size of his own skull; therefore he approaches the programming task in full humility, and among other things he avoids clever tricks like the plague.", "Edsger Dijkstra"), 
    Quote("It is practically impossible to teach good programming style to students that have had prior exposure to Basic; as potential programmers they are mentally mutilated beyond hope of regeneration.", "Edsger Dijkstra"), 
    Quote("We are apt to shut our eyes against a painful truth.... For my part, I am willing to know the whole truth; to know the worst; and to provide for it.", "Patrick Henry"), 
    Quote("A non-virtual function says, you have to do this and you must do it this way. A virtual function says you have to do this, but you don't have to do it this way. That's their fundamental difference.", "Scott Meyers"), 
    Quote("Comparing to another activity is useful if it helps you formulate questions, it's dangerous when you use it to justify answers.", "Martin Fowler"), 
    Quote("Correctness is clearly the prime quality. If a system does not do what it is supposed to do, then everything else about it matters little.", "Bertrand Meyer"), 
    Quote("An API that isn't comprehensible isn't usable.", "James Gosling"), 
    Quote("Style distinguishes excellence from accomplishment.", "James Coplien"), 
    Quote("You know you've achieved perfection in design, not when you have nothing more to add, but when you have nothing more to take away.", "Antoine de Saint-Exupery, Wind, Sand and Stars"), 
    Quote("It always takes longer than you expect, even when you take into account Hofstadter's Law.", "Hofstadter's Law"), 
    Quote("The ability to simplify means to eliminate the unnecessary so that the necessary may speak.", "Hans Hoffmann"), 
    Quote("Simplicity carried to the extreme becomes elegance.", "Jon Franklin"), 
    Quote("Simplicity is the ultimate sophistication.", "Leonardo da Vinci"), 
    Quote("It's so easy to become mesmerized by the immediacy of a result that you don't question its validity.", "Naomi Karten"), 
    Quote("Every program has (at least) two purposes: the one for which it was written, and another for which it wasn't.", "Alan J. Perlis"), 
    Quote("Elegance is not optional ", "Richard O'Keefe"), 
    Quote("The most amazing achievement of the computer software industry is its continuing cancellation of the steady and staggering gains made by the computer hardware industry.", "Henry Petroski"), 
    Quote("Technology is dominated by two types of people: Those who understand what they do not manage. Those who manage what they do not understand.", "Putt's Law"), 
    Quote("Copy and paste is a design error ", "David Parnas"), 
    Quote("There is not now, nor has there ever been, nor will there ever be, any programming language in which it is the least bit difficult to write bad code.", "Flon's Law"), 
    Quote("Any code of your own that you haven't looked at for six or more months might as well have been written by someone else.", "Eagleson's law"), 
    Quote("If you can't be a good example, then you'll just have to be a horrible warning.", "Catherine Aird"), 
    Quote("Alas, to wear the mantle of Galileo it is not enough that you be persecuted by an unkind establishment, you must also be right.", "Bob Park"), 
    Quote("Any fool can use a computer. Many do.", "Ted Nelson"), 
    Quote("Say what you will about the Ten Commandments, you must always come back to the pleasant fact that there are only ten of them.", "H. L. Mencken"), 
    Quote("Incorrect documentation is often worse than no documentation.", "Bertrand Meyer"), 
    Quote("Debugging is twice as hard as writing the code in the first place. Therefore, if you write the code as cleverly as possible, you are, by definition, not smart enough to debug it.", "Brian W. Kernighan"), 
    Quote("If the lessons of history teach us anything it is that nobody learns the lessons that history teaches us.", "unknown"), 
    Quote("The primary duty of an exception handler is to get the error out of the lap of the programmer and into the surprised face of the user. Provided you keep this cardinal rule in mind, you can't go far wrong.", "Verity Stob"), 
    Quote("If you want a product with certain characteristics, you must ensure that the team has those characteristics before the product's development.", "Jim and Michele McCarthy"), 
    Quote("Organizations which design systems are constrained to produce designs which are copies of the communication structures of these organizations. (For example, if you have four groups working on a compiler, you'll get a 4-pass compiler)", "Damien Conway (Conway's Law)"), 
    Quote("It's not at all important to get it right the first time. It's vitally important to get it right the last time.", "Andrew Hunt and David Thomas")
)

