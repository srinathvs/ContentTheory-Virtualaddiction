# This file will be reomved later, is here for testing of various functionalities before it is introduced to the main
# program.

import textblob
from textblob.classifiers import NaiveBayesClassifier

train_depressed = [("I feel sad", 'dep'),
                   ("I dont feel alright", 'dep'),
                   ("I dont look forward to tomorrow", 'dep'),
                   ("I wish I werent here", 'dep'),
                   ("I want all of this to end", 'dep'),
                   ("I dont know what I am living for", 'dep'),
                   ("I am very happy with the way things are", 'happy'),
                   ("I am ok, still alive", 'dep'),
                   ("I am feeling good", 'happy'),
                   ("I never do enough", 'dep'),
                   ("I should be better", 'dep'),
                   ("I am fine", 'happy'),
                   ("I am look forward to tomorrow", 'happy'),
                   ("This is great", 'happy'),
                   ("Things aren't great", 'dep'),
                   ("Things could be better", 'dep'),
                   ("I dont want to wake up tomorrow", 'dep'),
                   ("I cant wait for tomorrow", 'happy'),
                   ("I am tired of life", 'dep'),
                   ("Life is amazing", 'happy'),
                   ("This is intriguing", 'happy'),
                   ("I feel very tired", 'dep'),
                   ("I feel alone", 'dep'),
                   ("I am feeling blesses", 'happy'),
                   ("There is too much work", 'dep'),
                   ("there isnt enough work", 'dep'),
                   ("I cant make this work", 'dep'),
                   ("I can do anything", 'happy'),
                   ("There is always a way", 'happy'),
                   ("I feel better than before", 'happy')
                   ]

test_depressed = [("I don't want to do this anymore", 'dep'),
                  ("I wish I could be better", 'dep'),
                  ("I have never been better", 'happy'),
                  ("This is the worst", 'dep'),
                  ("This is the best", 'happy'),
                  ("I am not happy", 'dep'),
                  ("I am sad", 'dep'),
                  ("I feel alone", ' dep'),
                  ("This is the best", 'happy'),
                  ("This is not good", 'dep'),
                  ("I am unhappy", 'dep'),
                  ("I dont think I can feel better", 'happy')
                  ]


cl = NaiveBayesClassifier(train_depressed)

# Get input from user here.
teststr = "I wish you would wait for me"

prob_dist = cl.prob_classify(teststr)
dep_prob = round(prob_dist.prob("dep"), 2)
print(dep_prob, "is the probability of this sentence having a depressing air")


