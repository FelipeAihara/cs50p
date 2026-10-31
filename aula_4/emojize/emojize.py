import sys
import emoji

emj = emoji.emojize(input("Input: "))

if (not emoji.is_emoji(emj)):
    sys.exit("Text is not an emoji")

print("Output: " + emj)
