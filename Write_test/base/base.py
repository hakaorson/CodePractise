nums = list(map(int, input().split()))
cars = sorted(nums, key=lambda x: x[0], reverse=True)

" ".join(map(str,nums))