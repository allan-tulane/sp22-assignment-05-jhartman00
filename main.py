
####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('book', 'back'), ('kookaburra', 'kookybird-'), ('relev-ant','-elephant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if not S and not T:
        return 0
    elif not S:
        return(len(T))
    elif not T:
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            insert = 1 + MED(S, T[1:])
            delete = 1 + MED(S[1:], T)
            replace = 1 + MED(S[1:], T[1:])
            return min(insert, delete, replace)


def fast_MED(S, T, MED={}):
    if (S, T) in MED:
        return MED[(S, T)]
    elif not S and not T:
        return 0
    elif not S:
        return len(T)
    elif not T:
        return len(S)
    elif S[0] == T[0]:
        return fast_MED(S[1:], T[1:])
    else:
        insert = 1 + fast_MED(S, T[1:])
        delete = 1 + fast_MED(S[1:], T)
        replace = 1 + fast_MED(S[1:], T[1:])

        val = min(insert, delete, replace)

        MED[(S, T)] = val
        
        return val
            

def fast_align_MED(S, T, S_align, T_align MED={}):
    # TODO - keep track of alignment
    if (S, T) in MED:
        return MED[(S, T)]
    elif not S and not T:
        return 0
    elif not S:
        return len(T)
    elif not T:
        return len(S)
    elif S[0] == T[0]:
        return fast_MED(S[1:], T[1:])
    else:
        insert = 1 + fast_MED(S, T[1:])
        delete = 1 + fast_MED(S[1:], T)
        replace = 1 + fast_MED(S[1:], T[1:])

        val = min(insert, delete, replace)

        MED[(S, T)] = val
        
        return val

def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)
                                 
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])

test_MED()