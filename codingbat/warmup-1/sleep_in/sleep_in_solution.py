# https://codingbat.com/prob/p173401
#
# The parameter weekday is True if it is a weekday, and the parameter vacation
# is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation.
# Return True if we sleep in.
# # # #
# sleep_in(False, False) → True
# sleep_in(True, False) → False
# sleep_in(False, True) → True
# sleep_in(True, True) → True


def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False
    pass


def main():
    print(sleep_in(False, False))  # → True
    print(sleep_in(True, False))  # → False
    print(sleep_in(False, True))  # → True
    print(sleep_in(True, True))  # → True
    pass


if __name__ == "__main__":
    # execute only if run as a script
    main()
    pass
