# Recursive function for Tower of Hanoi
def hanoi(disks, source, helper, destination):
    # Base Condition
    if (disks == 1):
        print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
        return

    # Recursive calls in which function calls itself.
    hanoi(disks - 1, source, destination, helper)
    print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
    hanoi(disks - 1, helper, source, destination)

def hanoi_anna(disks, source, helper, destination):
    if disks == 1:
        print(f"Move {disks} from {source} to {destination}")
        return
        
    
    # all_disks = [x for x in range(1, disks+1)]
    # print(all_disks)
    
    # disks_helper = []
    # disks_destination = []
    
    # disks = []
    hanoi_anna(disks-1,source, destination, helper)
    print(f'Disk {disks} moves from tower {source} to tower {destination}.')
    hanoi_anna(disks-1, helper, source, destination)

    
# Driver code: Initializing and calling the function
disks = int(input('Number of disks to be displaced: '))
'''
Tower names passed as arguments:
Source: A
Helper: B
Destination: C
'''
# Actual function call
hanoi_anna(disks, 'A', 'B', 'C')


