def tuples_to_dict_if_unique(pairs):
    keys=[k for k,_ in pairs]
    if len(keys)!=len(set(keys)):
        raise ValueError("duplicate keys in tuples")
    return dict(zip(keys,pairs))

pairs=[('a',1),('b',2),('c',3)]
print(tuples_to_dict_if_unique(pairs))
