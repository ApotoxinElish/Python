import pygame as p
import sys as s

oratio = 1.5

class Card:
    def __init__(self, content):
        self.content = content
        self.oimage = p.image.load(content['image']).convert()
        self.orect = self.oimage.get_rect()
        self.image = p.transform.smoothscale(self.oimage, (int(self.orect.width/oratio), int(self.orect.height/oratio)))
        self.rect = self.image.get_rect()
        


'''
cost 费用
level 等级
cardType 卡牌类型
classSymbol 职阶符号
title 名称
subtitle 副名称
skills 技能
traits 属性
ability 能力
elderSignAbility 远古印记能力
health 生命值
sanity 神智值
skillTestIcons 技能检定图标
productSetInformation 产品图标
'''


class Investigator():  # 调查员
    pass


class Asset():  # 支援
    pass


class Skill():  # 技能
    pass


class Event():  # 事件
    pass


class Weakness():
    pass


'''
encounterSetSymbol 遭遇组符号
cardType 卡牌类型
title 名称
traits 属性
ability 能力
enemyFightValue 敌人攻击值
enemyHealthValue 敌人生命值
enemyEvadeValue 敌人躲避值
damage 伤害
horror 恐惧
shroud 隐藏值
clueValue 线索值
connectionSymbols 连接符号
act/agenda Sequence 场景/密谋编号
ClueThreshold 线索目标值
doomThreshold 毁灭目标值
productSetInformation 产品图标
encounterSetNumber 遭遇组牌数
'''


class Agenda():  # 密谋
    pass


class Act():  # 场景
    pass


class ScenarioReference():  # 冒险辅助
    pass


class Location(Card):  # 地点
    def __init__(self, content):
        Card.__init__(self, content)
        self.rect.height = int(self.rect.height/2)
        self.image = self.image.subsurface(self.rect).copy()
        self.rect = self.image.get_rect()


class Enemy():  # 敌人
    pass


class Treachery():  # 诡计
    pass


def test():
    p.init()
    
    size = width, height = int(1440/oratio), int(900/oratio)
    bg = (255, 255, 255)
    
    screen = p.display.set_mode(size, p.RESIZABLE)
    p.display.set_caption('诡镇奇谈LCG')

    ratio = 1.5

    content = {'cardType': 'LOCATION',
               'title': 'Study',
               'productSetInformation': ('Core Set', 111),
               'image': 'Scenario/Location/01111.png'}
    location = Location(content)

    clock = p.time.Clock()

    while True:
        for event in p.event.get():
            if event.type == p.QUIT:
                s.exit()

        #location.rect.center = width//2, height//2

        screen.blit(location.image, location.rect)

        p.display.flip()
        clock.tick(25)


if __name__ == "__main__":
    test()
