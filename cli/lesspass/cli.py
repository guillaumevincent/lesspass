import argparse
import os


class readable_dir(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        prospective_dir = values
        if not os.path.isdir(prospective_dir):
            raise argparse.ArgumentTypeError(
                f"readable_dir: `{prospective_dir}` is not a valid path"
            )
        if os.access(prospective_dir, os.R_OK):
            setattr(namespace, self.dest, prospective_dir)
        else:
            raise argparse.ArgumentTypeError(
                f"readable_dir: `{prospective_dir}` is not a readable dir"
            )


def parse_args(args):
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("site", nargs="?")
    parser.add_argument("login", nargs="?")
    parser.add_argument(
        "master_password",
        default=os.environ.get("LESSPASS_MASTER_PASSWORD", None),
        nargs="?",
    )
    parser.add_argument("-l", "--lowercase", dest="l", action="store_true")
    parser.add_argument("-u", "--uppercase", dest="u", action="store_true")
    parser.add_argument("-d", "--digits", dest="d", action="store_true")
    parser.add_argument("-s", "--symbols", dest="s", action="store_true")
    parser.add_argument("--no-lowercase", dest="nl", action="store_true")
    parser.add_argument("--no-uppercase", dest="nu", action="store_true")
    parser.add_argument("--no-digits", dest="nd", action="store_true")
    parser.add_argument("--no-symbols", dest="ns", action="store_true")
    parser.add_argument("-L", "--length", default=16, type=int)
    parser.add_argument("-C", "--counter", default=1, type=int)
    parser.add_argument("-p", "--prompt", dest="prompt", action="store_true")
    parser.add_argument(
        "--to-profiles", dest="to_profiles", action=readable_dir
    )
    parser.add_argument(
        "-c", "--copy", "--clipboard", dest="clipboard", action="store_true"
    )
    parser.add_argument("-h", "--help", action="store_true")
    parser.add_argument("-v", "--version", action="store_true")
    return parser.parse_args(args)
