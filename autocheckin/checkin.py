from checkmein import *
from arguments import *

def run():
    args = getArgs()
    checkmein = CheckMeIn(args.firstName, args.lastName, args.confNum)
    checkmein.checkIn()

if __name__ == '__main__':
    run()
