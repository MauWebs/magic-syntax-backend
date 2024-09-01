def get_items_by_plan(user_plan, model):
    if user_plan == 'free':
        return model.objects.filter(plan='free')
    elif user_plan == 'basic':
        return model.objects.filter(plan__in=['free', 'basic'])
    elif user_plan == 'expert':
        return model.objects.all()
    else:
        return model.objects.none()
