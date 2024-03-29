'''
    this is for getting the close matches

    example:
        we have list :
        possibilities = ["ape", "apple", "peach", "puppy"]

        and we have a word "appel"

        output = get_close_matches(word, possibilities, n=3, cutoff=0.6)

        output = ['apple', 'ape']

        get_close_matches(word, possibilities, n=3, cutoff=0.6)
            Use SequenceMatcher to return list of the best "good enough" matches.

            word is a sequence for which close matches are desired (typically a
            string).

            possibilities is a list of sequences against which to match word
            (typically a list of strings).

            Optional arg n (default 3) is the maximum number of close matches to
            return.  n must be > 0.

            Optional arg cutoff (default 0.6) is a float in [0, 1].  Possibilities
            that don't score at least that similar to word are ignored.

            The best (no more than n) matches among the possibilities are returned
            in a list, sorted by similarity score, most similar first.

            >>> get_close_matches("appel", ["ape", "apple", "peach", "puppy"])
            ['apple', 'ape']
            >>> import keyword as _keyword
            >>> get_close_matches("wheel", _keyword.kwlist)
            ['while']
            >>> get_close_matches("Apple", _keyword.kwlist)
            []
            >>> get_close_matches("accept", _keyword.kwlist)
            ['except']

'''
