# -*- coding: utf-8 -*-
### Automatically generated by repyhelper.py ### /Users/tomashasselquist/git/tda596/demokit/urlparse.repy

### THIS FILE WILL BE OVERWRITTEN!
### DO NOT MAKE CHANGES HERE, INSTEAD EDIT THE ORIGINAL SOURCE FILE
###
### If changes to the src aren't propagating here, try manually deleting this file. 
### Deleting this file forces regeneration of a repy translation


from repyportability import *
import repyhelper
mycontext = repyhelper.get_shared_context()
callfunc = 'import'
callargs = []

"""
<Program Name>
  urlparse.repy

<Started>
  May 15, 2009

<Author>
  Michael Phan-Ba

<Purpose>
  Provides utilities for parsing URLs, based on the Python 2.6.1 module urlparse.

"""


def urlparse_urlsplit(urlstring, default_scheme="", allow_fragments=True):
  """
  <Purpose>
    Parse a URL into five components, returning a dictionary.  This corresponds
    to the general structure of a URL:
    scheme://netloc/path;parameters?query#fragment.  The parameters are not
    split from the URL and individual componenets are not separated.

    Only absolute server-based URIs are currently supported (all URLs will be
    parsed into the components listed, regardless of the scheme).

  <Arguments>
    default_scheme:
      Optional: defaults to the empty string.  If specified, gives the default
      addressing scheme, to be used only if the URL does not specify one.

    allow_fragments:
      Optional: defaults to True.  If False, fragment identifiers are not
      allowed, even if the URL's addressing scheme normally does support them.

  <Exceptions>
    ValueError on parsing a non-numeric port value.

  <Side Effects>
    None.

  <Returns>
    A dictionary containing:

    Key         Value                               Value if not present
    ============================================================================
    scheme      URL scheme specifier                empty string
    netloc      Network location part               empty string
    path        Hierarchical path                   empty string
    query       Query component                     empty string
    fragment    Fragment identifier                 empty string
    username    User name                           None
    password    Password                            None
    hostname    Host name (lower case)              None
    port        Port number as integer, if present  None

  """

  components = {"scheme": default_scheme, "netloc": "", "path": "", "query": "",
    "fragment": "", "username": None, "password": None, "hostname": None,
    "port": None }

  # Extract the scheme, if present.
  (lpart, rpart) = _urlparse_splitscheme(urlstring)
  if lpart:
    components["scheme"] = lpart

  # Extract the server information, if present.
  if rpart.startswith("//"):
    (lpart, rpart) = _urlparse_splitnetloc(rpart, 2)
    components["netloc"] = lpart
    # Adds a trailing slash to the URL if no path exists. 
    if rpart == "":
      rpart = "/"

    (components["username"], components["password"], components["hostname"],
      components["port"]) = _urlparse_splitauthority(lpart)

  # Extract the fragment.
  if allow_fragments:
    (rpart, components["fragment"]) = _urlparse_splitfragment(rpart)


  # Extract the query.
  (components["path"], components["query"]) = _urlparse_splitquery(rpart)

  return components


def _urlparse_splitscheme(url):
  """Parse the scheme portion of the URL"""
  # The scheme is valid only if it contains these characters.
  scheme_chars = \
    "abcdefghijklmnopqrstuvwxyz0123456789+-."

  scheme = ""
  rest = url

  spart = url.split(":", 1)
  if len(spart) == 2:

    # Normalize the scheme.
    spart[0] = spart[0].lower()

    # A scheme is valid only if it starts with an alpha character.
    if spart[0] and spart[0][0].isalpha():
      for char in spart[0]:
        if char not in scheme_chars:
          break
      (scheme, rest) = spart

  return scheme, rest


def _urlparse_splitnetloc(url, start=0):
  """Parse the netloc portion of the URL"""

  # By default, the netloc is delimited by the end of the URL.
  delim = len(url)

  # Find the left-most delimiter.
  for char in "/?#":
    xdelim = url.find(char, start)
    if xdelim >= 0:
      delim = min(delim, xdelim)

  # Return the netloc and the rest of the URL.
  return url[start:delim], url[delim:]


def _urlparse_splitauthority(netloc):
  """Parse the authority portion of the netloc"""

  # The authority can have a userinfo portion delimited by "@".
  authority = netloc.split("@", 1)

  # Default values.
  username = None
  password = None
  hostname = None
  port = None

  # Is there a userinfo portion?
  if len(authority) == 2:

    # userinfo can be split into username:password
    userinfo = authority[0].split(":", 1)

    # hostport can be split into hostname:port
    hostport = authority[1].split(":", 1)

    if userinfo[0]:
      username = userinfo[0]
    if len(userinfo) == 2:
      password = userinfo[1]

  # No userinfo portion found.
  else:

    # hostport can be split into hostname:port
    hostport = netloc.split(":", 1)

  # Is there a port value?
  if hostport[0]:
    hostname = hostport[0]
  if len(hostport) == 2:
    port = int(hostport[1], 10)

  # Return the values.
  return username, password, hostname, port


def _urlparse_splitquery(url):
  """Parse the query portion of the url"""

  qpart = url.split("?", 1)
  if len(qpart) == 2:
    query = qpart[1]
  else:
    query = ""

  return qpart[0], query


def _urlparse_splitfragment(url):
  """Parse the query portion of the url"""

  fpart = url.split("#", 1)
  if len(fpart) == 2:
    fragment = fpart[1]
  else:
    fragment = ""

  return fpart[0], fragment

### Automatically generated by repyhelper.py ### /Users/tomashasselquist/git/tda596/demokit/urlparse.repy
