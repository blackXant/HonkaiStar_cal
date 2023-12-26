# -*- coding: utf-8 -*-
import PySimpleGUI as sg

sg.theme('BlueMONO')   # デザインテーマの設定

# タブ1のレイアウト
layout_tab1 = [
    [sg.Text('スキル効果命中基礎確率：'), sg.InputText(k="skill")],
    [sg.Text('キャラステータス効果命中：'), sg.InputText(k="status")],
    [sg.Text('敵の効果抵抗：'), sg.InputText(k="enemy")],
    [sg.Button('OK(一般)'), sg.Button('キャンセル')],
    [sg.Text('命中率:'), sg.Text('0', key='result'), sg.Text('%')]
]

# タブ2のレイアウト（例として同じ内容）
layout_tab2 = [
    [sg.Text('スキル効果命中基礎確率：'), sg.InputText(k="skill2")],
    [sg.Text('キャラステータス効果命中：'), sg.InputText(k="status2")],
    [sg.Text('敵の効果抵抗：'), sg.InputText(k="enemy2")],
    [sg.Button('OK(銀狼)'), sg.Button('キャンセル')],
    [sg.Text('命中率:'), sg.Text('0', key='result2'), sg.Text('%')]
]

# タブグループのレイアウト
layout = [
    [sg.TabGroup([
        [sg.Tab('一般', layout_tab1)],
        [sg.Tab('銀狼', layout_tab2)]
    ])]
]

# ウィンドウの生成
window = sg.Window('崩壊スターレイル効果命中計算', layout, font=(None,14))

def cal(tab_num, skill_key, status_key, enemy_key, result_key):
    skill = int(values[skill_key])
    status = int(values[status_key])
    enemy = int(values[enemy_key])
    txt = skill * (1 + (status/100)) * (1 - (enemy/100))
    window[result_key].update(txt)  # 結果の表示を更新
    
def cal2(tab_num, skill_key, status_key, enemy_key, result_key):
    skill = int(values[skill_key])
    status = int(values[status_key])
    enemy = int(values[enemy_key])
    txt = skill * (1 + (status /100)) * (1 - ((enemy-20)/100))
    window[result_key].update(txt)  # 結果の表示を更新

# イベントループ
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'キャンセル':
        break
    elif event == 'OK(一般)':
        # タブ1の計算
        cal(1, "skill", "status", "enemy", "result")
        
        
    elif event == 'OK(銀狼)':
        # タブ2の計算
        cal2(2, "skill2", "status2", "enemy2", "result2")

window.close()
