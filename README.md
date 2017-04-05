## Synopsis

This is a fork from [twaddington/python-tumblr-scraper][958689cf].  The original is a photo archiver from tumblr site by sending simple JSON requests.

I have made the following modifications:

#### Modifications:     
- modified to support tumblr API v2
- changed post type photo archive to archive photo caption as html
- modified looping through posts using limit and offset
- added param api_key to JSON request url
- add blog_name as a base directory of archives


#### Additional Functions:    
- add archive features for post type text and link
- add post_type as optional input in command-line tool

  [958689cf]: https://github.com/twaddington/python-tumblr-scraper "twaddington's python-tumblr-scraper"


## Installation

In terminal console, cd to root of repo directory, run `python setup.py install`


## Code Example

After installation, type `tumblr-scraper --help`:

    usage: tumblr-scraper [-h] [-ptype POST_TYPE] [-o OUT] [--quiet] blog_name

    Archives a Tumblr blog to a local directory

    positional arguments:
      blog_name
      api_key

    optional arguments:
      -h, --help            show this help message and exit
      -ptype POST_TYPE, --post_type POST_TYPE
                            select post type to archive
      -o OUT, --out OUT     set the out directory for the archive
      --quiet               suppress all output except errors

To archive all posts:
    `tumblr-scraper '{blog_name}' '{api_key}'`

To select archive by post type:
    `tumblr-scraper '{blog_name}' '{api_key}' -ptype='{post_type}'`

{blog_name} must NOT include '.tumblr.com'

{post_type} options are: 'photo', 'link', 'text'


## API Reference

Reference to [tumblr API v2][b25500f0].

  [b25500f0]: https://www.tumblr.com/docs/en/api/v2 "Tumblr API v2"

## TO-DOs:

- Implement bootstrap

## Contributors

Many thanks to [Tristan Waddington][df2cd640] for the initial version.  

  [df2cd640]: https://github.com/twaddington "Tristan Waddington"

## License

    Copyright 2015 cHoWy1026

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.


For README from [original repo][958689cf], read README_orig.rst.
