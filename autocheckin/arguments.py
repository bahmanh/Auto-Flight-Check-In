import argparse

def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("firstName", help="First name of passenger")
    parser.add_argument("lastName", help="Lase name of passenger")
    parser.add_argument("confNum", help="Confirmation number of flights")

    args = parser.parse_args()
    return args

