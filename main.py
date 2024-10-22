from pdftoc import merge_toc
from pdftoc import parse_toc

pdf = "test.pdf"
start = 8  # 正文第一页在文中的位置
toc = """
1 (p0-1): 序 周礼全
1 (p1): 第一章 罗素哲学思想的两个时期
1 (p1-2): 一、1910年前的客观唯心论
8 (p1-3): 二、1912年后的主观唯心论
17 (p2): 第二章 从休谟、康德到罗素
19 (p2-2): 一、从休谟说起
23 (p2-3): 二、经过康德
33 (p2-4): 三、谈到罗素
50 (p3): 第三章 歪曲了形式逻辑导致形而上学(一)
54 (p3-2): 一、罗素的逻辑分析主义
63 (p3-3): 二、罗素的一般与个别论
76 (p3-4): 三、罗素的先验主义
82 (p3-5): 六、罗素的存在论
83 (p3-6): 四、关于文法上和逻辑上的主词
88 (p4): 第四章 歪曲了形式逻辑导致形而上学(二)
96 (p4-2): 七、罗素的指示词或摹状词论
105 (p4-3): 八、罗素关于类的理论
201 (p7-2): 一、以感觉材料为基本原料的构造论
204 (p7-3): 二、在感觉材料上做文章
206 (p7-4): 三、用奥卡姆剃刀剃掉实体
214 (p7-5): 四、所谓“公共空间”的构造
222 (p7-6): 五、所谓“事物”的构造
231 (p8): 第八章 对中立一无论的批判
231 (p8-2): 一、中立一元论与《物的分析》、《心的分析》
233 (p8-3): 二、物心的同元与物心的分别
237 (p8-4): 三、心灵的构造
249 (p8-5): 四、物质的构造与中立一元论的本质
268 (p9): 附录
268 (p9-2): 一、罗素小传
273 (p9-3): 二、罗素主要著作年表
112 (p4-4): 九、罗素的逻辑构造论
124 (p5): 第五章 对罗索感觉材料论的批判
126 (p5-2): 一、用感觉内容替换感觉对象
136 (p5-3): 三、没有变化发展的感觉
140 (p5-4): 四、封闭的感觉材料体系
146 (p5-5): 五、罗素不承认蓝本因
151 (p5-6): 二、脱离了社会实践的感觉
152 (p5-7): 六、把感觉和梦觉、幻觉混淆了
157 (p5-8): 七、把感觉材料说成是私有的
163 (p6): 第六章 从感觉材料的直接认识能推出客观事物的间接知识吗?
164 (p6-2): 一、所谓对感觉材料的直接认识
176 (p6-3): 二、从直接认识到间接知识的推论行得通吗?
197 (p7): 第七章 逻辑构造能代替推论吗?
279 (p9-4): 三、金岳霖主要哲学论著年表
283 (p9-5): 四、名词索引
283 (p9-6): 跋 冯契”
"""

def app():
    toc0 = parse_toc(toc, start - 1)
    merge_toc(toc0, pdf, None)


if __name__ == '__main__':
    app()
