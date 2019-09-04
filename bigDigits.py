import sys

Zero = ["  ***  ",
        " *   * ",
        "*     *",
        "*     *",
        "*     *",
        " *   * ",
        "  ***  "
        ]

One = [" * ",
       "** ",
       " * ",
       " * ",
       " * ",
       " * ",
       "***"
       ]

Two = ["  ***  ",
       " *    *",
       "*    * ",
       "   *   ",
       "  *    ",
       " *     ",
       "*******"
       ]

Three = ["*******",
         "      *",
         "      *",
         "*******",
         "      *",
         "      *",
         "*******"
         ]

Four = ["   *   ",
        "  *  * ",
        " *   * ",
        " ******",
        "     * ",
        "     * ",
        "     * "
        ]

Five = [" ******",
        " *     ",
        " *     ",
        " ******",
        "      *",
        "      *",
        " ******"
        ]

Six = [" ******",
       " *     ",
       " *     ",
       " ******",
       " *    *",
       " *    *",
       " ******"
       ]

Seven = [" ******",
         "      *",
         "      *",
         "      *",
         "      *",
         "      *",
         "      *"
         ]

Eight = [" ******",
         " *    *",
         " *    *",
         " ******",
         " *    *",
         " *    *",
         " ******"
         ]

Nine = [" ******",
        " *    *",
        " *    *",
        " ******",
        "      *",
        "      *",
        " ******"
        ]

print(sys.argv)
Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]
try:
    digits = sys.argv[1]
    row = 0
    line = ""
    while row < len(One):

        for dig in digits:
            line += Digits[int(dig)][row]
            line += "   "

        print(line)
        line = ""
        row += 1
except ValueError as err:
    print(err)
