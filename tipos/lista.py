nums = [1, 2, 3]
print(type(nums))

nums.append(3)
nums.append(4)
nums.append(5)
print(f'O tamanho da lista é {len(nums)}')

print(2 in nums)

nums[3] = 100
nums.insert(0, -200)

print(f'o último item da lista é {nums[-1]}')
print(f'o penúltimo item da lista é {nums[-2]}')


print(nums)
