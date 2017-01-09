#!/usr/bin/env python3

"""Generate function"""

import random
import sys
#import ..hparser.parseOptions

try:
    print("NOTE: --help is not working yet")
    PRINT_COMMENT = sys.argv[1]
except IndexError:
    PRINT_COMMENT = ""


comments = {
    "COMMENT_CUT": "Cut",
    "COMMENT_PASTE": "Paste",
    "COMMENT_SELECT_ALL": "Select all",
    "COMMENT_KEYPRESS_ENTER": "Keypress 'Enter'",
    "COMMENT_KEYPRESS_UP": "Keypress 'Up'",
    "COMMENT_KEYPRESS_DOWN": "Keypress 'Down'",
    "COMMENT_KEYPRESS_LEFT": "Keypress 'Left'",
    "COMMENT_KEYPRESS_RIGHT": "Keypress 'Right'",
    "COMMENT_KEYPRESS_A": "Keypress 'A'",
    "COMMENT_KEYPRESS_B": "Keypress 'B'",
}

actionToComment = {
    "com.cut()": comments["COMMENT_CUT"],
    "com.paste()": comments["COMMENT_PASTE"],
    "com.select_all()": comments["COMMENT_SELECT_ALL"],
    "type(Key.ENTER)": comments["COMMENT_KEYPRESS_ENTER"],
    "type(Key.UP)": comments["COMMENT_KEYPRESS_UP"],
    "type(Key.DOWN)": comments["COMMENT_KEYPRESS_DOWN"],
    "type(Key.LEFT)": comments["COMMENT_KEYPRESS_LEFT"],
    "type(Key.RIGHT)": comments["COMMENT_KEYPRESS_RIGHT"],
    "type(Key.A)": comments["COMMENT_KEYPRESS_A"],
    "type(Key.B)": comments["COMMENT_KEYPRESS_B"],
}

actions = [
    "com.cut()",
    "com.paste()",
    "com.select_all()",
    "type(Key.ENTER)",
    "type(Key.UP)",
    "type(Key.DOWN)",
    "type(Key.LEFT)",
    "type(Key.RIGHT)",
    "type(Key.A)",
    "type(Key.B)",
]

def create():
    print(startup())
    for i in range(999):
        aSeed = random.randint(0,len(actions)-1)
        output = actions[aSeed] + ";"
        if PRINT_COMMENT == "print":
            output += "  # " + actionToComment[actions[aSeed]]
            # output = "\n# " + actionToComment[actions[aSeed]] + "\n" + output
        print(output)
    print(shutdown())

def startup():
    return """
# https://raw.githubusercontent.com/Mozilla-TWQA/Hasal/487f7a6/tests/regression/gdoc/test_chrome_gdoc_create_copypaste_image_1.sikuli/test_chrome_gdoc_create_copypaste_image_1.py
# if you are putting your test script folders under {git project folder}/tests/, it will work fine.
# otherwise, you either add it to system path before you run or hard coded it in here.
sys.path.append(sys.argv[2])
import browser
import common
import gdoc

com = common.General()
chrome = browser.Chrome()
gd = gdoc.gDoc()

chrome.clickBar()
chrome.enterLink(sys.argv[3])
sleep(5)
gd.wait_for_loaded()
gd.insert_image_url("https://drive.google.com/open?id=0B9Zi9TqbRWsdTV9JTmZQUXRFTWM")
sleep(5)

# DDBEGIN
"""

def shutdown():
    return """
# DDEND

gd.deFoucsContentWindow()
"""