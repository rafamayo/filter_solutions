#!/usr/bin/env python

import panflute as pf

def my_filter(elem, doc):
    if doc.get_metadata('render-solutions') == True:
        if isinstance(elem, pf.Div) and 'solution' in elem.classes:
            return elem
    elif doc.get_metadata('render-solutions') == False:
        if isinstance(elem, pf.Div) and 'solution' in elem.classes:
            return []
    return None


if __name__ == '__main__':
    # Call the main function
    pf.toJSONFilter(my_filter)
