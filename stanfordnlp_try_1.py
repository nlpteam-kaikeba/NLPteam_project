from stanfordcorenlp import StanfordCoreNLP
import snownlp
from nltk.tree import Tree


filename = r"/Users/lingrowzhang/Documents/Artificial-Intelligence-for-NLP/project_1/stanford-corenlp-full-2018-10-05"

zh_model = StanfordCoreNLP(filename, port=9999, lang='zh')
# en_model = StanfordCoreNLP(filename, port=9999, lang='en')

zh_sentence = '你觉得会说那一句话，有可能是其中一句话！'
# en_sentence = 'I love natural language processing technology!'

print('Tokenize:', zh_model.word_tokenize(zh_sentence))
# print('Tokenize:', en_model.word_tokenize(en_sentence))

print('Part of Speech:', zh_model.pos_tag(zh_sentence))
# print('Part of Speech:', en_model.pos_tag(en_sentence))

# 实体名字
print('Named Entities:', zh_model.ner(zh_sentence))

# 句法成分分析,生成句法树
print('Constituency Parsing:', zh_model.parse(zh_sentence) + "\n")
# print('Constituency Parsing:', en_model.parse(en_sentence))

# 依存句法分析
print('Dependency:', zh_model.dependency_parse(zh_sentence))
# print('Dependency:', en_model.dependency_parse(en_sentence))

sentence ='Guangdong University of Foreign Studies is located in Guangzhou.'


tree = Tree.fromstring(zh_model.parse(zh_sentence))
tree.draw()


print(tree.height())# 树的高度

print(tree.leaves())# 树的叶子结点

tree.productions()# 生成与树的非终端节点对应的结果


zh_model.close()#释放，否则后端服务器将消耗大量内存

