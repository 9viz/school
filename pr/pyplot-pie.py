import matplotlib.pyplot as plt

streams = ["cs" , "history" , "chem" , "maths"]
num     = [50   , 40        , 20     , 75     ]
expld   = [0    , 0         , 0.25   , 0      ]

plt.pie(num, labels=streams, explode=expld, autopct="%.2f%%")
plt.show()
