'''
Disk Stacking from AlgoExpert.io
March 2021 Jakub Kazimierski
'''

def diskStacking(disks):
    '''
    You're given a non-empty array of arrays 
    where each subarray holds three integers 
    and represents a disk. These integers 
    denote each disk's width, depth, and height, 
    respectively. Your goal is to stack up the disks 
    and to maximize the total height of the stack. 
    A disk must have a strictly smaller width, depth, 
    and height than any other disk below it.
        
    Write a function that returns an array of the disks 
    in the final stack, starting with the top disk and 
    ending with the bottom disk. Note that you can't 
    rotate disks; in other words, the integers in each 
    subarray must represent [width, depth, height] at all
    times.

    You can assume that there will only be one stack with 
    the greatest total height.
    '''

    # Time O(n^2) | Space O(n)

    output = []
    heights = []
    sequences = []

    # sort disks by height
    disks.sort(key = lambda x: x[2]) 

    for disk in disks:
        heights.append(disk[2])


    for idx in range(len(disks)):
        curr_disk = disks[idx]
        sequences.append([idx])
        for idx_2 in range(0, idx):       
            prev_disk = disks[idx_2]

            if prev_disk[0] < curr_disk[0] and prev_disk[1] < curr_disk[1]\
                and prev_disk[2] < curr_disk[2]:

                old_height = heights[idx]
                # dynamic programming approach
                heights[idx] = max(heights[idx], heights[idx_2]+curr_disk[2])

                # update indexes in sequence
                if old_height < heights[idx]:
                    sequences[idx] = sequences[idx_2] + [idx]
                    

    max_seq_id = heights.index(max(heights))

    disk_indexes = sequences[max_seq_id]

    for idx in disk_indexes:
        output.append(disks[idx])

    return output    
