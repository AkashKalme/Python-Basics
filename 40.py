# Short Circuiting: OR is short circuting
is_friend = True
is_user = True

# Both conditions are evaluated
if is_friend and is_user:
    print("Best Friends")

# If first one is True, then second condition is not evaluated
if is_friend or is_user:
    print("Best Friends")
