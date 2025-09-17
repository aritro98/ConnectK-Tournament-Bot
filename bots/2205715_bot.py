import copy
import random
import time

my_id=None
connect_k=None
rows=None
cols=None
TIME_LIMIT=0.98 # Seconds for the next move

def init(isFirst,connectK):
    global my_id,connect_k
    my_id=1 if isFirst else 2
    connect_k=connectK

def next_move(board):
    global rows,cols
    rows=len(board)
    cols=len(board[0])
    start_time=time.time()
    valid_columns=[c for c in range(cols) if board[0][c]==0]

    # Check for immediate win
    for col in valid_columns:
        temp_board=make_move(board,col,my_id)
        if check_win(temp_board,my_id):
            return col

    # Block opponent's win
    opp_id=2 if my_id==1 else 1
    for col in valid_columns:
        temp_board=make_move(board,col,opp_id)
        if check_win(temp_board,opp_id):
            return col

    # Iterative deepening minimax for the strongest move within the time limit
    best_col=random.choice(valid_columns)
    depth=2
    while True:
        move,_=minimax(board,depth,-float('inf'),float('inf'),True,start_time,TIME_LIMIT)
        if move is not None:
            best_col=move
        if time.time()-start_time>TIME_LIMIT:
            break
        depth+=1
    return best_col

def minimax(board,depth,alpha,beta,maximizingPlayer,start_time,time_limit):
    global my_id,rows,cols,connect_k
    opp_id=2 if my_id==1 else 1
    valid_columns=[c for c in range(cols) if board[0][c]==0]
    if (depth==0 or not valid_columns or time.time()-start_time>time_limit):
        return None,evaluate_board(board,my_id,connect_k)

    # Early win/loss detection
    for col in valid_columns:
        temp_board=make_move(board,col,my_id if maximizingPlayer else opp_id)
        if check_win(temp_board,my_id if maximizingPlayer else opp_id):
            if maximizingPlayer:
                return col,float('inf')
            else:
                return col,-float('inf')
    best_col=None
    if maximizingPlayer:
        value=-float('inf')
        for col in valid_columns:
            temp_board=make_move(board,col,my_id)
            _,new_score=minimax(temp_board,depth-1,alpha,beta,False,start_time,time_limit)
            if new_score>value:
                value=new_score
                best_col=col
            alpha=max(alpha,value)
            if beta<=alpha or time.time()-start_time>time_limit:
                break
        return best_col,value
    else:
        value=float('inf')
        for col in valid_columns:
            temp_board=make_move(board,col,opp_id)
            _,new_score=minimax(temp_board,depth-1,alpha,beta,True,start_time,time_limit)
            if new_score<value:
                value=new_score
                best_col=col
            beta=min(beta,value)
            if beta<=alpha or time.time()-start_time>time_limit:
                break
        return best_col,value

def make_move(board,col,player):
    new_board=copy.deepcopy(board)
    for r in range(rows-1,-1,-1):
        if new_board[r][col]==0:
            new_board[r][col]=player
            break
    return new_board

def check_win(board,player):
    for r in range(rows):
        for c in range(cols):
            if board[r][c]!=player:
                continue
            for dr,dc in [(0,1),(1,0),(1,1),(1,-1)]:
                count=0
                for k in range(connect_k):
                    nr,nc=r+dr*k,c+dc*k
                    if 0<=nr<rows and 0<=nc<cols and board[nr][nc]==player:
                        count+=1
                    else:
                        break
                if count==connect_k:
                    return True
    return False

def score_window(window,player,connect_k):
    opponent=2 if player==1 else 1
    count=window.count(player)
    opp_count=window.count(opponent)
    empty_count=window.count(0)
    if count==connect_k:
        return 100000  # Winning line
    elif count==connect_k-1 and empty_count==1:
        return 5000  # Almost winning
    elif count==connect_k-2 and empty_count==2:
        return 1000  # Very strong
    elif count==connect_k-3 and empty_count==3:
        return 200   # Noticeable threat

    # Defensive:Blocks opponent's threats
    if opp_count==connect_k-1 and empty_count==1:
        return -4000  # Opponent can win
    elif opp_count==connect_k-2 and empty_count==2:
        return -800
    elif opp_count==connect_k-3 and empty_count==3:
        return -100
    return 0

def evaluate_board(board,player,connect_k):
    rows=len(board)
    cols=len(board[0])
    center_col=cols//2
    score=0

    # Reward control of the center column
    center_array=[board[r][center_col] for r in range(rows)]
    score+=center_array.count(player)*6

    # Horizontal,vertical and both diagonal windows
    for r in range(rows):
        for c in range(cols-connect_k+1):
            window=[board[r][c+i] for i in range(connect_k)]
            score+=score_window(window,player,connect_k)

    for c in range(cols):
        for r in range(rows-connect_k+1):
            window=[board[r+i][c] for i in range(connect_k)]
            score+=score_window(window,player,connect_k)

    for r in range(rows-connect_k+1):
        for c in range(cols-connect_k+1):
            window=[board[r+i][c+i] for i in range(connect_k)]
            score+=score_window(window,player,connect_k)

    for r in range(connect_k-1,rows):
        for c in range(cols-connect_k+1):
            window=[board[r-i][c+i] for i in range(connect_k)]
            score+=score_window(window,player,connect_k)
    return score
