import pytest


def test_is_start_parsed_text_line():
    from detach_request import is_start_parsed_text_line
    assert is_start_parsed_text_line('ParsedText:') == True
    assert is_start_parsed_text_line('Text') == False


def test_is_key_value_line():
    from detach_request import is_key_value_line
    assert is_key_value_line('MessageType: LOG', ['=', ':']) == True
    assert is_key_value_line('      mcc_1 = 4 (0x4)', ['=', ':']) == True
    assert is_key_value_line('ParsedText:\n', ['=', ':']) == True
    assert is_key_value_line('Text', ['=', ':']) == False


def test_get_key_value_on_separator():
    from detach_request import get_key_value_on_separator
    assert get_key_value_on_separator('MessageType: LOG', ':') == ('MessageType', 'LOG')
    assert get_key_value_on_separator('MessageSummary: Length: 0025', ':') == ('MessageSummary', 'Length: 0025')
    assert get_key_value_on_separator('      mcc_1 = 4 (0x4)', '=') == ('mcc_1', '4 (0x4)')


def test_is_line_to_ignore():
    from detach_request import is_line_to_ignore
    assert is_line_to_ignore(' *QCAT Parsing Result*') == True


def test_is_key_nested_dict_line():
    from detach_request import is_key_nested_dict_line
    assert is_key_nested_dict_line("lte_emm_msg") == True
    assert is_key_nested_dict_line("lte_emm_msg:") == False
    assert not is_key_nested_dict_line("pkt_version = 1 (0x1)")
    assert not is_key_nested_dict_line("")


def test_can_get_key_for_nested_dict():
    from detach_request import get_key_for_nested_dict
    assert get_key_for_nested_dict(line="lte_emm_msg") == "lte_emm_msg"
    assert get_key_for_nested_dict(line="    eps_mob_id") == "eps_mob_id"


def test_is_message_header_line():
    from detach_request import is_message_header_line
    assert is_message_header_line("  emm_detach_request") == False
    assert is_message_header_line("Timestamp: 07/10/2013 12:04:11.590") == False
    assert is_message_header_line("2013 Jul 10  12:04:11.590  [00]  0xB0ED  LTE NAS EMM Plain OTA Outgoing Message  --  Detach request Msg") == True
    assert is_message_header_line("--  Detach request Msg ul 10  12:04:11.590  [00]  0xB0ED  LTE NAS EMM Plain OTA Outgoing Messag") == False


def test_can_get_message_type_from_message_header_line():
    from detach_request import get_message_type
    hdr_line = "2013 Jul 10  12:04:11.590  [00]  0xB0ED  LTE NAS EMM Plain OTA Outgoing Message  --  Detach request Msg"
    assert get_message_type(header_line=hdr_line) == 'Detach request'


def test_can_get_parsed_value_from_raw_value():
    from detach_request import get_parsed_value
    assert get_parsed_value(raw_value="1 (0x1) (EPS detach)") == "EPS detach"
    assert get_parsed_value(raw_value="4 (0x4)") == "4"


def test_can_get_identation_depth():
    from detach_request import get_indentation_depth
    assert get_indentation_depth(line="      MME_group_id = 2 (0x2)") == 6
    assert get_indentation_depth(line="lte_emm_msg") == 0
    assert get_indentation_depth(line="    eps_mob_id") == 4
