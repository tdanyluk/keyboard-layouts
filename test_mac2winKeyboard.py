import sys
import unittest
import time

from mac2winKeyboard import *


def _actualize_year(s):
    year = time.localtime()[0]
    return s.replace("(c) $YEAR", "(c) {}".format(year))


def _make_dummy_klc_attributes():
    return KlcAttributes(company_name='myCompany',
                         keyboard_name='dummy',
                         keyboard_description='Dummy - Mac',
                         language_id='0409',
                         language_tag='en-US',
                         language_name='English (United States)')


def _make_dummy_args():
    args = argparse.ArgumentParser()
    args.physical_layout = 'us'
    args.language_id = '0409'
    args.language_tag = 'en-US'
    args.language_name = 'English (United States)'
    args.keyboard_description = 'Dummy - Mac'
    args.company_name = 'myCompany'
    args.shift_states = 'all'
    return args


def _make_french_klc_attributes():
    return KlcAttributes(company_name='myCompany',
                         keyboard_name='french',
                         keyboard_description='French - Mac',
                         language_id='040c',
                         language_tag='fr-FR',
                         language_name='French (France)')


def _make_french_args():
    args = argparse.ArgumentParser()
    args.physical_layout = 'international'
    args.language_id = '040c'
    args.language_tag = 'fr-FR'
    args.language_name = 'French (France)'
    args.keyboard_description = 'French - Mac'
    args.company_name = 'myCompany'
    args.shift_states = 'all'
    return args


def _make_french_common_klc_attributes():
    return KlcAttributes(company_name='myCompany',
                         keyboard_name='frenchc',
                         keyboard_description='French - common shift states only - Mac',
                         language_id='040c',
                         language_tag='fr-FR',
                         language_name='French (France)')


def _make_french_common_args():
    args = argparse.ArgumentParser()
    args.physical_layout = 'international'
    args.language_id = '040c'
    args.language_tag = 'fr-FR'
    args.language_name = 'French (France)'
    args.keyboard_description = 'French - common shift states only - Mac'
    args.company_name = 'myCompany'
    args.shift_states = 'common'
    return args


def _make_german_klc_attributes():
    return KlcAttributes(company_name='myCompany',
                         keyboard_name='german',
                         keyboard_description='German - Mac',
                         language_id='0407',
                         language_tag='de-DE',
                         language_name='German (Germany)')


def _make_german_args():
    args = argparse.ArgumentParser()
    args.physical_layout = 'international'
    args.language_id = '0407'
    args.language_tag = 'de-DE'
    args.language_name = 'German (Germany)'
    args.keyboard_description = 'German - Mac'
    args.company_name = 'myCompany'
    args.shift_states = 'all'
    return args


def _make_german_common_klc_attributes():
    return KlcAttributes(company_name='myCompany',
                         keyboard_name='germanc',
                         keyboard_description='German - common shift states only - Mac',
                         language_id='0407',
                         language_tag='de-DE',
                         language_name='German (Germany)')


def _make_german_common_args():
    args = argparse.ArgumentParser()
    args.physical_layout = 'international'
    args.language_id = '0407'
    args.language_tag = 'de-DE'
    args.language_name = 'German (Germany)'
    args.keyboard_description = 'German - common shift states only - Mac'
    args.company_name = 'myCompany'
    args.shift_states = 'common'
    return args


def _make_sgcap_klc_attributes():
    return KlcAttributes(company_name='myCompany',
                         keyboard_name='sgcap',
                         keyboard_description='SGCAP example - Mac',
                         language_id='0409',
                         language_tag='en-US',
                         language_name='English (United States)')


def _make_sgcap_args():
    args = argparse.ArgumentParser()
    args.physical_layout = 'us'
    args.language_id = '0409'
    args.language_tag = 'en-US'
    args.language_name = 'English (United States)'
    args.keyboard_description = 'SGCAP example - Mac'
    args.company_name = 'myCompany'
    args.shift_states = 'all'
    return args


def _make_us_test_klc_attributes():
    return KlcAttributes(company_name='myCompany',
                         keyboard_name='us_test',
                         keyboard_description='US - Mac',
                         language_id='0409',
                         language_tag='en-US',
                         language_name='English (United States)')

def _make_us_test_args():
    args = argparse.ArgumentParser()
    args.physical_layout = 'us'
    args.language_id = '0409'
    args.language_tag = 'en-US'
    args.language_name = 'English (United States)'
    args.keyboard_description = 'US - Mac'
    args.company_name = 'myCompany'
    args.shift_states = 'all'
    return args

class KLTest(unittest.TestCase):

    def test_char_description(self):
        self.assertEqual(
            char_description(hex(ord('1'))), 'DIGIT ONE')
        self.assertEqual(
            char_description(hex(ord('A'))), 'LATIN CAPITAL LETTER A')
        self.assertEqual(
            char_description(hex(ord('A')) + '@'), 'LATIN CAPITAL LETTER A')
        self.assertEqual(
            char_description(hex(ord('!'))), 'EXCLAMATION MARK')
        self.assertEqual(
            char_description('-1'), '<none>')
        self.assertEqual(
            char_description(''), '<none>')
        self.assertEqual(
            char_description('E000'), 'PUA E000')

    def test_make_keyboard_name(self):
        self.assertEqual(
            make_keyboard_name('test'), 'test')
        self.assertEqual(
            make_keyboard_name('test.keylayout'), 'test')
        self.assertEqual(
            make_keyboard_name('~/Desktop/test.keylayout'), 'test')
        self.assertEqual(
            make_keyboard_name('perfect layout.keylayout'), 'perfect layout')

    def test_make_klc_filename(self):
        self.assertEqual(
            make_klc_filename('test'), 'test.klc')
        self.assertEqual(
            make_klc_filename('t.e.s.t'), 'test.klc')
        self.assertEqual(
            make_klc_filename('test test'), 'testtest.klc')
        self.assertEqual(
            make_klc_filename('test test test'), 'testtest.klc')
        self.assertEqual(
            make_klc_filename('longfilename'), 'longfile.klc')
        self.assertEqual(
            make_klc_filename('longfilename1'), 'longfi_1.klc')
        self.assertEqual(
            make_klc_filename('longfilename100'), 'long_100.klc')
        self.assertEqual(
            make_klc_filename('x1000000'), '_1000000.klc')

        with self.assertRaises(SystemExit) as cm:
            make_klc_filename('100000000')
        self.assertEqual(cm.exception.code, -1)

    def test_read_file(self):
        self.assertEqual(
            read_file(os.path.join('tests', 'dummy.txt')), ['a', 'b', 'c']
        )

    def test_verify_input_file(self):
        import argparse
        parser = argparse.ArgumentParser()
        test_file = os.path.join('tests', 'dummy.keylayout')
        non_klc_file = os.path.join('tests', 'dummy.txt')
        nonexistent_file = os.path.join('tests', 'nonexistent')
        self.assertEqual(
            verify_input_file(parser, test_file), test_file
        )

        with self.assertRaises(SystemExit) as cm:
            verify_input_file(parser, nonexistent_file)
        self.assertEqual(cm.exception.code, 2)

        with self.assertRaises(SystemExit) as cm:
            verify_input_file(parser, non_klc_file)
        self.assertEqual(cm.exception.code, 2)

    def test_get_args(self):
        with self.assertRaises(SystemExit) as cm:
            get_args([])
        self.assertEqual(cm.exception.code, 2)

    def test_filter_xml(self):
        self.assertEqual(
            filter_xml(
                os.path.join('tests', 'dummy.keylayout')),
            '\n'.join(read_file(
                os.path.join('tests', 'dummy_filtered.keylayout')))
        )

    def test_make_klc_data(self):
        for attributes, physical_layout, shift_states in [
            (_make_dummy_klc_attributes(), 'us', 'all'),
            (_make_french_klc_attributes(), 'international', 'all'),
            (_make_french_common_klc_attributes(), 'international', 'common'),
            (_make_german_klc_attributes(), 'international', 'all'),
            (_make_german_common_klc_attributes(), 'international', 'common'),
            (_make_sgcap_klc_attributes(), 'us', 'all'),
            (_make_us_test_klc_attributes(), 'us', 'all'),
        ]:
            input_keylayout = os.path.join('tests', attributes.keyboard_name + '.keylayout')
            output_klc = os.path.join('tests', attributes.keyboard_name + '.klc')
            keyboard_data = process_input_keylayout(input_keylayout, physical_layout, shift_states)
            self.assertEqual(make_keyboard_name(input_keylayout), attributes.keyboard_name)
            with codecs.open(output_klc, 'r', 'utf-16') as raw_klc:
                klc_data = _actualize_year(raw_klc.read())
            self.assertEqual(
                make_klc_data(keyboard_data, attributes, shift_states),
                klc_data.splitlines())

    def test_run(self):
        import tempfile

        for keyboard_name, args in [
            ('dummy', _make_dummy_args()),
            ('french', _make_french_args()),
            ('frenchc', _make_french_common_args()),
            ('german', _make_german_args()),
            ('germanc', _make_german_common_args()),
            ('sgcap', _make_sgcap_args()),
            ('us_test', _make_us_test_args()),
        ]:
            temp_dir = tempfile.gettempdir()
            args.input = os.path.join('tests', keyboard_name + '.keylayout')
            args.output_dir = temp_dir
            run(args)
            output_klc = os.path.join(temp_dir, keyboard_name + '.klc')
            example_klc = os.path.join('tests', keyboard_name + '.klc')
            with open(example_klc, 'r', encoding='utf-16') as xklc:
                example_klc_data = _actualize_year(xklc.read())
            with open(output_klc, 'r', encoding='utf-16') as oklc:
                output_klc_data = oklc.read()
            self.assertEqual(example_klc_data, output_klc_data)


if __name__ == "__main__":
    sys.exit(unittest.main())
