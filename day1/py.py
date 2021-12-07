previous = None
depth_increases = 0

window_size = 3

with open('input.txt') as f:
    depth_list = [int(i) for i in f]

for i in range(len(depth_list)):
    if len(depth_list[i:i+window_size]) == window_size:
        current = sum(depth_list[i:i+window_size])

        if previous and previous < current:
            depth_increases += 1
        
        previous = current

print(depth_increases)
