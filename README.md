# Twitter-Spam-Bot-Detector

## Scenario:
You have access to platform's activity log (available at ```/home/candidate/candidate_files/py/inputs```).

The structure of the activity log is described in ```/home/candidate/candidate_files/py/log-structure.txt```

We consider am user to be a spammer if it satisfies all the following criteria:
- The user has no original tweets.
- The user has at least one retweet.
- All the retweets of this user occur within 1000 milliseconds of the original tweet.

## Task:
Write the function ```identify_spammers``` that accepts the absolute path of the activity logfile, and returns a list of all the spammer usernames.

## Additional requirements:
- In the corner case where the retweet occurs exactly 1000 milliseconds after the original tweet, it should also be considered as a spam retweet.
- The output list must not contain duplicates.
- The order of the output list does not matter.

## Assumptions:
- The ```log_path``` supplied to the ```identify_spammers``` function is guaranteed to point to a file that exists, and can be read.
- All entries in the activity log are chronologically ordered.

