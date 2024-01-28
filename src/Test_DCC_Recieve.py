"""
Test Suite for DCC Receiver UART Module
"""

import unittest
import time

from DCC_Recieve import DCCListener, MOB_STATE, MOBParserException


class TestDCCReceiver(unittest.TestCase):
    def test_parser_valid_mob(self):
        dut = DCCListener()
        test_line = "MOB: WAKE, 12345.12345, 12345.12345, 12345.12345"
        self.assertEqual(dut.parse_line(test_line), True, "Did not parse valid MOB Wake String")


    def test_parser_valid_state(self):
        dut = DCCListener()
        test_line = "MOB: WAKE, 12345.12345, 12345.12345, 12345.12345"
        dut.parse_line(test_line)
        self.assertEqual(dut.mob_wake_dict['MOB_STATE'], MOB_STATE.MOB_WAKE, "Did not parse valid MOB State")

    def test_parser_valid_alt(self):
        dut = DCCListener()
        test_line = "MOB: WAKE, 12345.12345, 12345.12345, 12345.12345"
        dut.parse_line(test_line)
        self.assertEqual(dut.mob_wake_dict["Altitude"], "12345.12345", "Did not parse valid Altitude")

    def test_parser_valid_long(self):
        dut = DCCListener()
        test_line = "MOB: WAKE, 12345.12345, 12345.12345, 12345.12345"
        dut.parse_line(test_line)
        self.assertEqual(dut.mob_wake_dict["Longitude"], "12345.12345", "Did not parse valid Longitude")
    
    def test_parser_valid_lat(self):
        dut = DCCListener()
        test_line = "MOB: WAKE, 12345.12345, 12345.12345, 12345.12345"
        dut.parse_line(test_line)
        self.assertEqual(dut.mob_wake_dict["Latitude"], "12345.12345", "Did not parse valid Latitude")

    def test_parser_invalid_mob(self):
        # initialize default spi slave class
        dut = DCCListener()
        test_line = "NOTMOB: WAKE, 12345.12345, 12345.12345, 12345.12345"
        self.assertEqual(dut.parse_line(test_line), False, "Parse invalid MOB Wake String")

    def test_parser_invalid_state(self):
        # initialize default spi slave class
        dut = DCCListener()
        test_line = "MOB: INVALID, 12345.12345, 12345.12345, 12345.12345"
        dut.parse_line(test_line)
        self.assertRaises( MOBParserException, dut.parse_line, test_line)



if __name__ == '__main__':
    unittest.main()