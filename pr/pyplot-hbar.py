import matplotlib.pyplot as plt

label = ["lisp" , "c" , "python" , "go" , "haskell"]
pop   = [59     , 80  , 90       , 60   , 55       ]

plt.barh(label, pop)
plt.show()
