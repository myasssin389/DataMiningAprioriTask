def compute_confidence(rules):
  
    out = []
    for r in rules:
        supp_rule = r.get('support_rule', None)
        supp_ant = r.get('support_antecedent', None)

        if supp_rule is None or supp_ant is None:
            # skip or set to None if missing inputs
            new_r = dict(r)
            new_r['confidence'] = None
            out.append(new_r)
            continue

        if supp_ant == 0:
            conf = 0.0
        else:
            conf = supp_rule / supp_ant

        new_r = dict(r)
        new_r['confidence'] = conf
        out.append(new_r)
    return out
