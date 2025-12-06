import random

def simulate_game(prob_a):
    """模拟一局比赛，prob_a 是A选手每球获胜的概率"""
    score_a = 0
    score_b = 0
    while True:
        # 模拟每一球的胜负
        if random.random() < prob_a:
            score_a += 1
        else:
            score_b += 1
        
        # 判断是否分出胜负
        if (score_a >= 11 or score_b >= 11) and abs(score_a - score_b) >= 2:
            return score_a, score_b

def simulate_match(prob_a, best_of=3):
    """模拟一场比赛，best_of 是“几局几胜”（3代表三局两胜，5代表五局三胜）"""
    wins_a = 0
    wins_b = 0
    max_games = (best_of + 1) // 2  # 获胜需要的局数
    while wins_a < max_games and wins_b < max_games:
        score_a, score_b = simulate_game(prob_a)
        if score_a > score_b:
            wins_a += 1
        else:
            wins_b += 1
    return wins_a, wins_b

# 测试示例：A选手每球获胜概率为0.55，模拟一场三局两胜的比赛
if __name__ == "__main__":
    prob_a = 0.55
    wins_a, wins_b = simulate_match(prob_a, best_of=3)
    print(f"A选手赢了 {wins_a} 局，B选手赢了 {wins_b} 局")
