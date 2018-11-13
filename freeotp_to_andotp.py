#!/usr/bin/env python3

import base64
import json
import sys
import xml.etree.ElementTree
from pprint import pprint

def convert_freotp_to_andotp( freeotp_item ):
    andotp_item = {
                   "algorithm": freeotp_item["algo"],
                   "digits": freeotp_item["digits"],
                   "type": freeotp_item["type"],
                   "period": freeotp_item["period"],
                   }
    andotp_item["secret"] = base64.b32encode(
            bytes(x & 0xff for x in freeotp_item["secret"])
        ).decode("utf8")

    issuer = freeotp_item.get("issuerAlt") or \
        freeotp_item.get("issuerExt") or \
        freeotp_item.get("issuerInt")
    label = freeotp_item.get("label") or freeotp_item.get("labelAlt")

    if label and issuer:
        freeotp_item_label = "%s - %s" % (issuer, label)
    else:
        freeotp_item_label = label or issuer
    andotp_item["label"] = freeotp_item_label

    return andotp_item

def main():
    if sys.version_info.major < 3:
        print("This script requires Python 3.")
        sys.exit(1)

    if len(sys.argv) != 2:
        print("Usage: ./freeotp_backup_migrate.py <filename>")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        freeotp_data = json.load(f)

    pprint([ convert_freotp_to_andotp(x) for x in freeotp_data['tokens'] ])

if __name__ == "__main__":
    main()
