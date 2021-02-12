import matplotlib.pyplot as plt

# ------------------------------------------------ EASTER EGG ------------------------------------------------
# Uh oh! It seems like a little fox has jumped into Jonathan's life and scrambled up his priorities.
# 
# A variation of the Caesar Cipher is necessary to help decrypt the mess. Each letter in the original document
# has been shifted backwards by a multitude (from one to twenty-fix) of its index. For example, the encrypted
# string "abcd" decrypts into "adgj" assuming a multitude of two. String indices start from zero. The multiple
# is constant for every character in the string. Please help Jonathan figure out what he should be spending his
# time on!
# 
# Encrypted String: awfblxnwy

# blackbox.py
plt.gca().axes.xaxis.set_visible(False)
plt.gca().axes.yaxis.set_visible(False)
fig = plt.gcf()
fig.set_size_inches((11,7))

# G
g_x = [6, 2, 2, 6, 6, 4, 4]
g_y = [11, 11, 7, 7, 9, 9, 8]

plt.plot(g_x, g_y)

# I
i_x = [7, 11, 9, 9, 7, 11]
i_y = [11, 11, 11, 7, 7, 7]
plt.plot(i_x, i_y)

# V
v_x = [12, 14, 16]
v_y = [11, 7, 11]
plt.plot(v_x, v_y)

# E
e_x = [21, 17, 17, 21, 17, 17, 21]
e_y = [11, 11, 9, 9, 9, 7, 7]
plt.plot(e_x, e_y)

# A
a1_x = [2, 4, 6, 5, 3]
a1_y = [2, 6, 2, 4, 4]

plt.plot(a1_x, a1_y)

# P
p1_x = [7, 7, 11, 11, 7]
p1_y = [2, 6, 6, 4, 4]
plt.plot(p1_x, p1_y)

# P
p2_x = [12, 12, 16, 16, 12]
p2_y = [2, 6, 6, 4, 4]
plt.plot(p2_x, p2_y)

# A
a2_x = [17, 19, 21, 20, 18]
a2_y = [2, 6, 2, 4, 4]

plt.plot(a2_x, a2_y)

# Plot
plt.show()