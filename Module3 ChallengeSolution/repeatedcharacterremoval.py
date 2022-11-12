#Write  a  function  that  removes  repeated  characters from a string.
#a.	Sample Strings are:
#.	Hello: output should be Helo
#.	Concatenate: output should be Conaten


def removerepeated(word):
        temp = ""
        for letter in word:
            if letter not in temp:
                temp=temp+letter
        return temp

print(removerepeated("ALADEEOKO"))