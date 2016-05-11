#!/usr/bin/env python

import zipfile
import cPickle
import numpy as np

"""
    track_obj: {
        frames: 1 by n numpy array,
        anchors: 1 by n numpy array,
        features: m by n numpy array,
        scores: c by n numpy array,
        boxes: 4 by n numpy array,
        rois: 4 by n numpy array
    }
"""
def save_track_proto_to_zip(track_proto, save_file):
    zf = zipfile.ZipFile(save_file, 'w')
    print "Writing to zip file {}...".format(save_file)
    for track_id, track in enumerate(track_proto['tracks']):
        track_obj = {}
        track_obj['frames'] = np.asarray([box['frame'] for box in track])
        track_obj['anchors'] = np.asarray([box['anchor'] for box in track])
        track_obj['scores'] = np.asarray([box['scores'] for box in track])
        track_obj['features'] = np.asarray([box['feature'] for box in track])
        track_obj['boxes'] = np.asarray([box['bbox'] for box in track])
        track_obj['rois'] = np.asarray([box['roi'] for box in track])
        zf.writestr('{:06d}.pkl'.format(track_id),
            cPickle.dumps(track_obj, cPickle.HIGHEST_PROTOCOL))
        if (track_id + 1) % 1000 == 0:
            print "\t{} tracks written.".format(track_id + 1)
    print "\tTotally {} tracks written.".format(track_id + 1)
    zf.close()