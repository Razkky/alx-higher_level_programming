#!/usr/bin/python3
""" Add all arguement to a list and save to a json file"""
import sys


if __name__ == "__main__":
    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file = \
        __import__("6-load_from_json_file").load_from_json_file
    try:
        curr_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        curr_list = []
    curr_list.extend(sys.argv[1:])
    save_to_json_file(curr_list, "add_item.json")
