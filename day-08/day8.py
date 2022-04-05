# --- Day 8: Seven Segment Search ---
# You barely reach the safety of the cave when the whale smashes into the cave mouth, collapsing it. Sensors indicate another exit to this cave at a much greater depth, so you have no choice but to press on.

# As your submarine slowly makes its way through the cave system, you notice that the four-digit seven-segment displays in your submarine are malfunctioning; they must have been damaged during the escape. You'll be in a lot of trouble without them, so you'd better figure out what's wrong.

# Each digit of a seven-segment display is rendered by turning on or off any of seven segments named a through g:

#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....

#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg
# So, to render a 1, only segments c and f would be turned on; the rest would be off. To render a 7, only segments a, c, and f would be turned on.

# The problem is that the signals which control the segments have been mixed up on each display. The submarine is still trying to display numbers by producing output on signal wires a through g, but those wires are connected to segments randomly. Worse, the wire/segment connections are mixed up separately for each four-digit display! (All of the digits within a display use the same connections, though.)

# So, you might know that only signal wires b and g are turned on, but that doesn't mean segments b and g are turned on: the only digit that uses two segments is 1, so it must mean segments c and f are meant to be on. With just that information, you still can't tell which wire (b/g) goes to which segment (c/f). For that, you'll need to collect more information.

# For each display, you watch the changing signals for a while, make a note of all ten unique signal patterns you see, and then write down a single four digit output value (your puzzle input). Using the signal patterns, you should be able to work out which pattern corresponds to which digit.

# For example, here is what you might see in a single entry in your notes:

# acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
# cdfeb fcadb cdfeb cdbaf
# (The entry is wrapped here to two lines so it fits; in your notes, it will all be on a single line.)

# Each entry consists of ten unique signal patterns, a | delimiter, and finally the four digit output value. Within an entry, the same wire/segment connections are used (but you don't know what the connections actually are). The unique signal patterns correspond to the ten different ways the submarine tries to render a digit using the current wire/segment connections. Because 7 is the only digit that uses three segments, dab in the above example means that to render a 7, signal lines d, a, and b are on. Because 4 is the only digit that uses four segments, eafb means that to render a 4, signal lines e, a, f, and b are on.

# Using this information, you should be able to work out which combination of signal wires corresponds to each of the ten digits. Then, you can decode the four digit output value. Unfortunately, in the above example, all of the digits in the output value (cdfeb fcadb cdfeb cdbaf) use five segments and are more difficult to deduce.

# For now, focus on the easy digits. Consider this larger example:

# be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |
# fdgacbe cefdb cefbgd gcbe
# edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |
# fcgedb cgb dgebacf gc
# fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |
# cg cg fdcagb cbg
# fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |
# efabcd cedba gadfec cb
# aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |
# gecf egdcabf bgf bfgea
# fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |
# gebdcfa ecba ca fadegcb
# dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |
# cefg dcbef fcge gbcadfe
# bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |
# ed bcgafe cdgba cbgef
# egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |
# gbdfcae bgc cg cgb
# gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |
# fgae cfgab fg bagce
# Because the digits 1, 4, 7, and 8 each use a unique number of segments, you should be able to tell which combinations of signals correspond to those digits. Counting only digits in the output values (the part after | on each line), in the above example, there are 26 instances of digits that use a unique number of segments (highlighted above).

# In the output values, how many times do digits 1, 4, 7, or 8 appear?

notes = [line.strip() for line in open("input.txt","r")]

# Returns the union of two strings
def union(str1,str2):
    temp = str1
    for i in str2:
        if i not in str1:
            temp += i
    return temp

# Returns the substraction of two strings
def subs(str1,str2):
    for letter in str1:
        str2 = str2.replace(letter,'')
    return str2

# Returns True if all letters of str2 are in str1
def inSet(str1,str2):
    for letter in str2:
        if letter not in set(str1): 
            return False
    return True

# Finds a signal pattern for given input, returns array with matching patterns
def decode(input):
    digits = [None]*10
    # Find easy digits
    for segment in input:
        if(len(segment) == 2):   digits[1] = segment
        elif(len(segment) == 3): digits[7] = segment
        elif(len(segment) == 4): digits[4] = segment
        elif(len(segment) == 7): digits[8] = segment
    # Find other digits
    for segment in input:
        if(len(segment) == 5 and len(union(segment,digits[1])) == 5):
            digits[3] = segment
        elif(len(segment) == 5 and len(union(segment,digits[4])) == 6):
            digits[5] = segment
        elif(len(segment) == 5 and len(union(segment,digits[4])) == 7):
            digits[2] = segment
        elif(len(segment) == 6 and inSet(segment,union(digits[4],digits[7]))):
            digits[9] = segment
        elif(len(segment) == 6 and len(union(segment,digits[1])) == 7):
            digits[6] = segment
        elif(len(segment) == 6 and len(union(segment,subs(digits[1],digits[7])))):
            digits[0] = segment
    return digits

# Returns number that corresponds to given string using decoded input
def readDecoding(str, decoded):
    for i in range(len(decoded)):
        if (set(str) == set(decoded[i])):
            return i
    return -1

# Returns the number that matches 
def getNumber(input,output):
    decoded = decode(input)
    number = 0
    for i in range(len(output)):
        # print(example_out[i],"=>",readDecoding(example_out[i],bla),"*",pow(10,(3-i)))
        number += readDecoding(output[i],decoded)*pow(10,(3-i))
    return number

input_values = []
output_values = []
for line in notes:
    input,output = line.split(' | ')
    input_values.append(input.split(' '))
    output_values.append(output.split(' '))

# PART 1
total = 0
for output in output_values:
    for segment in output:
        if(len(segment) in (2,3,4,7)):
            total += 1
print("Part 1:",total)

# PART 2

# example_in = ["acedgfb","cdfbe","gcdfa","fbcad","dab","cefabd","cdfgeb","eafb","cagedb","ab"]
# example_out = ["cdfeb","fcadb","cdfeb","cdbaf"]
# bla = decode(example_in)

total = 0
for i in range(len(input_values)):
    total += getNumber(input_values[i],output_values[i])
print("Part 2:",total)