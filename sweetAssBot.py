import praw
import re

reddit = praw.Reddit("sweetassbot")
subreddit = reddit.subreddit("all")

for comment in subreddit.stream.comments():
    newComment = "That's a sweet ass-"
    if re.search("sweet-ass", comment.body, re.IGNORECASE):
        wordList = comment.body.split()
        for x in range(len(wordList)-1):
            if wordList[x] == "sweet-ass":
                newComment += wordList[x+1]
        comment.reply(newComment)
        print("Sent reply to ", comment.body)

