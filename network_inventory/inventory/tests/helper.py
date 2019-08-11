def in_content(response, string):
    decoded_content = response.content.decode('utf8')
    if string not in decoded_content:
        return False
    return True


def not_in_content(response, string):
    decoded_content = response.content.decode('utf8')
    if string in decoded_content:
        return False
    return True
