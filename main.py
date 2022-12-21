import argparse
from datetime import datetime
from booking import booking


def main():
    parser = argparse.ArgumentParser(
        description="Tool to fight for a badminton court at UofT. The bot should be run two days in advance of the "
                    "desired date (since courts are tight like that), and within 15 minutes of the target hour (to "
                    "avoid auth timeout) "
    )
    parser.add_argument("-d", "--date", type=str, required=True, help="Datetime string of format DD/MM/YYYY")
    parser.add_argument("-t", "--time", type=int, required=True, help="24hr format hour integer, HH")
    parser.add_argument("-n", "--num", type=int, required=True, choices=[1, 2, 3], help="Court number, must be 1, 2, or 3")
    parser.add_argument("-u", "--username", type=str, required=True, help="UTORID username")
    parser.add_argument("-p", "--password", type=str, required=True, help="Password associated with UTORID")
    args = parser.parse_args()

    assert datetime.strptime(args.date, "%d/%m/%Y"), "Date given in improper format, must be DD/MM/YYYY"

    booking(args.date, args.time, args.num, args.username, args.password)


if __name__ == '__main__':
    main()
