#!/usr/bin/env python3

# Todo, move to bin directory


def auth(username, password):
    print(username)


def order(args):
    pass


if __name__ == '__main__':
    # setup argument parsers
    import argparse

    from functools import wraps
    def map_subparser_to_func(func, subparser):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(subparser, *args, **kwargs)
        return wrapper

    parser = argparse.ArgumentParser(
        prog='T.O.S.T.I. CLI',
        description='Order at T.O.S.T.I.',
        epilog='Made by https://github.com/mark-boute'
    )
    subparsers = parser.add_subparsers()

    # order parser and options
    order_parser = subparsers.add_parser('order')
    order_parser.add_argument('-c', '--cheese',
                        required=False,
                        help="Add 'i' cheese tosti's to your order",
                        dest='cheese',
                        type=int, default=0,
                        metavar='i'
    )
    order_parser.add_argument('-hc', '--ham-cheese',
                        required=False,
                        help="Add 'i' ham-cheese tosti's to your order",
                        dest='ham_cheese',
                        type=int, default=0,
                        metavar='i'
    )
    order_parser.set_defaults(func= map_subparser_to_func(order, order_parser))

    # authentication parser and options
    auth_parser = subparsers.add_parser('auth')
    auth_parser.add_argument('-u', '--username',
                        required=True,
                        dest='username',
                        help="Username (s-number)",
                        type=str, default='',
                        metavar='s-number'
    )
    auth_parser.add_argument('-p', '--password',
                        required=True,
                        dest='password',
                        help="Password for s-number",
                        type=str, default='',
                        metavar='password'
    )
    auth_parser.set_defaults(func= map_subparser_to_func(auth, auth_parser))