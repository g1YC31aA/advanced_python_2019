import pytest
import sys, os
# This block is not neccessary if you instaled your package
# using e.g. pip install -e
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), # location of this file
            os.pardir, # and one level up, in linux ../
        )
    )
)
# EOBlock

import playground

def test_find_peaks():
    peaks = playground.color_sorting.find_peaks([(4,4,4),(1,1,1),(0,9,3)])
    assert peaks == [(1,1,1)]

def test_find_two_peaks():
    peaks = playground.color_sorting.find_peaks([(4,4,4),(1,1,1),(0,9,3), (2,2,2), (255,200,100)])
    assert peaks == [(1,1,1), (2,2,2)]

def test_find_peaks_max_edge():
    peaks = playground.color_sorting.find_peaks([(4,4,4),(255,255,255),(0,9,3)])
    assert peaks == [] 

def test_find_peaks_empty_list():
    peaks = playground.color_sorting.find_peaks([])
    assert peaks == []
