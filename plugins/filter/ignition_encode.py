import base64


def ignition_encode(val, content_type='text/plain', charset='utf-8'):
    content = base64.b64encode(val.encode(charset)).decode()
    return f'data:{content_type};charset={charset};base64,{content}'


class FilterModule(object):
    def filters(self):
        return {
            'ignition_encode': ignition_encode,
        }
