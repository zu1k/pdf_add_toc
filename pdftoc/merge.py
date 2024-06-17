import sys
import os.path
from fitzutils import open_pdf
from pdftocio.tocio import write_toc

def merge_toc(toc, path_in, out):
    try:
        with open_pdf(path_in) as doc:
            write_toc(doc, toc)
            if out is None:
                pfx, ext = os.path.splitext(path_in)
                out = f"{pfx}_toc{ext}"
            doc.save(out)
    except ValueError as e:
        print("error:", e, file=sys.stderr)
        sys.exit(1)
    except IOError as e:
        print("error: unable to open file", file=sys.stderr)
        print(e, file=sys.stderr)
        sys.exit(1)
    except IndexError as e:
        print("index error:", e, file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt as e:
        print("error: interrupted", file=sys.stderr)
        sys.exit(1)