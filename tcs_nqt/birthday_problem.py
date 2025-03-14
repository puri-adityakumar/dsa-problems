'''
    It's Tina's birthday today, and everyone is bringing different gifts for her. 
    You forgot to bring a gift for her. So, she became a bit sad.

    To cheer her up, you have promised to give her Teddys for the next N days. 
    But how many Teddys, that Tina will decide. 
    She gave a list 'B' where she has mentioned the number of Teddys for each day from 1 to N, which she wants.
    The problem is that there is a limited supply of Teddys in the city. 
    So, she decided to compensate for it with chocolates. 
    But she has also set a rule for each day for chocolates also. 
    For every missing Teddy on day, you have to compensate it with C[i] number of chocolates per Teddy.

    Let's say on day 2, you have to give 4 Teddys to Tina, but you gave only 2, 
    then the remaining 2 Teddys have to be compensated by chocolates from C[2]. 
    And for each day, it may be different.

    Given the maximum number of available Teddys M, and the number of days N.
    You have to give the Teddys in such a way that you minimize the chocolates on any given day that you have to give to Tina.
    You have to find the maximum number of chocolates you have given to Tina over the period of N days, in the best possible scenario.

    The number of Teddys on ith day which is asked for by Tina is mentioned in sequence B[ ]. 
    If on "i" day you failed to give one or more of these Teddys, then for each Teddy not given, it has to be compensated by C[i] chocolates per Teddy.

    Now you have to plan in such a way that the maximum chocolate that was given on any given day is minimum in any scenario.

    So, the goal is to minimize the number of chocolates that you need to give to Tina for any missing teddy on any given day.
    Let’s say the sequence Z contains the number of chocolates given on all N days.
    Once you have the list of all the chocolates given for all the N-days, 
    find the Maximum value MAXIMUM value of chocolate from this final sequence Z that was given on any particular day.

    Example:
    Let us try to understand it with an example.
    Let’s say Number of days N = 5 and maximum Teddys available in the city is M = 3.
    Below is the rule Tina has made for Teddys and chocolates.

    B = [1 2 3 4 5]
    C = [1 2 3 4 5]

    It means on:
    Day 1, if you are missing 1 teddy, you have to give 1 chocolate (C[0]).
    Day 2, if you are missing 1 teddy, you have to give 2 chocolates (C[1]) per 1 missing teddy.
    …and so on.

    So, if on Day-2 you fail to give 2 Teddys, then you have to give 2*2 = 4 chocolates.
    In the above array C[ ], we can see that for the 5th day, the number of chocolates for each missing teddy is maximum, which is 5 (C[5]).
    This is what we have to minimize.

    To minimize the chocolates, we avoid the maximum values which are available in B[ ]. 
    And these are B[4] & B[5].

    Hence, with 3 Teddys, we can give as [0 0 0 1 2] on each day, 
    and on top of the Teddys we have to pay chocolates which are required on day 5 is 15.

    There could be another scenario, where we give teddy as [0 0 0 3], 
    then the number of chocolates that need to be given for the missing teddys will be as Z = [1 4 9 16 10].
    The maximum value in this sequence Z is 16.

    So, this is not the best possible answer compared to the previous example where the maximum chocolate was 15.
    So, we choose the minimum value out of it, which is 15.
    So, the answer is 15.

'''