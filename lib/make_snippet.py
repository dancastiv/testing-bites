def make_snippet(entry):
    if len(entry.split()) <= 5:
        return entry
    else:
        snippet = entry.split()[0:5]
        return ' '.join(snippet) + '...'