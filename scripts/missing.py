#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Find missing images.
"""
import os
import gpo_member_photos


def files_exist(bioguide):
    jpg_filename = os.path.join("congress", "original", bioguide + ".jpg")
    jpg_found = os.path.exists(jpg_filename)

    yaml_filename = os.path.join("congress", "metadata", bioguide + ".yaml")
    yaml_found = os.path.exists(yaml_filename)

    if not jpg_found or not yaml_found:
        print "---"
        print l['name']
        if not jpg_found:
            print "Not found:", jpg_filename
        if not yaml_found:
            print "Not found:", yaml_filename


if __name__ == "__main__":
    # clone or update legislator YAML
    gpo_member_photos.download_legislator_data()

    legislators = gpo_member_photos.load_yaml(
        "congress-legislators/legislators-current.yaml")
    for l in legislators:
        bioguide = l['id']['bioguide']
        files_exist(bioguide)

# End of file
