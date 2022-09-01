#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        track_value = 0
        track_key = ''
        for key, value in a_dictionary.items():
            if value > track_value:
                track_value = value
                track_key = key
        return track_key
    return None
