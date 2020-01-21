import matplotlib.pyplot as plt

label = ["lisp" , "c" , "python" , "go" , "haskell"]
pop   = [59     , 80  , 90       , 60   , 55       ]
expld = [0      , 0   , 0        , 0.25 , 0        ]

plt.pie(pop, explode=expld, labels=label, autopct="%.2f")
plt.show()
