import skfeature.utility.entropy_estimators as ees
import numpy as np

def ICSRCFS(data, labels, select_nub):
    """
    fi=candidate feature  Y=[l1,l2,..lm] f_selected=S(selected subset)
    J=sum(I(fi;Y))-sum(sum(I(fi;f_selected;Y)))
    :param data:  numpy.array [n_sample,n_feature]
    :param labels: numpy.array [n_sample,n_classes]
    :param n_features: the number of selected features
    :return: S list
    """
    S = []
    mm, f_nub = np.shape(data)
    nn, l_nub = np.shape(labels)

    # pre-calculate
    rel = np.zeros((f_nub, 1))
    for i in range(f_nub):
        for j in range(l_nub):
            rel[i] = rel[i] + ees.midd(data[:, i], labels[:, j])

    # pre-calculate
    ff_L = np.zeros((f_nub, f_nub, l_nub))  
    for i in range(l_nub):
        for j in range(f_nub):
            for k in range(j, f_nub):
                ff_L[j][k][i] = ees.cmidd(data[:, j], data[:, k], labels[:, i])
                ff_L[k][j][i] = ff_L[j][k][i]
    


    # Selecting First Feature
    F = list(range(f_nub))
    idx = np.argmax(rel[:, 0])
    S.append(idx)
    F.remove(idx)
    f_idx = idx

    red = np.zeros((f_nub, 1))
    RC = np.zeros((f_nub, 1))

    while len(S) < select_nub:
        j_cmi = -np.inf
        for i in F:
            # red
            red[i] = red[i] + ees.midd(data[:, i], data[:, f_idx])
            # RC
            RC[i] = rel[i]
            for j in range(l_nub):
                for k in F:
                    if k != i:
                        RC[i] = RC[i] + ff_L[i][k][j]

            t = (1 / l_nub) * rel[i] - (1 / len(S)) * red[i] + (1 / (l_nub * len(F))) * RC[i]
            if t > j_cmi:
                j_cmi = t
                idx = i
 
        S.append(idx)
        F.remove(idx)
        f_idx = idx
    
    return np.array(S[:select_nub])
