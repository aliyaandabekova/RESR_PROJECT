def comment_validate(text):
    bad_word = 'bad'
    text = text.lower()
    if bad_word not in text:
        return True
    return False

def count_avg_score(score_list,product):
    avg_score = 0
    amount = len(score_list)
    for obj in score_list:
        avg_score += obj.score
    avg_score /= amount
    product.avg_score = avg_score
    product.save()
