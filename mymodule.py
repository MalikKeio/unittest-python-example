#!/usr/bin/env python3

def removeTags(string):
    insideTag = False
    noHTMLStr = ""
    for c in string:
        if c == "<":
            insideTag = True
        if not insideTag:
            noHTMLStr += c
        if c == ">":
            insideTag = False
    return noHTMLStr

def stripSpaces(string):
    strippedStr = ""
    string = string.strip()
    onSpaces = False
    spaceInserted = False
    for c in string:
        beforeOnSpaces = onSpaces
        onSpaces = c == " " or c == "\n"
        if not beforeOnSpaces and onSpaces:
            spaceInserted = False
        if not onSpaces:
            strippedStr += c
        elif onSpaces and not spaceInserted:
            strippedStr += " "
            spaceInserted = True
    return strippedStr

def myfunction(string):
    noHTMLStr = removeTags(string)
    strippedStr = stripSpaces(noHTMLStr)
    return strippedStr
