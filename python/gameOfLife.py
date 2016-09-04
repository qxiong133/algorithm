


#Any live cell with fewer than two live neighbors dies, as if caused by under-population.
#Any live cell with two or three live neighbors lives on to the next generation.
#Any live cell with more than three live neighbors dies, as if by over-population..
#Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction


class Solution(object):

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        direction = ((-1, -1),(-1, 0),(-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),(1, 1),)
        max_m = len(board)
        max_n = len(board[0]) if max_m else 0
        for m, l in enumerate(board):
            for n, v in enumerate(l):
                tmp_sum = 0
                for t in direction:
                    tmp_m = m + t[0]
                    tmp_n = n + t[1]
                    # die to die 0
                    # live to live 1
                    # live to die 2
                    # die to live 3
                    if tmp_m < 0 or tmp_m >= max_m or tmp_n <0 or tmp_n >= max_n:
                        continue
                    if m ==1 and n ==1:
                        print "======",tmp_m,tmp_n,board[tmp_m][tmp_n]
                    if board[tmp_m][tmp_n] == 1 or board[tmp_m][tmp_n] == 2:
                        tmp_sum += 1
                # <2 die
                # =2 =3 live
                # >3 die
                # =3 live
                if board[m][n] == 0:
                    if tmp_sum == 3:
                        board[m][n] = 3
                else:
                    if tmp_sum < 2 or tmp_sum > 3:
                        board[m][n] = 2
                print m,n,tmp_sum,board[m][n]
        for m, l in enumerate(board):
            for n, v in enumerate(l):
                board[m][n] = board[m][n]%2
        return None

def main():
    a = Solution()
    b = [[1,0,0,0,1,1,0,0],
         [1,0,0,0,1,1,0,0],
         [1,0,0,0,1,1,0,0],
         [1,0,0,0,1,1,0,0],
         ]
    print b
    a.gameOfLife(b)
    print b



if __name__ == "__main__":
    main()
