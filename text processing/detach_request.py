
def get_key_value_on_separator(line, separator):
    key, val = line.split(separator, 1)
    return key.strip(), val.strip()


def is_start_parsed_text_line(line):
    return line == 'ParsedText:'


def is_key_value_line(line, separators):
    for separator in separators:
        if separator in line:
            return True
    return False


def is_line_to_ignore(line):
    return line == ' *QCAT Parsing Result*'


def is_key_nested_dict_line(line):
    striped_line = line.strip()
    words = striped_line.split()
    if len(words) > 1:
        return False
    elif words:
        key_candidate = words[0].replace('_', '')
        return key_candidate.isalnum()


def get_key_for_nested_dict(line):
    striped_line = line.strip()
    return striped_line


def is_message_header_line(line):
    return line.endswith("--  Detach request Msg")


def get_message_type(header_line=''):
    msg_type_area = header_line.split("--")[1]
    return msg_type_area.replace("Msg", "").strip()


def get_parsed_value(raw_value):
    value_string = raw_value.replace(')', '')
    value_parts = value_string.split('(')
    if len(value_parts) > 2:
        return value_parts[-1]
    else:
        return value_parts[0].replace(' ','')


def get_indentation_depth(line):
    count = 0
    for character in line:
        if character != " ":
            return count
        else:
            count += 1

    raise Exception("Empty Line")


def parse(log_content=""):
    msg = {}
    current_dict = msg
    nested_dicts = []
    for line in content.splitlines():
        if is_line_to_ignore(line=line):
            continue
        if is_start_parsed_text_line(line=line):
            substructure = {}
            current_dict['ParsedText'] = substructure
            current_dict = substructure
        elif is_message_header_line(line=line):
            msg_type = get_message_type(header_line=line)
            substructure = {}
            nested_dicts.append((-1, substructure))  # put dict on stack for all 0-indent keys like 'pkt_version = 1 (0x1)'
            current_dict[msg_type] = substructure
            current_dict = substructure
        elif is_key_nested_dict_line(line=line):
            key = get_key_for_nested_dict(line=line)
            indentation = get_indentation_depth(line=line)
            substructure = {}
            nested_dicts.append((indentation, substructure))
            current_dict[key] = substructure
            current_dict = substructure
        elif is_key_value_line(line=line, separators=[':', '=']):
            current_separator = "=" if "=" in line else ':'
            key, value = get_key_value_on_separator(line=line, separator=current_separator)
            if current_separator == ":":
                current_dict[key] = value
            else:
                while nested_dicts:
                    indentation = get_indentation_depth(line=line)
                    last_dict_indentation, last_dict = nested_dicts[-1]
                    if indentation <= last_dict_indentation:
                        nested_dicts.pop()
                        last_dict_indentation, last_dict = nested_dicts[-1]
                        current_dict = last_dict
                    else:
                        break
                current_dict[key] = get_parsed_value(raw_value=value)
    return msg


if __name__ == '__main__':
    import pprint
    with open("detach_request.log") as msg_file:
        content = msg_file.read()
        print content
        pprint.pprint(parse(log_content=content))