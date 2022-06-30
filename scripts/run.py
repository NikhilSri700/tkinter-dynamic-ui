import sys


def describe_s3(args):
    print(f"""This script takes arguments! which are as follows:

Bucket Name: {args[0]}
Region: {args[1]}
Account ID: {args[2]}
File Name: {args[3]}
ARN: {args[4]}
Path: {args[5]}

Thank You!""")


if __name__ == '__main__':
    describe_s3(sys.argv[1:])
