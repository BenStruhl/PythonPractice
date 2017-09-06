ninedy_nine_problems = ["car","money","women","rent"]

## append - put a element at the end of the list
ninedy_nine_problems.append("credit cards")

print(ninedy_nine_problems)

## extend - extend a list by an iterable
ninedy_nine_problems.extend(range(1,10))

print(ninedy_nine_problems)

## insert - insert element to index in list
ninedy_nine_problems.insert(1,"Kanye")

print(ninedy_nine_problems)

## remove - get rid of first element in list whose value is x REALLY SLOW
## performance wise
ninedy_nine_problems.remove("Kanye")

print(ninedy_nine_problems)

## count- count how many times something has appeared in a list
print(ninedy_nine_problems.count("car"))

stacks_on_stacks = [1,2,3]

stacks_on_stacks.append(4)
print(stacks_on_stacks)
stacks_on_stacks.pop()
stacks_on_stacks.pop()
print(stacks_on_stacks)
