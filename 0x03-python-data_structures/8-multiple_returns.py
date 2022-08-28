#!/usr/bin/python3
def multiple_return(sentence):
    if not sentence:
        return (len(sentence), None)
    return (len(sentence), sentence[0])
