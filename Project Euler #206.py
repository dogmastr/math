"""

    Author: @dogmastr

    Problem 206
    Find the unique positive integer whos square has the form 1_2_3_4_5_6_7_8_9_0, where each "_" is a single digit.

"""

# We only have to check from sqrt(1020304050607080900) ~= 1010101010 to sqrt(1929394959697989900) ~= 1389026623.
# We choose the closest number ending with 30 and 70 for start and end respectively because of result (3).
start, end = 1010101030, 1389026570
while start <= end:

    # (1) Since n*n ends with 0, n must end with 0, so we loop n in steps of 100, starting from 1010101000 to 1389026620.

    # (2) Since n ends with 0, n*n must end with 00, so our last missing digit is 0.

    # (3) Since our number ends with 900, the second digit of n must be 3 or 7 because only 30 * 30 = 900 and 70 * 70 = 4900.
    #     Therefore, in these intervals of 100, we only need to check n ending with 30 or 70. 

    # For each "100-block", we check both numbers ending with 30 and 70.
    if str((start ** 2))[::2] == "1234567890":
        print(start + 30)
        break
    if str(((start + 40) ** 2))[::2] == "1234567890":
        print(start + 40)
        break

    # Now we jump to the next "100-block". This reduces our search space by 90%.
    start += 100