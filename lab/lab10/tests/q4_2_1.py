OK_FORMAT = True

test = {   'name': 'q4_2_1',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> import hashlib\n'
                                               '>>> def get_hash(num):\n'
                                               '...     """Helper function for assessing correctness."""\n'
                                               '...     return hashlib.md5(str(num).encode()).hexdigest()\n'
                                               ">>> get_hash(np.round(prob_cancer_given_positive_new, 4)) == '4f59b3fd6f5001542919c239391a3278'\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
