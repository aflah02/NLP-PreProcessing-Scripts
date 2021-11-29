def get_numeric_spans(tofind_spans, full_sent):
    dict_spans = {}
    dict_spans['start'] = []
    dict_spans['end'] = []
    ls_joined = []
    for i in tofind_spans:
        ls_joined.append(' '.join(i))
    ls_joined
    joinedfull = ' '.join(full_sent)
    ls_joined_no_repeats = []
    for i in ls_joined:
        if (i not in ls_joined_no_repeats):
            ls_joined_no_repeats.append(i)
    for i in ls_joined_no_repeats:
        for match in re.finditer(i, joinedfull):
                start = match.start()
                end = match.end()
                words_before = joinedfull[:start].count(' ')
                words_inmidst = i.count(' ') + 1
                dict_spans['start'].append(words_before)
                dict_spans['end'].append(words_before+words_inmidst)
    return dict_spans

df['numSpans'] = df.apply(lambda x: get_numeric_spans(x.Span, x.Hate_Speech), axis=1)