from urllib import parse

from argparse import ArgumentTypeError

# Check for valid file paths provided as command line arguments
# Following https://stackoverflow.com/questions/27494400/python-using-file-handle-to-print-contents-of-file


def is_valid_file(arg):

    try:

        return open(arg, 'r')  # return an open file handle

    except IOError:

        raise ArgumentTypeError("The file %s does not exist!" % arg)


# Encode non ascii charaters in a url
# Tip of the hat to
# https://stackoverflow.com/questions/4389572/how-to-fetch-a-non-ascii-url-with-python-urlopen/29231552


def encode_url(url):

    url = parse.urlsplit(url)

    url = list(url)

    url[2] = parse.quote(url[2])

    url = parse.urlunsplit(url)

    return url
