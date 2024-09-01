from asyncio.log import logger


def filter_by_plan(items, plan):
    if plan == "free":
        filtered = items.filter(plan="free")
    elif plan == "basic":
        filtered = items.filter(plan__in=["free", "basic"])
    elif plan == "expert":
        filtered = items.filter(plan__in=["free", "basic", "expert"])
    else:
        filtered = items.none()

    logger.debug(f'Filtered items for plan {plan}: {filtered}')
    return filtered
