
# -*- coding: utf-8 -*-

# BMI関数
# 引数は身長(cm),体重(kg),日本基準適用の是非の順に指定
def bmi(h, w = False, j = False):

    # 標準体重を計算
    s_weight = round(22*(h/100)**2, 2)

    # BMI(body mass index)を計算
    x = round(w/((h/100)**2), 2)

    # WHO の基準
    if x < 16:
        advice_w = "痩せすぎです"

    elif 16 <= x < 17:
        advice_w = "痩せています"

    elif 17 <= x < 18.5:
        advice_w = "痩せ気味です"

    elif 18.5 <= x < 25:
        advice_w = "普通体重です"

    elif 25 <= x < 30:
        advice_w = "前肥満です"

    elif 30 <= x < 35:
        advice_w = "肥満（1度）です"

    elif 35 <= x < 40:
        advice_w = "肥満（2度）です"

    else:
        advice_w = "肥満（3度）です"

    # 日本の基準
    if x < 18.5:
        advice_j = "低体重です"

    elif 18.5 <= x < 25:
        advice_j = "普通体重です"

    elif 25 <= x < 30:
        advice_j = "肥満（１度）です"

    elif 30 <= x < 35:
        advice_j = "肥満（2度）です"

    elif 35 <= x < 40:
        advice_j = "肥満（3度）です"

    elif x > 40:
        advice_j = "肥満です"

    # 体重を省略すると標準体重のみを返します
    if w == False:
        return s_weight

    # 第3引数をTrueにすると日本基準で返します
    elif j == True:
        return x, s_weight, advice_j

    # 第3引数がTrue以外の値であればWHO基準で返します
    else:
        return x, s_weight, advice_w

# 以下、サンプルデータを入力して動作を確認しています
# 身長170cm,体重75kg
sample_1 = bmi(170, 75)

# 身長170cm,体重75kg
sample_2 = bmi(170, 75, True)

# 身長183cmのみを入力
sample_3 = bmi(183)

print(sample_1)
print(sample_2)
print(sample_3)
