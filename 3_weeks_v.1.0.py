import random
SIZE = [100, 100]
ENEMYS = {'slime': {'str': 1, 'def': 0, 'hp': 7, 'mhp': 7,  'exp': 1, 'level': 2, 'char': 'o', 'name': 'slime', 'pos': [0, 0]},
         'cat': {'str': 4, 'def': 0, 'hp': 5, 'mhp': 5, 'exp': 2, 'level': 4, 'char': 'n', 'name': 'cat'},
         'bird': {'str': 5, 'def': 2, 'hp': 3, 'mhp': 3, 'exp': 4, 'level': 5, 'char': 'v', 'name': 'bird'},
         'dog': {'str': 10, 'def': 3, 'hp': 15, 'mhp': 15, 'exp': 9, 'level': 7, 'char': 'm', 'name': 'dog'},
         'wolf': {'str': 14, 'def': 7, 'hp': 12, 'mhp': 12, 'exp': 17, 'level': 9, 'char': 'w', 'name': 'wolf'},
         'golem': {'str': 28, 'def': 2, 'hp': 40, 'mhp': 40, 'exp': 30, 'level': 13, 'char': 'l', 'name': 'golem'},
         'knight': {'str': 30, 'def': 18, 'hp': 30, 'mhp': 30, 'exp': 40, 'level': 14, 'char': 'k', 'name': 'knight'},
         'undead': {'str': 36, 'def': 15, 'hp': 150, 'mhp': 150, 'exp': 60, 'level': 15, 'char': 'f', 'name': 'undead'}}
LEVELS = [{'exp': 10, 'str': 2, 'def': 0, 'mhp': 6, 'regen': 0.6},
          {'exp': 25, 'str': 3, 'def': 1, 'mhp': 7, 'regen': 0.8},
          {'exp': 45, 'str': 5, 'def': 2, 'mhp': 9, 'regen': 1.0},
          {'exp': 75, 'str': 6, 'def': 4, 'mhp': 12, 'regen': 1.2},
          {'exp': 150, 'str': 8, 'def': 5, 'mhp': 16, 'regen': 1.4},
          {'exp': 250, 'str': 10, 'def': 7, 'mhp': 21, 'regen': 1.6},
          {'exp': 350, 'str': 13, 'def': 9, 'mhp': 28, 'regen': 1.8},
          {'exp': 500, 'str': 16, 'def': 11, 'mhp': 35, 'regen': 2.0},
          {'exp': 700, 'str': 19, 'def': 13, 'mhp': 42, 'regen': 2.2}, 
          {'exp': 950, 'str': 22, 'def': 15, 'mhp': 50, 'regen': 2.4},
          {'exp': 1200, 'str': 25, 'def': 17, 'mhp': 60, 'regen': 2.6},
          {'exp': 1600, 'str': 29, 'def': 20, 'mhp': 70, 'regen': 2.8},
          {'exp': 2200, 'str': 33, 'def': 23, 'mhp': 80, 'regen': 3.0},
          {'exp': 3000, 'str': 36, 'def': 26, 'mhp': 90, 'regen': 3.5},
          {'exp': 4000, 'str': 40, 'def': 30, 'mhp': 100, 'regen': 4.0},
          {'exp': 9999}]
DAYS = [['slime'],
        ['slime'],
        ['slime', 'cat'],
        ['slime', 'cat'],
        ['bird', 'slime'],
        ['bird'],
        ['dog', 'cat'],
        ['dog', 'cat'],
        ['dog'],
        ['wolf', 'cat'],
        ['wolf', 'dog'],
        ['wolf', 'golem'],
        ['wolf'],
        ['golem'],
        ['knight', 'golem'],
        ['golem', 'wolf'],
        ['knight', 'golem'],
        ['knight'],
        ['knight', 'undead'],
        ['undead'],
        ['undead'], []]
# field[x, y]
def genfld(SIZE):
    seed = random.randint(1024, 2048)
    field = []
    for a in range(SIZE[1]):
        cha = max(20 - a, 0) + max(20 + (a - SIZE[1]), 0)
        string = ''
        for b in range(SIZE[0]):
            chb = max(20 - b, 0) + max(20 + (b - SIZE[0]), 0)
            if cha ** 2 + chb ** 2 > ((seed + a ** 2 + b ** 2) ** 2) % 800:
                string += '#'
            else:
                string += '.'
        field.append(string)
    return field
    
    
def move(string, ppos, size):
    pos = ppos[:]
    if string[0] == 'u':
        pos[1] -= 1
    if string[0] == 'r':
        pos[0] += 1
    if string[0] == 'd':
        pos[1] += 1
    if string[0] == 'l':
        pos[0] -= 1
    if field[pos[1]][pos[0]] != '#':
        for a in enemys:
            if pos == a['pos']:
                pos = ppos
                a['hp'] -= int(max(pd['str'] - a['def'], 0))
                enemydata[0] = a['char']
                enemydata[1] = a['name']
                hp = (min(a['mhp'] - a['hp'], a['mhp']) * 8) // a['mhp']
                enemydata[2] = [8 - hp, hp]
                enemydata[3] = a['level']
        return pos
    return ppos
        
        
def indel(string, pos, char):
    newstring = ''
    if pos:
        newstring = string[:pos]
    newstring += char
    if len(string) > pos + 1:
        newstring += string[pos + 1:]
    return newstring
    
    
def border(field):
    field[0] = '#' * len(field[0])
    field[-1] = '#' * len(field[-1])
    for a in range(len(field)):
        field[a] = '#' + field[a][1:-1] + '#'
        
        
def helpme():
    print('')
    print('Type up/left/down/right to move or attack')
    print('Type pass to skip move')
    print('Type exit to exit')
    print('Shortcuts: u/l/d/r for move, h for help, e for exit, other letter for skip') 
    print('Trees are poisoned')
    print('Type help to show help again.')
    print('Survive 3 weeks to win\n')
    print("Minin Nikita, Sep, 11. '21")
    
   
def tick():
    global enemys
    ppos = pd['pos']
    damaged = False
    for a in enemys:
        pos = a['pos']
        if sum([abs(pos[a] - ppos[a]) for a in range(2)]) == 1:
            damaged = True
            pd['hp'] -= max(0, a['str'] - pd['def'])
        else:
            dif = [ppos[a] - pos[a] for a in range(2)]
            step = []
            step.append([(dif[0] - 1) ** 2 + dif[1] ** 2, [1, 0]])
            step.append([(dif[0] + 1) ** 2 + dif[1] ** 2, [-1, 0]])
            step.append([dif[0] ** 2 + (dif[1] - 1) ** 2, [0, 1]])
            step.append([dif[0] ** 2 + (dif[1] + 1) ** 2, [0, -1]])
            step.sort()
            pos = [pos[a] + step[0][1][a] for a in range(2)]
            if field[pos[0]][pos[1]] != '#' and pos not in [a['pos'] for a in enemys]:
                a['pos'] = pos[:]  
    if random.random() * 10 < 1/(len(enemys) + 1):
        enemys.append({})
        enemy = random.choice(DAYS[day - 1])
        for a in ENEMYS[enemy]:
            enemys[-1][a] = ENEMYS[enemy][a]
        pos = [0, 0]
        while field[pos[0]][pos[1]] == '#' or pos in [a['pos'] for a in enemys[:-1]] or sum([abs(pos[a] - ppos[a]) for a in range(2)]) < 25:
            pos = [random.randint(20, SIZE[a] - 20) for a in range(2)]
        enemys[-1]['pos'] = pos[:]        
    if not damaged:
        pd['regenpr'] += pd['regen']
        pd['hp'] = int(min(pd['hp'] + pd['regenpr'], pd['mhp']))
        pd['regenpr'] = pd['regenpr'] % 1
    if pd['hp'] < 1:
        pd['char'] = 't'
        pd['hp'] = 'DEAD'
    
    
field = genfld(SIZE)  
border(field)
pd = {'pos': [30, 30], 'exp': 0, 'str': 1, 'def': 0, 'mhp': 5, 'regen': 0.4, 'regenpr': 0, 'level':1, 'hp': 5, 'char': 'P', 'psn': 0}
string = ' '
helpme()
cycles = 0
enemys = []
day = 1
enemydata = [' ', '', [0, 8], '-']
input('Type anything to start!')

while string != 'e' and cycles < 4200 and pd['hp'] != 'DEAD':
    ppos = pd['pos']
    cycles += 1
    if not cycles % 200:
        day += 1
    if string:
        char = string[0]
    else:
        char = ' '
        string = ' '
    if char != 'h':
        ppos = move(string, ppos, SIZE)
        if any([ppos[a] < 20 or ppos[a] >= SIZE[a] - 20 for a in range(2)]):
            pd['psn'] += 5
        elif pd['psn']:
            pd['psn'] -= 1
        if pd['psn'] > 99:
            pd['hp'] -= (pd['psn'] - 90) // 10
        pos = [min(max(ppos[a] - 7, 0), SIZE[a] - 15) for a in range(2)]
        pd['pos'] = ppos
        tick()
        ofield = field[:]
        ofield[ppos[1]] = indel(ofield[ppos[1]], ppos[0], pd['char'])
        for a in enemys:
            ofield[a['pos'][1]] = indel(ofield[a['pos'][1]], a['pos'][0], a['char'])
        ofield = [a[pos[0]:pos[0] + 15] + '#' for a in ofield]
        outdata = ofield[pos[1]:pos[1] + 15] + ['#' * 16]
        outdata[0] += '    {}, {}'.format(ppos[0], ppos[1])
        outdata[1] += '    HP:{}/{}'.format(pd['hp'], pd['mhp'])
        outdata[2] += '    STR:{}'.format(pd['str'])
        outdata[3] += '    DEF:{}'.format(pd['def'])
        outdata[4] += '    EXP:{}/{}'.format(pd['exp'], LEVELS[pd['level'] - 1]['exp'])
        outdata[5] += '    LVL:{}'.format(pd['level'])
        outdata[6] += '    DAY:{}'.format(day)
        outdata[7] += '    PSN:{}%'.format(pd['psn'])
        outdata[10] += '    ---[{}]---'.format(enemydata[0])
        outdata[11] += '    ' + enemydata[1]
        outdata[12] += '    ' + '|' * enemydata[2][0] + '.' * enemydata[2][1]
        outdata[13] += '    LVL:{}'.format(enemydata[3])
        print(*outdata, sep='\n')
        kille = -1
        for a in range(len(enemys)):
            if enemys[a]['hp'] < 1:
                kille = a
        if kille != -1:
            pd['exp'] += int(enemys[kille]['exp'] / (1.5 ** max(0, pd['level'] - enemys[kille]['level'])))
            del enemys[kille]
            lvl = pd['level']
            exp = pd['exp']
            while exp >= LEVELS[lvl - 1]['exp']:
                pd['level'] += 1
                lvl += 1
                pd['str'] = LEVELS[lvl - 2]['str']
                pd['def'] = LEVELS[lvl - 2]['def']
                pd['mhp'] = LEVELS[lvl - 2]['mhp']
                pd['regen'] = LEVELS[lvl - 2]['regen']
    else:
        helpme()
    if pd['hp'] == 'DEAD':
        print('YOU ARE DEAD.')
    if cycles == 4200:
        print('YOU WIN!.')
    string = input()