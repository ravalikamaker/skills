def _clean_label(value):
    if not isinstance(value, str):
        raise TypeError("label must be text")
    label = value.strip().lower()
    if not label:
        raise ValueError("label must not be blank")
    return label


def _forward_label(value):
    return _clean_label(value)


def add_label(value, events):
    label = _forward_label(value)
    events.append(label)
    return label


def preview_label(value):
    return _clean_label(value)
