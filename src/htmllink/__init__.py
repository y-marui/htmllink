from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from docopt import docopt
__doc__ = """{f}
Usage:
  {f} [-f | --force] <title> <url>
  {f} [-f | --force]
  {f} -h | --help

Options:
  -h, --help   Show this screen.
  -f, --force  Force to create link.
  <title>      Title of link.
  <url>        URL of link.
""".format(
    f=__file__
)
args = docopt(__doc__)


def generate():
    title = args["<title>"]
    if title is None:
        title = input("title: ")
    url = args["<url>"]
    if url is None:
        url = input("url: ")

    env = Environment(loader=FileSystemLoader(Path(__file__).parent))
    template = env.get_template('template.html')
    rendered = template.render(url=url,
                               title=title)

    mode = "w" if args["--force"] else "x"
    with open(f"{title}.html", mode) as fp:
        fp.write(rendered)
