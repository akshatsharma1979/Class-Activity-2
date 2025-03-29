def find_cube_pairs(target)    # Missing colon (:) at the end.
    solutions = []
    max_num = round(targ ** (1/3))  # change targ to target, *** to **

    for a in range(1, max_num + 1)       # Should be range, not ranges.
        for b in range(a, max_num + 1)   # Should be range, not ranges.
            if a***3 + b***3 == target      # Should be a**3 + b**3 == target.
                solutions.append((a, b))     # The list is named solutions, not sol.
    return solutions
   
pairs = find_cube_pairs(1728)          # The comma makes it a tuple, we don't want that, number Should be 1278, instead of 1279
printf("Valid cube pairs for 1728:")  # printf is not a valid Python function. Use print().
for a, b in pairs:    # The variable is named pairs, not pair.
    printf(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1728")     # printf should be print(), {a**2} + {b**2} should be {a**3} + {b**3} (cubes, not squares).
## remove all semicolons
