# *_*coding:utf-8 *_*


def clip(text, max_len=80) -> str:
    """在max_len前面或后面的第一个空格处截断文本"""
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_before = text.rfind(' ', max_len)
            if space_before >= 0:
                end = space_before
    if end is None:
        end = len(text)

    return text[:end].rstrip()


def clipDemo():
    print(clip.__defaults__)
    print(clip.__code__)
    print(clip.__code__.co_varnames)
    print(clip.__code__.co_filename)
    print(clip.__code__.co_argcount)


def getFuncSign():
    from inspect import signature
    sig = signature(clip)
    print(sig)
    print(str(sig))
    for name, param in sig.parameters.items():
        print(param.kind, ':', name, '=', param.default)
        print(param.VAR_KEYWORD)

    print(sig.return_annotation)
    for param in sig.parameters.values():
        note = repr(param.annotation).ljust(13)
        print(note, ":", param.name, '=', param.default)


if __name__ == '__main__':
    # clipDemo()
    getFuncSign()
