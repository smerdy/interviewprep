#!/usr/bin/env python

import sys
# Please do not use any URL, URI, or regular expression modules or libraries.

class ParsedUrl(object):
  def __init__(self, protocol, host, pathname, query_hash):
    self.protocol = protocol
    self.host = host
    self.pathname = pathname
    self.query_hash = query_hash

  def __str__(self):
    return ', '.join([ "{k}: '{v}'".format(k=k, v=self.__dict__[k]) for k in self.__dict__ ])

  def __repr__(self):
    return self.__str__()

  @staticmethod
  def parse_from_string(input):
    splitInput = input.split('/')
    orderAndPath = '/'.join(splitInput[3:]).split('?')
    pathname = orderAndPath[0] if orderAndPath[0] else '/'
    query_hash = {}
    if len(orderAndPath) > 1: # if it has parameters
      for kwarg in orderAndPath[1].split('&'):
        kvPair = kwarg.split('=')
        query_hash[kvPair[0]] = kvPair[1]
        # casting of numeric parameters
        try:
        # assuming that numbers that can be represented as integers don't overflow...
        # and should be converted.
        # rudimentary check.
          if len(query_hash[kvPair[0]]) < 10:
            query_hash[kvPair[0]] = int(query_hash[kvPair[0]])
        except:
          pass
    return ParsedUrl(splitInput[0].strip(':'), splitInput[2], pathname, query_hash)

def main(argv):
  # Should print something like:
  # protocol: 'http', host: 'test.com:8888', pathname: 'order/search', queryHash: {keyword: awesome}
  print ParsedUrl.parse_from_string("http://test.com:8888/order/search?keyword=awesome")
  print ParsedUrl.parse_from_string("https://www.test2.com:8888/api/v1/list?keyword=awesome")
  print ParsedUrl.parse_from_string("ftp://username:password@test3.com:8888/api/v1/list?keyword=awesome&secondkey=123asdfa81214")
  print ParsedUrl.parse_from_string("sftp://www.subdomain.actual.com:8888/")
  print ParsedUrl.parse_from_string("sftp://www.subdomain.actual.com:8888")


if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))
