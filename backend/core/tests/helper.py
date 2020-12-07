from django.utils.html import escape


def in_content(response, object_to_find):
    decoded_content = response.content.decode('utf8')
    if str(escape(object_to_find)) not in decoded_content:
        return False
    return True


def not_in_content(response, object_to_find):
    decoded_content = response.content.decode('utf8')
    if str(escape(object_to_find)) in decoded_content:
        return False
    return True
