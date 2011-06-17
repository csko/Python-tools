#!/usr/env python
# -*- coding: utf-8 -*-

import poppler
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "USAGE: %s ABSOLUTE_PATH" % sys.argv[0]
        quit()

    document = poppler.document_new_from_file ("file://"+sys.argv[1], None)
    n_pages = document.get_n_pages()

    for page in range(n_pages):
        print "------ Page #%d ------" % page
        current_page = document.get_page(page)

        for i in current_page.get_annot_mapping():
            try:
                annot = i.annot
                contents = annot.get_contents()
                if contents:
                    print "Annotation: %s" % contents
            except AttributeError:
                # ooops...
                pass
