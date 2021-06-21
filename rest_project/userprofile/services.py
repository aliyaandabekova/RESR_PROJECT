def count_sale(profile):
    order_count = profile.order_count
    if order_count > 50 and order_count < 100:
        profile.sale = 0.1
    elif order_count > 100:
        profile.sale = 0.2
    profile.save()