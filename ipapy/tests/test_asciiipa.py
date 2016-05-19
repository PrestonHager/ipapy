#!/usr/bin/env python
# coding=utf-8

import unittest

from ipapy.asciiipa import unicode_string_to_ascii_string
from ipapy.asciiipa import ipa_string_to_ascii_string
from ipapy.ipastring import IPAString

class TestASCIIIPA(unittest.TestCase):

    def test_unicode_string_to_ascii_string(self):
        values = [
            (None, None),
            (u"", u""),
            (u"foo", u"foo"),
            (u"\u0070\u032A", u"p["),
            (u"\u025F", u"J"),
            (u"\u0294", u"?"),
            (u"foo\u025F\u0294", u"fooJ?"),
            (u"fo\u02C8o\u025F\u0294", u"fo'oJ?"),
            (u"foo bar", u"foo#bar<trl>"),
            (u"\u0261\u0067", u"gg"),
            (u"ma\u0272ana", u"man^ana"),
            (u"\u02A3", u"dz"),
            (u"\u02A7", u"tS"),
        ]
        for v, e in values:
            self.assertEqual(unicode_string_to_ascii_string(v), e)

    def test_ipa_string_to_ascii_string(self):
        values = [
            (u"", u""),
            (u"foo", u"foo"),
            (u"\u0070\u032A", u"p["),
            (u"\u025F", u"J"),
            (u"\u0294", u"?"),
            (u"foo\u025F\u0294", u"fooJ?"),
            (u"fo\u02C8o\u025F\u0294", u"fo'oJ?"),
            (u"foo bar", u"foo#bar<trl>"),
            (u"\u0261\u0067", u"gg"),
            (u"ma\u0272ana", u"man^ana"),
            (u"\u02A3", u"dz"),
            (u"\u02A7", u"tS"),
        ]
        for v, e in values:
            self.assertEqual(ipa_string_to_ascii_string(IPAString(unicode_string=v)), e)

    def test_unicode_string_to_ascii_string_ignore(self):
        values = [
            (None, None),
            (u"", u""),
            (u"foo", u"foo"),
            (u"\u0070\u032A", u"p["),
            (u"\u025F", u"J"),
            (u"\u0294", u"?"),
            (u"foo\u025F\u0294", u"fooJ?"),
            (u"fo\u02C8o\u025F\u0294", u"fo'oJ?"),
            (u"foo bar", u"foo#bar<trl>"),
            (u"\u0261\u0067", u"gg"),
            (u"ma\u0272ana", u"man^ana"),
            (u"\u02A3", u"dz"),
            (u"\u02A7", u"tS"),
            (u"L", u""),
            (u"foo", u"foo"),
            (u"\u0070\u032AL", u"p["),
            (u"L\u025FM", u"J"),
            (u"L\u0294M", u"?"),
            (u"fLoo\u025F\u0294M", u"fooJ?"),
            (u"fo\u02C8oL\u025F\u0294M", u"fo'oJ?"),
            (u"fooL MbarN", u"foo#bar<trl>"),
            (u"\u0261L\u0067", u"gg"),
            (u"mLa\u0272Mana", u"man^ana"),
            (u"L\u02A3", u"dz"),
            (u"\u02A7M", u"tS"),
        ]
        for v, e in values:
            self.assertEqual(unicode_string_to_ascii_string(v, ignore=True), e)

    def test_ipa_string_to_ascii_string_ignore(self):
        values = [
            (u"", u""),
            (u"foo", u"foo"),
            (u"\u0070\u032A", u"p["),
            (u"\u025F", u"J"),
            (u"\u0294", u"?"),
            (u"foo\u025F\u0294", u"fooJ?"),
            (u"fo\u02C8o\u025F\u0294", u"fo'oJ?"),
            (u"foo bar", u"foo#bar<trl>"),
            (u"\u0261\u0067", u"gg"),
            (u"ma\u0272ana", u"man^ana"),
            (u"\u02A3", u"dz"),
            (u"\u02A7", u"tS"),
            (u"L", u""),
            (u"foo", u"foo"),
            (u"\u0070\u032AL", u"p["),
            (u"L\u025FM", u"J"),
            (u"L\u0294M", u"?"),
            (u"fLoo\u025F\u0294M", u"fooJ?"),
            (u"fo\u02C8oL\u025F\u0294M", u"fo'oJ?"),
            (u"fooL MbarN", u"foo#bar<trl>"),
            (u"\u0261L\u0067", u"gg"),
            (u"mLa\u0272Mana", u"man^ana"),
            (u"L\u02A3", u"dz"),
            (u"\u02A7M", u"tS"),
        ]
        for v, e in values:
            self.assertEqual(ipa_string_to_ascii_string(IPAString(unicode_string=v, ignore=True)), e)

    def test_unicode_string_to_ascii_string_single(self):
        values = [
            (None, None),
            (u"", u""),
            (u"foo", u"foo"),
            (u"\u0070\u032A", u"p["),
            (u"\u025F", u"J"),
            (u"\u0294", u"?"),
            (u"foo\u025F\u0294", u"fooJ?"),
            (u"fo\u02C8o\u025F\u0294", u"fo'oJ?"),
            (u"foo bar", u"foo#bar<trl>"),
            (u"\u0261\u0067", u"gg"),
            (u"ma\u0272ana", u"man^ana"),
            (u"\u02A3", u"dz"),
            (u"\u02A7", u"tS"),
        ]
        for v, e in values:
            self.assertEqual(unicode_string_to_ascii_string(v, single_char_parsing=True), e)



