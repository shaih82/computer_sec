import numpy as np

msg = 'abc'

K = np.diag(np.ones(8))
np.random.shuffle(K)
b_msg = np.asarray([list(format(ord(x), 'b')) for x in msg]).astype('int32')
b_msg = np.hstack([np.zeros((3,1)),b_msg])

#encrypt
C = np.dot(b_msg,K)
#decrypt
M = np.dot(C,K.T)
recon_msg = np.packbits(M.astype('int'),axis=1).flatten()
recon_msg = ''.join(map(lambda x:format(x,'c'),recon_msg))


