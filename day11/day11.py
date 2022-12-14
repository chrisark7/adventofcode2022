monkeys = {
    0: {'items': [75, 75, 98, 97, 79, 97, 64],
        'operation': lambda old:  old * 13,
        'test': lambda x: (x % 19) == 0,
        'true': 2,
        'false': 7
        },
    1: {'items': [50, 99, 80, 84, 65, 95],
        'operation': lambda old: old + 2,
        'test': lambda x: x % 3 == 0,
        'true': 4,
        'false': 5
        },
    2: {'items': [96, 74, 68, 96, 56, 71, 75, 53],
        'operation': lambda old: old + 1,
        'test': lambda x: x % 11 == 0,
        'true': 7,
        'false': 3
        },
    3: {'items': [83, 96, 86, 58, 92],
        'operation': lambda old: old + 8,
        'test': lambda x: x % 17 == 0,
        'true': 6,
        'false': 1
        },
    4: {'items': [99],
        'operation': lambda old: old * old,
        'test': lambda x: x % 5 == 0,
        'true': 0,
        'false': 5
        },
    5: {'items': [60, 54, 83],
        'operation': lambda old: old + 4,
        'test': lambda x: x % 2 == 0,
        'true': 2,
        'false': 0
        },
    6: {'items': [77, 67],
        'operation': lambda old: old * 17,
        'test': lambda x: x % 13 == 0,
        'true': 4,
        'false': 1
        },
    7: {'items': [95, 65, 58, 76],
        'operation': lambda old: old + 5,
        'test': lambda x: x % 7 == 0,
        'true': 3,
        'false': 6
        }
}
monkeys_supermod = 19 * 3 * 11 * 17 * 5 * 2 * 13 * 7

monkeys_test = {
    0: {'items': [79, 98],
        'operation': lambda old: old * 19,
        'test': lambda x: (x % 23) == 0,
        'true': 2,
        'false': 3
        },
    1: {'items': [54, 65, 75, 74],
        'operation': lambda old: old + 6,
        'test': lambda x: x % 19 == 0,
        'true': 2,
        'false': 0
        },
    2: {'items': [79, 60, 97],
        'operation': lambda old: old * old,
        'test': lambda x: x % 13 == 0,
        'true': 1,
        'false': 3
        },
    3: {'items': [74],
        'operation': lambda old: old + 3,
        'test': lambda x: x % 17 == 0,
        'true': 0,
        'false': 1
        }
}
monkeys_test_supermod = 23 * 19 * 13 * 17

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
def compute_prime_factorization(n):
    # Start an output dictionary
    out = {prime_n: 0 for prime_n in primes}
    # Run through the list of primes and see which primes fit
    for prime_n in primes:
        while n % prime_n == 0:
            out[prime_n] += 1
            n = n/prime_n
    return out


# Choose which monkey properties we're looking at
monkeys_n = monkeys
supermod_n = monkeys_supermod
part_n = "Part 2"

# Add an 'inspections' field to each monkey initialized to zero
for i in range(len(monkeys_n)):
    monkeys_n[i]['inspections'] = 0

# Multiple rounds
rounds = 10000
for k in range(rounds):
    # Single Round
    for i in range(len(monkeys_n)):
        # Iterate over all items in the list
        for j in range(len(monkeys_n[i]['items'])):
            # Pop the first item from the front of the monkey's item list
            item_n = monkeys_n[i]['items'].pop(0)
            # Perform the monkey's operation on the item value
            item_n = monkeys_n[i]['operation'](item_n)
            if part_n == "Part 1":
                # Divide the items value by three
                item_n = item_n//3
            elif part_n == "Part 2":
                item_n = item_n % supermod_n
            # Test the item per the monkey's test
            test_n = monkeys_n[i]['test'](item_n)
            # Decide which monkey the item goes to
            goto_n = monkeys_n[i]['true'] if test_n else monkeys_n[i]['false']
            # Add the item to the appropriate monkey's item list
            monkeys_n[goto_n]['items'].append(item_n)
            # Update this monkey's inspection number
            monkeys_n[i]['inspections'] += 1
    # Debug check
    '''
    print(f"\nRound {k+1}")
    for i in range(len(monkeys_n)):
        print(f"Monkey {i}: {monkeys_n[i]['items']}")
    '''

# Print the number of inspections
print("\nInspections:")
for i in range(len(monkeys_n)):
    print(f"  Monkey {i}: {monkeys_n[i]['inspections']}")

# Calculate the multiple of the two highest
inspections = [x['inspections'] for x in monkeys_n.values()]
inspections.sort(reverse=True)
print(f"Inspection Multiple: {inspections[0] * inspections[1]}")
