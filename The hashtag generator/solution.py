def generate_hashtag(s):
    if len(s.strip()) == 0:
        return False
    
    hashtag = "#" + "".join(ele.strip().capitalize() for ele in s.split())
    return hashtag if len(hashtag) <= 140 else False
    
