import json


def identify_spammers(log_path):

    log_data = {}
    visited_user = set()
    visited_tweet = set()
    user_data = {}
    tweet_data = {}

    with open(log_path) as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        log_data[i] = json.loads(line)

        if log_data[i][u'user'] not in visited_user:
            visited_user.add(log_data[i][u'user'])
            user_data[log_data[i][u'user']] = []

        user_data[log_data[i][u'user']].append(log_data[i])

        if u'id' in log_data[i] and log_data[i][u'id'] not in visited_tweet:
            visited_tweet.add(log_data[i][u'id'])
            tweet_data[log_data[i][u'id']] = [(log_data[i][u'id'],log_data[i][u'timestamp'],log_data[i][u'user'])]
        if u'target_id' in log_data[i]:
            tweet_data[log_data[i][u'target_id']].append((log_data[i][u'target_id'],log_data[i][u'timestamp'],log_data[i][u'user']))


    spam_users = []
    for user in user_data.keys():

        # If all 3 are true, then spam
        criteria1 = True
        criteria2 = False
        criteria3 = True

        early_termination = False

        
        for tweet in user_data[user]:
            #TEST 1
            #User has no "action": "tweet"
            if tweet[u'action'] == u'tweet':
                criteria1 = False
                early_termination = True
                break # If original tweet, then not spam
            
            #TEST 2
            #User has at least 1 "action": "retweet" 
            if tweet[u'action'] == u'retweet':
                criteria2 = True

                #TEST 3
                #ALL retweets are <= 1000 ms of original tweet
                original_timestamp = tweet_data[tweet[u'target_id']][0][1]
                rt_timestamp = tweet[u'timestamp']

                if abs(original_timestamp - rt_timestamp) <= 1000 and criteria3:
                    criteria3 = True
                else:
                    criteria3 = False


        if early_termination:
            early_termination = False
            continue # Move on to next user

        if criteria1 and criteria2 and criteria3:
            spam_users.append(user)

    # Convert Unicode to String
    spam_users = [x.encode('UTF8') for x in spam_users]

    return spam_users