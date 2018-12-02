from sys import argv
from stack_array import *

def tsort(vertices):
    '''
    * Performs a topological sort of the specified directed acyclic graph.  The
    * graph is given as a list of vertices where each pair of vertices represents
    * an edge in the graph.  The resulting string return value will be formatted
    * identically to the Unix utility {@code tsort}.  That is, one vertex per
    * line in topologically sorted order.
    *
    * Raises a ValueError if:
    *   - vertices is emtpy with the message "input contains no edges"
    *   - vertices has an odd number of vertices (incomplete pair) with the
    *     message "input contains an odd number of tokens"
    *   - the graph contains a cycle (isn't acyclic) with the message 
    *     "input contains a cycle"'''
    list_len = len(vertices)
    returnstring = ''
    if list_len == 0:
        raise ValueError('input contains no edges')
    elif list_len % 2 == 1: 
        raise ValueError('input contains an odd number of tokens')
    stack = Stack(list_len)
    adj_list = build_adj_list(vertices)
    num_verts = len(adj_list)
    output = 0

    for key in adj_list:
        if adj_list[key][0] == 0:
            stack.push(key)
    while not stack.is_empty():
        val = stack.pop()
        if returnstring == '':
            returnstring = returnstring + val
            output +=1
        else:
            returnstring = returnstring + "\n" + val 
            output += 1
        for item in adj_list[val][1]:
            adj_list[item][0] -= 1
            if adj_list[item][0] == 0:
                stack.push(item)
    if output != num_verts:
        raise ValueError('input contains a cycle')
    return returnstring
    
def build_adj_list(vertices):
    adj_list = {}
    i = 0
    while i in range(len(vertices)-1):
        vert1 = vertices[i]
        vert2 = vertices[i+1]
        if vert1 not in adj_list:
            adj_list.update({vert1 : [0, [vert2]]})
        else:
            adj_list[vert1][1].append(vert2)

        if vert2 not in adj_list:
            adj_list.update({vert2 : [1, []]})
        else:
            adj_list[vert2][0] +=1
        i +=2
    return adj_list

def main():
    '''Entry point for the tsort utility allowing the user to specify
       a file containing the edge of the DAG'''
    if len(argv) != 2:
        print("Usage: python3 tsort.py <filename>")
        exit()
    try:
        f = open(argv[1], 'r')
    except FileNotFoundError as e:
        print(argv[1], 'could not be found or opened')
        exit()
    
    vertices = []
    for line in f:
        vertices += line.split()
       
    try:
        result = tsort(vertices)
        print(result)
    except Exception as e:
        print(e)

    
if __name__ == '__main__': 
    main()
